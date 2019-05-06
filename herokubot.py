import logging
import os
import subprocess

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Original code
# def start(bot, update):
#     update.effective_message.reply_text("Hi!")
# def echo(bot, update):
#     update.effective_message.reply_text(update.effective_message.text)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I have a very good brain")

def randomtweet(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Testing random tweet')

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text.upper())

def number(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="This is a number.")

def test(bot, update):
    try:
        #os.system('subfile.py')
        subfile_output = subprocess.run('subfile.py', check=True, capture_output=True, stdout=PIPE).stdout
        bot.send_message(chat_id=update.message.chat_id, text=subfile_output)
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Exception")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "666218025:AAFOzCAxqnxwZcZsoq4P0kjPZrB-5UehMWA"
    NAME = "stablegenius"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))       # Handles /commands
    dp.add_handler(CommandHandler('randomtweet', randomtweet))
    dp.add_handler(MessageHandler(Filters.text, test)) # Handles all text
    # dp.add_handler(MessageHandler(Filters.regex(r'\S'), echo))      # Handles messages which are characters
    # dp.add_handler(MessageHandler(Filters.regex(r'\d*'), number))   # Filter message
    dp.add_error_handler(error)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
