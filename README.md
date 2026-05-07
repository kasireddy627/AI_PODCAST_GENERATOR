````markdown
# <span style="color:#2563eb;">Multilingual AI Podcast Generator</span>

An end-to-end Generative AI platform that converts online news articles into multilingual podcast-style audio using LLMs, translation pipelines, AI validation, and neural text-to-speech.

---

## Problem Statement

Millions of articles, blogs, and news reports are published daily, but most users:

- do not have time to read long-form content
- prefer audio-based content consumption
- consume information while multitasking
- want content in regional/native languages

At the same time, manually converting articles into podcasts is expensive, time-consuming, and difficult to scale.

Additionally, AI-generated content introduces risks such as:
- hallucinations
- repetitive narration
- unsafe content
- poor-quality outputs

This project solves these problems by automatically generating validated multilingual podcast audio from article URLs.

---

## Why This Project?

This project was built to explore practical real-world GenAI orchestration instead of building another simple chatbot demo.

The goal was to design a complete AI pipeline involving:
- content extraction
- LLM-based generation
- translation workflows
- AI validation systems
- neural voice synthesis
- deployment pipelines

The project focuses on building an actual usable AI product workflow.

---

## Core Features

- Article URL extraction
- AI podcast script generation
- Multilingual translation
- AI content validation
- Neural text-to-speech generation
- Downloadable podcast audio
- Streamlit UI
- Dockerized deployment

---

## Supported Languages

- English
- Telugu
- Hindi
- Tamil

---

## Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| LLM Provider | Groq API |
| LLM Model | Llama 3.3 70B |
| Article Extraction | newspaper3k |
| Translation | Groq LLM |
| Text-to-Speech | Edge-TTS |
| Deployment | Docker + Render |
| Language | Python |

---

## System Workflow

```text
Article URL
     ↓
Article Extraction
     ↓
Podcast Script Generation
     ↓
Translation Layer
     ↓
AI Validation
     ↓
Neural Text-to-Speech
     ↓
Podcast Audio
````

---

## How We Built It

### 1. Article Extraction

The system accepts a news/article URL and extracts:

* title
* article text
* summary

using `newspaper3k`.

---

### 2. AI Podcast Script Generation

The extracted content is sent to Groq LLM APIs where the model generates:

* conversational narration
* podcast-style summaries
* human-readable storytelling format

Prompt engineering was used to reduce:

* robotic narration
* placeholders
* repetitive responses

---

### 3. Translation Pipeline

Generated scripts are translated into:

* Telugu
* Hindi
* Tamil

using LLM-based translation while preserving conversational tone.

---

### 4. AI Validation Layer

A second AI validation layer checks generated scripts for:

* unsafe content
* suspicious claims
* repetition
* narration quality
* grammar issues

This introduces a basic AI moderation workflow before audio generation.

---

### 5. Neural Audio Generation

Validated scripts are converted into realistic multilingual audio using:

* Edge-TTS
* neural voices
* dynamic language-based voice selection

---

### 6. Streamlit Interface

A lightweight Streamlit frontend was built for:

* article submission
* language selection
* audio playback
* podcast download

---

### 7. Dockerized Deployment

The entire application was containerized using Docker and deployed publicly using Render.

---

## Key Learning Outcomes

* End-to-end GenAI orchestration
* Prompt engineering
* AI validation systems
* Multilingual AI workflows
* Neural text-to-speech integration
* Dockerization & deployment
* Streamlit + FastAPI integration

---

## Current Limitations

* Some regional websites fail extraction
* Validation is heuristic-based
* No persistent database yet
* Single-user MVP architecture

---

## Future Improvements

* RSS feed automation
* Daily AI news podcasts
* Background music integration
* Multiple narrator voices
* Cloud audio storage
* Better factual verification
* Workflow automation using n8n

---

## Author

Kambalapalle Kasi Reddy

```
```
