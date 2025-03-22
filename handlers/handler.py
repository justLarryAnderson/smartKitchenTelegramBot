from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

router = Router()

@router.message()
async def cmd_start(message: Message):
    await message.answer('Nice! You start the bot')
    