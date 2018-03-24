# Tg2Vk
Your personal Telegram bot for messaging to VK social network.

Install source (requires git, make, gettext and Python):

```
$ git clone https://github.com/vb64/Tg2Vk.git
$ cd Tg2Vk
$ make setup
```

There are some [additional notes for setup on Windows](WINDOWS.md).

Edit file `source/settings.py` for your credentials for Telegram and VK. Then go to Tg2Vk project root catalog and run

```
make run
```

You can communicate with your Telegram bot, while program running. To finish work press Ctrl+C. Your Telegram bot becomes unavailable.
