from fastapi import FastAPI, Request
import os
import httpx
import logging

app = FastAPI()

# ---------------------------
# Logging (Azure-friendly)
# ---------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ---------------------------
# Telegram config
# ---------------------------
def get_bot_token() -> str:
    token = os.getenv("PNM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Environment variable PNM_BOT_TOKEN is not set")
    return token


def get_base_url() -> str:
    return f"https://api.telegram.org/bot{get_bot_token()}"


# ---------------------------
# Health checks
# ---------------------------
@app.get("/")
async def root():
    return {"status": "running"}


@app.get("/status")
async def status():
    return {
        "status": "ok",
        "bot_token_exists": bool(os.getenv("PNM_BOT_TOKEN"))
    }


# ---------------------------
# Webhook
# ---------------------------
@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()

    logger.info("UPDATE: %s", update)

    # Handle channel posts only (можно расширить позже)
    if "channel_post" in update:
        post = update["channel_post"]

        chat_id = post["chat"]["id"]
        message_id = post["message_id"]

        text = f"message id:{message_id} - processed"

        base_url = get_base_url()

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                f"{base_url}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": text
                }
            )

        logger.info("Telegram response: %s", response.text)

    return {"ok": True}