import os
from dotenv import load_dotenv
from crewai import LLM

# Load variables from .env
load_dotenv()

# Read API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create the LLM
llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=GEMINI_API_KEY
)