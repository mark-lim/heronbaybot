from telegram.ext import Updater
import time
import logging
from telegram import Update
from telegram.ext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler

#Import Updater and Dispatcher classs to fetch new updates from telegramp
updater = Updater(token = "2001966813:AAE2fZOT96v6vseK7-zL1aHKp5_p0MiVP5A", use_context = True)
dispatcher = updater.dispatcher

#Create log to check back for errors
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %m(message)s', 
                    level = logging.INFO)
logger = logging.getLogger(__name__)
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '2001966813:AAE2fZOT96v6vseK7-zL1aHKp5_p0MiVP5A'

#Create states 
FIRST, SECOND = 1,2
#Start function
def start(update, context):
    #Record in log that user has started convo
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    #Building inline keyboard with multiple rows
    keyboard = [
        [InlineKeyboardButton("Gym", callback_data="1"),
         InlineKeyboardButton("Tennis Courts", callback_data="2")],
         [InlineKeyboardButton("BBQ Pits", callback_data='3'),
         InlineKeyboardButton("Exit", callback_data="4")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    #Send messages with start
    update.message.reply_text("Welcome to the Heron Bay Facilities Booking Bot!")
    time.sleep(0.5)
    update.message.reply_text("How may I help you today?")
    time.sleep(0.5)
    update.message.reply_text(
        "Select one of the following: ",
        reply_markup = reply_markup
    )

def help(update, context):
    update.message.reply_text("For any enquiries contact the facilities manager!")

def error(update, context):
    #Log errors that are caused by updates
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TOKEN, use_context = True)
    
    #Allow dispatcher to register handlers
    dp = updater.dispatcher

    #Indicate what happens if I input different commands into Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    #Start bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)

    updater.bot.setWebhook('https://whispering-wildwood-52220.herokuapp.com/' + TOKEN)

if __name__ == "__main__":
    main()