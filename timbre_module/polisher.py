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
    
    def translator_prompt(self, text: str, language: str): 
        return f"""
You are an expert, professional, and precise translator.

Strictly adhere to the following instructions:
1.  **Task:** Translate the text provided below into **{language}**.
2.  **Accuracy:** The translation must be as accurate, idiomatic, and contextually appropriate as possible.
3.  **Formatting:** Preserve all original line breaks, paragraph structure, and markdown/HTML elements exactly in the translated text.
4.  **Output Rule:** Provide **only** the translated text. **DO NOT** include any surrounding conversation, explanation, preamble, or any other text.
5.  **Target Language:** The entire output must be in **{language}**.

Text to Translate:
---
{text}
---
""" 
    def enhancer_prompt(self, text: str, style: str):
        style = style.strip()
        if style:
            instruction =f"Refine the text to conform to a **{style}** style and tone. Ensure the phrasing is accurate, idiomatic, and highly suitable for the requested style."
        else:
            instruction ="Correct all grammar and spelling mistakes. Improve the phrasing to be **clear, natural, and highly accurate** without changing the original tone significantly."
        return f"""
You are an expert editor and style guide. Your task is to polish and refine the provided text.

Strictly adhere to the following instructions:
1.  **Primary Task:** {instruction}
2.  **Correction:** Scrutinize and correct all errors in grammar, spelling, punctuation, and syntax.
3.  **Tone & Audience:** Ensure the refined text is appropriate for its context and maintains coherence.
4.  **Output Rule:** Provide **only** the polished and corrected text. **DO NOT** include any conversation, explanation, or preamble.
5.  **Formatting:** Preserve all original line breaks and paragraph structure.

Text to Enhance:
---
{text}
---
"""      