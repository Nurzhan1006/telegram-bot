import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ChatAction
import os

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("8493632468:AAE9_RSWIpR5ojOSPg7A90xZNI0P2ZX6-Eg")  # токен из переменных окружения

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я твой бот 🤖")

@dp.message()
async def echo(message: types.Message):
    # Анимация "печатает..."
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await asyncio.sleep(2)
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
