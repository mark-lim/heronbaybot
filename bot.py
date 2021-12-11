from telegram.ext import Updater

import logging

from telegram import Update
from telegram.ext import CallbackContext

from telegram.ext import CommandHandler

#Import Updater and Dispatcher classs to fetch new updates from telegramp
updater = Updater(token = "2001966813:AAE2fZOT96v6vseK7-zL1aHKp5_p0MiVP5A", use_context = True)
dispatcher = updater.dispatcher

#Create log to check back for errors
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %m(message)s', 
                    level = logging.INFO)

#Start function
startstr = "Welcome to the Heron Bay Facilities Booking Bot! How may I help you today?"
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id = update.effective_chat.id,
                             text = startstr)

#Allow the start function to be called everytime the bot receives a message containing "/start"
start_handler = Commandhandler('start', start)
dispatcher.add_handler(start_handler)