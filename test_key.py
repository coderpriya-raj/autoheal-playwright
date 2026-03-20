import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("--- Available Models ---")
try:
    # This lists every model your key can access
    for model in client.models.list():
        print(f"ID: {model.name} | Display: {model.display_name}")
except Exception as e:
    print(f"Failed to list: {e}")