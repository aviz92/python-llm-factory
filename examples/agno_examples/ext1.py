from pprint import pprint

from agno.agent import Agent
from agno.db.sqlite.sqlite import SqliteDb
from agno.models.google.gemini import Gemini
from dotenv import load_dotenv

from python_llm_factory import Settings

load_dotenv()
USER_ID = '123'

db = SqliteDb(
    db_file="memory.db",
    session_table="sessions",
    memory_table="user_memories",
)

agent = Agent(
    model=Gemini(api_key=Settings().gemini.gemini_2_5_flash.api_key),
    user_id=USER_ID,
    db=db,
    enable_user_memories=True,
    add_datetime_to_context=True,
    markdown=True,
    add_history_to_context=True,
    enable_agentic_memory=True,
)

if __name__ == "__main__":
    agent.print_response("My name is Peter Rabbit and I like to eat carrots.")

    # Get memories using the agent's method
    memories = agent.get_user_memories(user_id=USER_ID)
    print(f"Memories about {USER_ID}:")
    pprint(memories)

    agent.print_response("What is my favorite food?")
    agent.print_response("My best friend is Jemima Puddleduck.")

    # Get updated memories
    memories = agent.get_user_memories(user_id=USER_ID)
    print(f"Memories about {USER_ID}:")
    pprint(memories)

    agent.print_response("Recommend a good lunch meal, who should i invite?")
    agent.print_response("What have we been talking about?")
