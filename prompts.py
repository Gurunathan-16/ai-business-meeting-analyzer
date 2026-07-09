PROMPT = """
You are an expert Business Analyst.

Analyze the following meeting transcript.

Return ONLY valid JSON.

{
  "summary": "",
  "decisions": [],
  "action_items": [
    {
      "owner": "",
      "task": "",
      "deadline": ""
    }
  ],
  "blockers": [],
  "risks": [],
  "open_questions": [],
  "next_steps": [],
  "participant_analysis": {
    "most_active": "",
    "least_active": "",
    "overall": ""
  },
  "project_status": ""
}

Meeting Transcript:

{transcript}
"""