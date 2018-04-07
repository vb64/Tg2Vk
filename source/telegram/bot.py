""" Bot class definition, instancing a bot and register content handlers."""
from telebot import TeleBot
import vk
import settings


def is_from_master(message):
    """ Is a message from bot owner?"""
    return message.from_user.username == bot.master_username


class Bot(TeleBot):
    """ Class for Telegram bot, based on pyTelegramBotAPI """
    def __init__(
      self, bot_token, master_username, vk_app_id, vk_login, vk_pass
    ):  # pylint: disable=too-many-arguments
        TeleBot.__init__(self, bot_token)

        self.__id = None
        self.__name = None
        self.master_username = master_username

        session = vk.AuthSession(
          app_id=vk_app_id,
          user_login=vk_login,
          user_password=vk_pass,
          scope="wall, messages"
        )
        self.vk_api = vk.API(session, v='5.35')

    def tele_id(self):
        """ Return saved bot ID. The first call read it from API. """
        if self.__id is None:
            self.__set_info()

        return self.__id

    def username(self):
        """ Return saved bot username. The first call read it from API. """
        if self.__name is None:
            self.__set_info()

        return self.__name

    def __set_info(self):
        """ Read bot data from API and save it in an instance. """
        me_info = self.get_me()
        self.__id = me_info.id
        self.__name = me_info.username

    @staticmethod
    def set_log_level(level):
        """ Set a level of logging for used libraries. """
        from telebot import logger as tg_logger
        from vk import logger as vk_logger
        tg_logger.setLevel(level)
        vk_logger.setLevel(level)


# instancing bot for defining content handlers
bot = Bot(  # pylint: disable=invalid-name
  settings.BOT_TOKEN,
  settings.USERNAME,
  settings.VK_APP_ID,
  settings.VK_LOGIN,
  settings.VK_PASS
)

# define content handlers
# these instructions cannot be placed at the top of the module by the cyclic import reason
from .command import start  # noqa: F401 pylint: disable=wrong-import-position,unused-import
from . import content  # noqa: F401 pylint: disable=wrong-import-position,unused-import


@bot.message_handler(func=lambda message: True)
def default_answer(message):
    """ This function processed all messages,
    that not processed by content handlers, that defined above."""
    reply = ''.join((
      _("My master is @{}").format(bot.master_username),
      ' ',
      _("I execute commands only from my master."),
    ))

    return bot.reply_to(message, reply)
