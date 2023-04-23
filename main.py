import asyncio
from text_generation import generate_text

async def main():
    chat = False
    prompt = "User: hi\nAssistant: Hello! How can I assist you today?\nUser: "
    printing = True

    generated_text = await generate_text(chat, prompt, printing,timeout=60)
    print(generated_text)

asyncio.run(main())
