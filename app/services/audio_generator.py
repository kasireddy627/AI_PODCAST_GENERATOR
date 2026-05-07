import edge_tts
import asyncio


# async def text_to_speech(text: str, output_file: str):

#     communicate = edge_tts.Communicate(
#         text=text,
#         voice="en-US-GuyNeural"
#     )

#     await communicate.save(output_file)


import edge_tts


async def text_to_speech(text: str, output_file: str, voice: str):

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(output_file)