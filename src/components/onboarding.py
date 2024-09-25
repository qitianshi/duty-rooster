"""Onboarding for new users.

Duty Rooster introduces itself and asks for initial signup info. Triggered by
the `/start` command.
"""

# Copyright 2024 Qi Tianshi. All rights reserved.


from telegram import Update
from telegram.ext import ContextTypes


async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Update handler callback for `onboarding`."""

    # TODO: Placeholder message.
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Cock-a-doodle-doo! I'm Duty Rooster, the duty roster that isn't"
            + " bird-brained. Something's hatching soon, so watch this coop! 🐣"
    )
