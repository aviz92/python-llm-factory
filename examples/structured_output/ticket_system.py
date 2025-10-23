from enum import Enum
from typing import Annotated

from instructor import llm_validator
from pydantic import BaseModel, BeforeValidator, Field

from python_llm_factory.config.settings import Settings
from python_llm_factory.instructor_llm.instructor_factory import LlmInstructorFactory

llm = LlmInstructorFactory(
    settings=Settings().gemini.gemini_2_5_flash,
)


class TicketCategory(str, Enum):
    """Enumeration of categories for incoming tickets."""

    GENERAL = "general"
    ORDER = "order"
    BILLING = "billing"


class CustomerSentiment(str, Enum):
    """Enumeration of customer sentiment labels."""

    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"


class ValidationTicket(BaseModel):
    reply: str = Field(description="Your reply that we send to the customer.")
    category: TicketCategory
    confidence: float = Field(ge=0, le=1)
    sentiment: CustomerSentiment
    content: Annotated[
        str,
        BeforeValidator(
            llm_validator(
                statement="Never say things that could hurt the reputation of the company. ",
                client=llm.client,
                model="gemini-2.5-flash",
                allow_override=True,
            )
        ),
    ]


class Ticket(BaseModel):
    reply: str = Field(description="Your reply that we send to the customer.")
    category: TicketCategory
    confidence: float = Field(ge=0, le=1)
    sentiment: CustomerSentiment


def process_ticket(customer_message: str) -> Ticket:
    reply = llm.completions_create(
        # response_model=Ticket,
        response_model=ValidationTicket,
        max_retries=3,
        messages=[
            {
                "role": "system",
                "content": "Analyze the incoming customer message and predict the values for the ticket.",
            },
            {"role": "user", "content": customer_message},
        ],
    )

    return reply
