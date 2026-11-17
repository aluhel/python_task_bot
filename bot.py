import asyncio
import os
import logging

from config import LEVELS

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = logging.getLogger(__name__)
load_dotenv()
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher()

async def start(message: Message):
    """Бот здоровается и объясняет, что умеет"""
    pass

async def assistance(message: Message):
    """Все команды"""
    pass

async def complexity(message: Message):
    """Выбираем(при первом запуске)/меняем уровень сложности задач"""
    pass

async def begin(message: Message):
    """Начать решать, бот отправяет тебе задачу"""
    pass

async def decision_making_approach(message: Message):
    """Приём решения (любой текст)"""
    pass
