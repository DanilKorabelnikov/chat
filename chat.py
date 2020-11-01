from vkbottle.api import API
import asyncio
import os

TOKEN = os.environ.get("TOKEN")
SLEEP = os.environ.get("SLEEP")
USER_ID = os.environ.get("USER_ID")
TEXT = os.environ.get("TEXT")
OWNER_ID = os.environ.get("OWNER_ID")
api = API(tokens=TOKEN)


async def post():
    try:
        while True:
            await api.wall.post(owner_id=-int(OWNER_ID), message=f"{TEXT}")
            await asyncio.sleep(int(SLEEP))
    except:
        await api.messages.send(user_id=int(USER_ID), random_id=api.extension.random_id(), peer_id=int(USER_ID),
                                message="Произошла ошибка при создание поста!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(post())
