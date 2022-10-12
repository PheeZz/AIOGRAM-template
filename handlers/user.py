from loguru import logger


from aiogram import types
from aiogram.dispatcher import FSMContext

from middlewares import rate_limit
import keyboards as kb


@rate_limit(limit=5)
async def cmd_start(message: types.Message):
    await message.reply(f"Hello,{message.from_user.full_name or message.from_user.username}!")
