from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
LINK = os.environ.get("LINK")  # vk.cc/aBAZSc
SLEEP = os.environ.get("SLEEP")
LIST = [-73482240, -42590964, -112291806]
api = API(tokens=TOKEN)


async def post():
    while True:
        for i in LIST:
            if i != -73482240:
                await api.wall.post(owner_id=i, message="#arizonarp\n"
                                                        "Чат для продавцов имущества Arizona RP, аксессуаров и т.д.\n"
                                                        "Продажа виртуальной валюты запрещена!"
                                                        f"{LINK}\n"
                                                        f"{LINK}")
            else:
                await api.wall.post(owner_id=i, message="Чат для продавцов имущества, аксессуаров и т.д.\n"
                                                        "Продажа виртуальной валюты запрещена!"
                                                        f"{LINK}\n"
                                                        f"{LINK}")
            await asyncio.sleep(60)
        await asyncio.sleep(int(SLEEP))


if __name__ == '__main__':
    asyncio.run(post())
