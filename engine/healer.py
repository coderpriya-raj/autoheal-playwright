import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def suggest_new_selector(broken_selector, html_context):
    try:
        # UPDATED: Using the version 2.5 flash model found in your list
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"HTML: {html_context}\nFix CSS selector: {broken_selector}. Return ONLY the CSS."
        )
        return response.text.strip().replace('`', '')
    except Exception as e:
        return f"Healing Error: {str(e)}"