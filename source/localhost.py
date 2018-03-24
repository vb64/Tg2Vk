import os
import sys
import logging
import gettext
import settings


def main():
    params = [
      settings.BOT_TOKEN,
      settings.USERNAME,
      settings.VK_APP_ID,
      settings.VK_LOGIN,
      settings.VK_PASS,
    ]
    if not all(params):
        print "!!!!!\nPlease, set all parameters in settings.py\n!!!!!"
        return

    gettext.translation(
      'messages',
      os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locale'),
      languages=[settings.LANGUAGE]
    ).install()

    sys.path.insert(1, "libs")

    from telegram.bot import bot
    bot.set_log_level(logging.DEBUG)
    bot.polling()


if __name__ == "__main__":  # pragma: no cover
    main()
