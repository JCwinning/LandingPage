import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
import datetime
from zoneinfo import ZoneInfo

# Load environment variables from .env
load_dotenv()

# Tool definition
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    elif city.lower() == "shanghai":
        tz_identifier = "Asia/Shanghai"
    elif city.lower() == "london":
        tz_identifier = "Europe/London"
    elif city.lower() == "tokyo":
        tz_identifier = "Asia/Tokyo"
    else:
        # Default to checking if the city name works as a timezone directly
        try:
            # Very basic fallback for common cities
            city_fmt = city.replace(" ", "_").title()
            tz_identifier = f"Etc/GMT" # Placeholder
            # Actually, let's keep it simple as per original
            return {
                "status": "error",
                "error_message": f"Sorry, I don't have timezone information for {city}."
            }
        except:
            return {
                "status": "error",
                "error_message": f"Sorry, I don't have timezone information for {city}."
            }

    try:
        tz = ZoneInfo(tz_identifier)
        now = datetime.datetime.now(tz)
        report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

# Streamlit UI Configuration
st.set_page_config(page_title="ADK Chat Bot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
        color: #ffffff;
    }
    .stChatMessage {
        border-radius: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Google ADK Chat Bot")
st.caption("Powered by Google ADK & OpenRouter")

# Initialize Agent and Runner in session state to persist resources
@st.cache_resource
def initialize_agent():
    # Model setup
    openrouter_model = LiteLlm(
        model="openrouter/minimax/minimax-m2.5",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        api_base="https://openrouter.ai/api/v1"
    )

    # Agent setup
    agent = Agent(
        name="my_adk_agent_openrouter",
        model=openrouter_model,
        description="Assistant using OpenRouter via Google ADK.",
        instruction="Be a helpful assistant. You can provide the current time for cities like New York, Shanghai, London, and Tokyo using your tools.",
        tools=[get_current_time],
    )
    
    session_service = InMemorySessionService()
    runner = Runner(agent=agent, session_service=session_service, app_name="adk_chat_app")
    
    return runner

runner = initialize_agent()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Async function to process agent turn
async def process_message(prompt):
    full_response = ""
    # Creating a placeholder for the assistant message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Runner.run_async returns an AsyncGenerator of Event objects
            async for event in runner.run_async(
                user_id="default_user",
                session_id="default_session",
                message=prompt
            ):
                # Try multiple ways to get text as framework versions/implementations might vary
                text_chunk = ""
                
                # Check for .text property (common shortcut)
                if hasattr(event, "text") and event.text:
                    text_chunk = event.text
                # Check for .content.parts (common in Vertex/GenAI based events)
                elif hasattr(event, "content") and event.content:
                    if hasattr(event.content, "parts") and event.content.parts:
                        for part in event.content.parts:
                            if hasattr(part, "text"):
                                text_chunk += part.text
                
                if text_chunk:
                    full_response += text_chunk
                    message_placeholder.markdown(full_response + "▌")
                
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error during agent execution: {str(e)}")
            return None
            
    return full_response

# React to user input
if prompt := st.chat_input("What is on your mind?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from agent
    with st.spinner("Agent is thinking..."):
        # Run the async process
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(process_message(prompt))
        
    if response:
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
