from groq import Groq
from app.utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def translate_script(script: str, language: str):

    try:

        prompt = f"""
        Translate the following podcast script into {language}.

        Requirements:
        - Keep conversational tone
        - Preserve meaning
        - Use natural spoken language
        - Return ONLY translated text

        Script:
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
            temperature=0.3,
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"ERROR: {str(e)}"