from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
LINK = os.environ.get("LINK")  # vk.cc/aBAZSc
SLEEP = os.environ.get("SLEEP")
OWNER_ID = os.environ.get("OWNER_ID")
api = API(tokens=TOKEN)


async def post():
    while True:
        await api.wall.post(owner_id=OWNER_ID, message="Чат для продавцов имущества, аксессуаров и т.д.\n"
                                                "Продажа виртуальной валюты запрещена!"
                                                f"{LINK}\n"
                                                f"{LINK}")
        await asyncio.sleep(int(SLEEP))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(post())
