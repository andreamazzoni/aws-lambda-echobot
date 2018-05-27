import config
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, Dispatcher


# command handler
def test(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="You typed /test command")


# simple echo handler
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def run(message):
    """Receive a message, handle it, and send a response"""

    bot = Bot(config.bot_token)
    dp = Dispatcher(bot, None, workers=0)

    # add your handlers here
    dp.add_handler(CommandHandler("test", test))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # decode update and try to process it
    update = Update.de_json(message, bot)
    dp.process_update(update)
