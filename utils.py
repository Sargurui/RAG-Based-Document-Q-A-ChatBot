import os
from dotenv import load_dotenv

# Load environment variables from the .env file
def load_env():
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Make sure GEMINI_API_KEY is set in your .env file.")
