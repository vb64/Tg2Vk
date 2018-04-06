from telebot import TeleBot
import vk
import settings


def is_from_master(message):
    return message.from_user.username == bot.master_username


class Bot(TeleBot):

    def __init__(
      self, bot_token, master_username, app_id, vk_login, vk_pass
    ):  # pylint: disable=too-many-arguments
        TeleBot.__init__(self, bot_token)

        self.__id = None
        self.__name = None
        self.master_username = master_username

        session = vk.AuthSession(
          app_id=app_id,
          user_login=vk_login,
          user_password=vk_pass,
          scope="wall, messages"
        )
        self.vk_api = vk.API(session, v='5.35')

    def tele_id(self):
        if self.__id is None:
            self.__set_info()

        return self.__id

    def username(self):
        if self.__name is None:
            self.__set_info()

        return self.__name

    def __set_info(self):
        me_info = self.get_me()
        self.__id = me_info.id
        self.__name = me_info.username

    @staticmethod
    def set_log_level(level):
        from telebot import logger as tg_logger
        from vk import logger as vk_logger
        tg_logger.setLevel(level)
        vk_logger.setLevel(level)


bot = Bot(  # pylint: disable=invalid-name
  settings.BOT_TOKEN,
  settings.USERNAME,
  settings.VK_APP_ID,
  settings.VK_LOGIN,
  settings.VK_PASS
)

from .command import start  # noqa: F401
from . import content  # noqa: F401


@bot.message_handler(func=lambda message: True)
def default_answer(message):
    reply = ''.join((
      _("My master is @{}").format(bot.master_username),
      ' ',
      _("I execute commands only from my master."),
    ))

    return bot.reply_to(message, reply)
