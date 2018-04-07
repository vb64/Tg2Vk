""" Handler for /start command. """
from telegram.bot import bot, is_from_master


@bot.message_handler(func=is_from_master, commands=['start'])
def start(message):
    """ Function responds to /start command, that send from the bot owner. """
    if message.chat.type == 'private':
        reply = _("Type a message and I will send it to your VK wall.")
    else:
        reply = ''.join((
          _("My master, let's go to private chat @{}").format(bot.username()),
          ' ',
          _("Those present here do not need to listen to our talk."),
        ))

    return bot.reply_to(message, reply)
