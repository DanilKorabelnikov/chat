from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
LINK = os.environ.get("LINK")  # vk.cc/aBAZSc
SLEEP = os.environ.get("SLEEP")
api = API(tokens=TOKEN)


async def post():
    group = [73482240, 112291806]
    while True:
        for item in group:
            if item == 73482240:
                await api.wall.post(owner_id=-item, message="Чат для продавцов имущества, аксессуаров и т.д.\n"
                                                                "Прoдaжa виpтyaльной вaлюты запрещена!\n"
                                                                f"{LINK}\n"
                                                                f"{LINK}")
            else:
                await api.wall.post(owner_id=-item, message="#arizona #arizonarp\n"
                                                            "Чат для продавцов имущества Arizona RP, аксессуаров и т.д.\n"
                                                            "Прoдaжa виpтyaльной вaлюты запрещена!\n"
                                                            f"{LINK}\n"
                                                            f"{LINK}")
            await asyncio.sleep(60)
        await asyncio.sleep(int(SLEEP))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(post())
