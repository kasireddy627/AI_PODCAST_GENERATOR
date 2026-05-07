from groq import Groq
from app.utils.config import GROQ_API_KEY
import json

client = Groq(api_key=GROQ_API_KEY)


def validate_script(script: str):

    try:

        json_format = """
        {
            "safe": true,
            "quality_score": 8,
            "issues": [
                "issue 1"
            ]
        }
        """

        prompt = f"""
        You are an AI content reviewer.

        Analyze this podcast script.

        Check for:
        - toxic language
        - unsafe content
        - suspicious claims
        - excessive repetition
        - robotic narration
        - grammar problems

        Return ONLY valid JSON:

        {json_format}

        SCRIPT:
        {script}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=300
        )

        result = response.choices[0].message.content.strip()

        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()
        print("RAW RESPONSE : ")
        try:
            return json.loads(result)

        except Exception as parse_error:

            return {
                "error": "JSON parsing failed",
                "raw_response": result,
                "parse_error": str(parse_error)
            }

    except Exception as e:
            return {
                    "error": str(e)
                }