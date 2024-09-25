"""Entry point for Duty Rooster.

Configures application, webhooks, event handlers, logging, etc.
"""

# Copyright 2024 Qi Tianshi. All rights reserved.


import logging
from secrets import token_urlsafe

from telegram.ext import ApplicationBuilder, CommandHandler

import components
from utils import env


# Logging configs.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Runs the app.
if __name__ == "__main__":

    # Uses the test bot in dev, and the production bot in prod.
    app = ApplicationBuilder().token(
        env.PROD_BOT_TOKEN
        if env.ENV == env.Environment.PROD
        else env.TEST_BOT_TOKEN
    ).build()

    # Adds handlers.
    app.add_handler(CommandHandler('start', components.onboarding.callback))

    # Uses the appropriate run mode depending on the environment. Generates a
    # short-lived token for verifying the authenticity of webhook requests.
    if env.ENV == env.Environment.PROD:
        app.run_webhook(
            listen="0.0.0.0",
            port=env.PORT,
            webhook_url=env.GCP_APP_ENDPOINT,
            secret_token=token_urlsafe(32),
        )

    else:
        app.run_polling()
