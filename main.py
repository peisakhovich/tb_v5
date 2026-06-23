from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

BOT_TOKEN = os.getenv("PNM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


@app.get("/")
async def root():
    return {"status": "running"}


@app.get("/status")
async def status():
    return {
        "status": "ok",
        "bot_token_exists": BOT_TOKEN is not None
    }


@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()

    print("UPDATE:", update)

    if "channel_post" in update:
        post = update["channel_post"]

        chat_id = post["chat"]["id"]
        message_id = post["message_id"]

        text = f"message id:{message_id} - processed"

        requests.post(
            f"{BASE_URL}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": text
            }
        )

    return {"ok": True}