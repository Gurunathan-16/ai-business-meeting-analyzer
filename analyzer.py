import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_meeting(transcript):

    prompt = PROMPT.format(transcript=transcript)

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown code fences if present
    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)