import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Podcast Generator",
    layout="wide"
)

st.title("Multilingual AI Podcast Generator")

st.write("Generate AI-powered podcast audio from news articles.")

# -----------------------------------
# LANGUAGE OPTIONS
# -----------------------------------

voice_options = {
    "English": "en-US-GuyNeural",
    "Telugu": "te-IN-MohanNeural",
    "Hindi": "hi-IN-MadhurNeural",
    "Tamil": "ta-IN-ValluvarNeural"
}

# -----------------------------------
# USER INPUTS
# -----------------------------------

article_url = st.text_input("Enter Article URL")

selected_language = st.selectbox(
    "Select Podcast Language",
    list(voice_options.keys())
)

generate_btn = st.button("Generate Podcast")

# -----------------------------------
# MAIN PIPELINE
# -----------------------------------

if generate_btn:

    if not article_url:

        st.error("Please enter article URL")

    else:

        # -----------------------------------
        # EXTRACT ARTICLE
        # -----------------------------------

        with st.spinner("Extracting article..."):

            extract_response = requests.post(
                f"{FASTAPI_URL}/extract-article",
                json={
                    "url": article_url
                }
            )

            extract_data = extract_response.json()

        if (
            "data" not in extract_data
            or "text" not in extract_data["data"]
        ):

            st.error("Article extraction failed")

            st.json(extract_data)

            st.stop()

        article_text = extract_data["data"]["text"]

        st.subheader("Extracted Article")

        st.write(article_text[:1500] + "...")

        # -----------------------------------
        # GENERATE SCRIPT
        # -----------------------------------

        with st.spinner("Generating podcast script..."):

            script_response = requests.post(
                f"{FASTAPI_URL}/generate-script",
                json={
                    "text": article_text
                }
            )

            script_data = script_response.json()

        if "script" not in script_data:

            st.error("Script generation failed")

            st.json(script_data)

            st.stop()

        script = script_data["script"]

        st.subheader("Generated Script")

        st.write(script)

        # -----------------------------------
        # TRANSLATE SCRIPT
        # -----------------------------------

        final_script = script

        if selected_language != "English":

            with st.spinner("Translating script..."):

                translation_response = requests.post(
                    f"{FASTAPI_URL}/translate-script",
                    json={
                        "script": script,
                        "language": selected_language
                    }
                )

                translation_data = translation_response.json()

            if "translated_script" not in translation_data:

                st.error("Translation failed")

                st.json(translation_data)

                st.stop()

            final_script = translation_data["translated_script"]

            st.subheader("Translated Script")

            st.write(final_script)

        # -----------------------------------
        # VALIDATE SCRIPT
        # -----------------------------------

        with st.spinner("Validating content..."):

            validation_response = requests.post(
                f"{FASTAPI_URL}/validate-script",
                json={
                    "script": final_script
                }
            )

            validation_data = validation_response.json()

        st.subheader("Validation Result")

        st.json(validation_data["validation"])

        # -----------------------------------
        # GENERATE AUDIO
        # -----------------------------------

        voice = voice_options[selected_language]

        with st.spinner("Generating podcast audio..."):

            audio_response = requests.post(
                f"{FASTAPI_URL}/generate-audio",
                json={
                    "script": final_script,
                    "voice": voice
                }
            )

        if audio_response.status_code == 200:

            st.subheader("Podcast Audio")

            audio_bytes = audio_response.content

            st.audio(audio_bytes, format="audio/mp3")

            st.download_button(
                label="Download Podcast",
                data=audio_bytes,
                file_name="podcast.mp3",
                mime="audio/mp3"
            )

        else:

            st.error("Audio generation failed")