##booglet, t stands for telegram

from telegram.ext import Updater
from telegram.ext import CommandHandler

with open('.env', 'r') as file:
    lines = file.readlines()
    BOT_TOKEN = lines[1]


updater = Updater(token = BOT_TOKEN, use_context = True)

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello")


updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
print('Bot started')


