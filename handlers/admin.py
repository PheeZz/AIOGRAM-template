from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import MessageNotModified


from data import config
import keyboards as kb
from middlewares import rate_limit


@rate_limit(limit=5)
async def cmd_info(message: types.Message):
    await message.reply(message)
