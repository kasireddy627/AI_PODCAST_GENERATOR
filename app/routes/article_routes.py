from fastapi import APIRouter
from app.models.article_model import ArticleRequest
from app.services.article_extractor import extract_article
from app.models.article_model import ScriptRequest
from app.services.script_generator import generate_podcast_script

from app.models.article_model import ValidationRequest
from app.services.content_validator import validate_script

from app.models.article_model import AudioRequest
from app.services.audio_generator import text_to_speech

from fastapi.responses import FileResponse

from app.models.article_model import TranslationRequest
from app.services.translator import translate_script


import asyncio

router = APIRouter()


@router.post("/extract-article")
def extract_article_route(request: ArticleRequest):
    data = extract_article(request.url)

    return {
        "success": True,
        "data": data
    }


@router.post("/generate-script")
def generate_script_route(request: ScriptRequest):

    script = generate_podcast_script(request.text)

    return {
        "success": True,
        "script": script
    }


@router.post("/validate-script")
def validate_script_route(request: ValidationRequest):

    result = validate_script(request.script)

    return {
        "success": True,
        "validation": result
    }

@router.post("/generate-audio")
async def generate_audio_route(request: AudioRequest):

    output_path = "outputs/podcast.mp3"

    await text_to_speech(
        request.script,
        output_path,
        request.voice
    )

    return FileResponse(
        output_path,
        media_type="audio/mpeg",
        filename="podcast.mp3"
    )
    return FileResponse(
        output_path,
        media_type="audio/mpeg",
        filename="podcast.mp3"
    )

@router.post("/translate-script")
def translate_script_route(request: TranslationRequest):

    translated = translate_script(
        request.script,
        request.language
    )

    return {
        "success": True,
        "translated_script": translated
    }