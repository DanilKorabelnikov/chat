from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
LINK = os.environ.get("LINK")  # vk.cc/aBAZSc
SLEEP = os.environ.get("SLEEP")
api = API(tokens="1d83f56b0ea6d7127e11c9ee01f1024cec0ac720cda5b20bd8444368b747f9d0c268a1a40183d054b244c")


async def post():
    group = [73482240, 112291806]
    while True:
        for item in group:
            if item == 73482240:
                await api.wall.post(owner_id=-item, message="Чат для продавцов имущества, аксессуаров и т.д.\n"
                                                                "Прoдaжa виpтyaльной вaлюты запрещена!\n"
                                                                "{LINK}\n"
                                                                "{LINK}")
            else:
                await api.wall.post(owner_id=-item, message="#arizona #arizonarp\n"
                                                            "Чат для продавцов имущества Arizona RP, аксессуаров и т.д.\n"
                                                            "Прoдaжa виpтyaльной вaлюты запрещена!\n"
                                                            "{LINK}\n"
                                                            "{LINK}")
            await asyncio.sleep(60)
        await asyncio.sleep(int(SLEEP))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(post())
