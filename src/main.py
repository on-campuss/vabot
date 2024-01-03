import asyncio


from vabot.config import BaseConfig as cfg
from vabot.bot import bot


def run():
    asyncio.run(bot.polling(restart_on_change=True))

if __name__ == "__main__":
    run()