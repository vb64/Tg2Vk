from telegram.bot import bot, is_from_master


def private_with_master(message):
    return is_from_master(message) and message.chat.type == 'private'


@bot.message_handler(func=private_with_master)
def start(message):
    """ function responds to any content in private chat with bot owner
    """
    bot.vk_api.wall.post(message=message.text)
    reply = _("Message was sent to your wall in VK.")

    return bot.reply_to(message, reply)
