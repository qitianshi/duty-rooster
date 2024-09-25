"""Entry point for Duty Rooster."""

# Copyright 2024 Qi Tianshi. All rights reserved.


import os
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


# Logging configs.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Onboarding for new users."""

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Cock-a-doodle-doo! I'm Duty Rooster, the duty roster that isn't"
            + " bird-brained. Something's hatching soon, so watch this coop!"
    )


if __name__ == "__main__":

    app = ApplicationBuilder().token(os.getenv("PROD_BOT_TOKEN")).build()

    # Adds handlers.
    app.add_handler(CommandHandler('start', start))

    # Uses the appropriate run mode depending on the environment.
    if os.getenv("ENV") == "production":
        app.run_webhook(
            listen="0.0.0.0",
            port=int(os.getenv("PORT", "8080")),
            webhook_url=os.getenv("GCP_APP_ENDPOINT"),
        )

    else:
        app.run_polling()
