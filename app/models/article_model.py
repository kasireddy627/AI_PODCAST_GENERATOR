from pydantic import BaseModel


class ArticleRequest(BaseModel):
    url: str


class ScriptRequest(BaseModel):
    text: str

class ValidationRequest(BaseModel):
    script: str

class AudioRequest(BaseModel):
    script: str
    voice: str

class TranslationRequest(BaseModel):
    script: str
    language: str