from enum import Enum

from pydantic import BaseModel, Field, field_validator
from pydantic_core.core_schema import FieldValidationInfo

from examples.instructor_examples.create_gemini_client import create_default_client
from python_llm_factory.hooks.logging_hooks import add_logging_hooks, log_kwargs


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str = Field(..., pattern=r"^\d{5}(-\d{4})?$")


class Contact(BaseModel):
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    phone: str | None = Field(None, pattern=r"^\+?1?-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$")


class Ticket(BaseModel):
    id: str
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=10)
    priority: Priority
    assignee: str | None = None
    tags: list[str] = Field(default_factory=list, max_length=5)
    estimated_hours: float | None = Field(None, gt=0, le=100)

    @field_validator("estimated_hours")
    @classmethod
    def validate_hours(cls, v: float | None) -> float | None:
        if v is not None and v % 0.5 != 0:
            raise ValueError("Hours must be in 0.5 increments")
        return v


class CustomerSupport(BaseModel):
    customer_name: str
    customer_contact: Contact
    customer_address: Address
    tickets: list[Ticket] = Field(..., min_length=1)
    total_estimated_time: float = Field(..., gt=0)

    @field_validator("total_estimated_time")
    @classmethod
    def validate_total_time(cls, v: float, info: FieldValidationInfo) -> float:  #
        if "tickets" in info.data:
            ticket_time = sum(t.estimated_hours or 0 for t in info.data["tickets"])
            if abs(v - ticket_time) > 0.1:  # Allow small floating point differences
                raise ValueError(f"Total time {v} must match sum of ticket times {ticket_time}")
        return v


if __name__ == "__main__":
    client = create_default_client()
    add_logging_hooks(client=client, handler=log_kwargs)

    support_case = client.completions_create(
        response_model=CustomerSupport,
        temperature=0.8,
        max_retries=3,
        max_tokens=2048,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
                "Always return a single structured CustomerSupport object, "
                "even if multiple tickets are included. Do not create separate tool calls.",
            },
            {
                "role": "user",
                "content": """
                Support case for Sarah Johnson (sarah.johnson@techcorp.com, +1-555-123-4567).
                Address: 123 Tech Street, San Francisco, CA 94105.

                Two tickets:
                1. "Login system completely broken" - CRITICAL priority, needs 4.5 hours, tags: authentication, security
                2. "Email notifications not working" - MEDIUM priority, needs 2 hours, tags: email, notifications

                Total estimated time: 6.5 hours
                """,
            },
        ],
    )

    print(
        f'"Support case for {support_case.customer_name} ({support_case.customer_contact.email}, '
        f"{support_case.customer_contact.phone})."
    )
    print(
        f"Address: {support_case.customer_address.street}, {support_case.customer_address.city}, "
        f'{support_case.customer_address.postal_code}."'
    )
    for ticket in support_case.tickets:
        print(f'- Ticket "{ticket.title}" with priority {ticket.priority} requiring {ticket.estimated_hours} hours.')
    print(f"Total estimated time: {support_case.total_estimated_time} hours.")

    print(f"Total tickets: {len(support_case.tickets)}")
    print(f"Critical tickets: {len([t for t in support_case.tickets if t.priority == Priority.CRITICAL])}")
