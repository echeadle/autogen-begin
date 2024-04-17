import os
from dotenv import load_dotenv

# Start importing autogen. In future import functions
import autogen

load_dotenv()

model = os.getenv("MODEL")
api_key = os.getenv("OPENAI_API_KEY")
