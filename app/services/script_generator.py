from groq import Groq
from app.utils.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_podcast_script(article_text: str):

    try:

        prompt = f"""
            You are an experienced podcast narrator.

            Convert the news article into a realistic spoken podcast script.

            Requirements:
            - Sound natural and human
            - Avoid generic AI phrases
            - No stage directions
            - No music references
            - No placeholders
            - No repetitive transitions
            - Keep it concise
            - Use simple spoken English
            - Make it sound like a real short news briefing

            Article:
            {article_text}
            """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        script = response.choices[0].message.content

        script = script.replace("*", "")
        script = script.replace("[Intro music plays]", "")
        script = script.replace("[Outro music continues to play]", "")

        return script.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"