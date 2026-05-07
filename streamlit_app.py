import streamlit as st
import asyncio
import os

from app.services.article_extractor import extract_article
from app.services.script_generator import generate_podcast_script
from app.services.translator import translate_script
from app.services.content_validator import validate_script
from app.services.audio_generator import text_to_speech

st.set_page_config(
    page_title="AI Podcast Generator",
    layout="wide"
)

st.title("Multilingual AI Podcast Generator")

st.write(
    "Generate AI-powered multilingual podcast audio from news articles."
)

# ---------------------------------------------------
# LANGUAGE OPTIONS
# ---------------------------------------------------

voice_options = {
    "English": "en-US-GuyNeural",
    "Telugu": "te-IN-MohanNeural",
    "Hindi": "hi-IN-MadhurNeural",
    "Tamil": "ta-IN-ValluvarNeural"
}

# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------

article_url = st.text_input(
    "Enter Article URL"
)

selected_language = st.selectbox(
    "Select Podcast Language",
    list(voice_options.keys())
)

generate_btn = st.button("Generate Podcast")

# ---------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------

if generate_btn:

    if not article_url:

        st.error("Please enter article URL")

    else:

        # ---------------------------------------------------
        # ARTICLE EXTRACTION
        # ---------------------------------------------------

        with st.spinner("Extracting article..."):

            extract_data = extract_article(article_url)

        if (
            "text" not in extract_data
            or not extract_data["text"]
        ):

            st.error("Article extraction failed")

            st.json(extract_data)

            st.stop()

        article_text = extract_data["text"]

        st.subheader("Extracted Article")

        st.write(article_text[:1500] + "...")

        # ---------------------------------------------------
        # SCRIPT GENERATION
        # ---------------------------------------------------

        with st.spinner("Generating podcast script..."):

            script = generate_podcast_script(article_text)

        if not script:

            st.error("Script generation failed")

            st.stop()

        st.subheader("Generated Script")

        st.write(script)

        # ---------------------------------------------------
        # TRANSLATION
        # ---------------------------------------------------

        final_script = script

        if selected_language != "English":

            with st.spinner("Translating script..."):

                final_script = translate_script(
                    script,
                    selected_language
                )

            st.subheader("Translated Script")

            st.write(final_script)

        # ---------------------------------------------------
        # VALIDATION
        # ---------------------------------------------------

        with st.spinner("Validating content..."):

            validation_result = validate_script(final_script)

        st.subheader("Validation Result")

        st.json(validation_result)

        # ---------------------------------------------------
        # AUDIO GENERATION
        # ---------------------------------------------------

        voice = voice_options[selected_language]

        output_path = "podcast.mp3"

        with st.spinner("Generating podcast audio..."):

            asyncio.run(
                text_to_speech(
                    final_script,
                    output_path,
                    voice
                )
            )

        # ---------------------------------------------------
        # AUDIO PLAYBACK
        # ---------------------------------------------------

        if os.path.exists(output_path):

            st.subheader("Podcast Audio")

            with open(output_path, "rb") as audio_file:

                audio_bytes = audio_file.read()

            st.audio(audio_bytes, format="audio/mp3")

            st.download_button(
                label="Download Podcast",
                data=audio_bytes,
                file_name="podcast.mp3",
                mime="audio/mp3"
            )

        else:

            st.error("Audio generation failed")