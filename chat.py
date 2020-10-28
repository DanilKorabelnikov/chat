from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")
LINK = os.environ.get("LINK")  # vk.cc/aBAZSc
SLEEP = os.environ.get("SLEEP")
api = API(tokens=TOKEN)


async def post():
    while True:
        await api.wall.post(owner_id=OWNER_ID, message="Чат для продавцов имущества, аксесуаров и т.д.\n"
                                                       "Продажа виpтyaльнoй вaлюты запрещена!"
                                                       f"{LINK}\n"
                                                       f"{LINK}")
        await asyncio.sleep(int(SLEEP))


if __name__ == '__main__':
    asyncio.run(post())
