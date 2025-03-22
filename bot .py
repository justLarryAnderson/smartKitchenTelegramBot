import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from handlers.handler import router
load_dotenv(find_dotenv())

async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)#maybe can add allowed updates in futer
    
if __name__ == '__main__':
    asyncio.run(main())