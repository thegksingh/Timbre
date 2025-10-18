import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class TextPolisher:

    def __init__(self, model_name: str="gemini-2.5-flash"):
        try:
            api_key = os.environ.get("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("Api key is not set up")
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(model_name=model_name)
        except Exception as e:
            print(f"Error {e}")
            self.model = None