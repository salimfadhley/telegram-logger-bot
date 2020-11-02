#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import yaml
import logging
import os
from telegram.update import Update

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters

log = logging.getLogger(__name__)

logger = logging.getLogger(__name__)

token = os.environ["TELEGRAM_TOKEN"]


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update:Update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update:Update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def foo_command(update:Update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Foo!')


def echo(update:Update, context):
    log.warning(yaml.dump(update.to_dict()))
    update.message.reply_text(update.message.text)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(CommandHandler("foo", foo_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

