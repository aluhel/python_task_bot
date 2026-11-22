import asyncio
import logging


from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from config import TELEGRAM_BOT_TOKEN, ALLOWED_USERS
from user_storage import get_user
from task_storage import get_task
from keyboards import levels_keyboard
import callbacks

logger = logging.getLogger(__name__)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
dp.message.filter(F.from_user.id.in_(ALLOWED_USERS))
dp.include_router(callbacks.router)

@dp.message(CommandStart())
async def start(message: Message):
  """Бот здоровается и объясняет, что умеет.

  Вызывает: user_storage.get_user(user_id).
  - Новый пользователь (None) → предложить выбрать уровень (/complexity).
  - Есть current_task → напомнить о незаконченной задаче,
    условие взять через task_storage.get_task(current_task).
  - Нет current_task → предложить взять задачу (/begin).
  """
  logger.info(f'{message.from_user.first_name}: {message.text}')
  user_id = message.from_user.id
  check_user = get_user(user_id)
  if not check_user:
    await message.answer(
      f'Привет! Я бот-тренажёр задач на Python. Выбери уровень:', 
      reply_markup=levels_keyboard()
      )
  elif check_user['current_task']:
    check_task = get_task(check_user['current_task'])
    await message.answer(
    f'С возвращением! У тебя есть незаконченная задача:\n\n{check_task['text']}\n\nПришли решение или возьми другую: /begin'
    )
  else:
    await message.answer(
    f'С возвращением! Возьми задачу: /begin'
    )


async def assistance(message: Message):
  """Список команд с кратким описанием: /start, /help, /complexity, /begin.
  Функций из других модулей не вызывает — только текст.
  """
  pass

async def complexity(message: Message):
  """Показывает inline-кнопки уровней из config.LEVELS
  (надпись — 'Простой', в callback_data — 'easy').
  Нажатие обрабатывает callbacks.py.
  """
  pass

async def begin(message: Message):
  """Выдаёт задачу по уровню пользователя.
  - user_storage.get_user(user_id) → None: «Сначала выбери уровень», /complexity.
  - Есть current_task → напомнить, кнопки «Доделать» / «Снять»
    (callbacks.on_button_unfinished).
  - Иначе task_storage.get_task_by_level(complexity, solved_ids),
    solved_ids — id из results со значением True:
      - None → «Задачи этого уровня закончились», предложить /complexity;
      - задача → user_storage.begin_task(user_id, id задачи), прислать условие.
  """
  pass

async def decision_making_approach(message: Message):
  """Пользователь прислал решение текстом.
  - user_storage.get_user(user_id) → None: «Сначала выбери уровень», /complexity.
  - Нет current_task → «Нет задачи в работе», предложить /begin.
  - Иначе task_storage.get_task(current_task) → checker.check(message.text, task)
    → (ok, text):
      - ok → user_storage.checked_task(user_id, id, True), ответ text, предложить /begin;
      - не ok → user_storage.checked_task(user_id, id, False), ответ text,
        «Исправь и пришли ещё раз».
  """
  pass

async def main():
  logging.basicConfig(level=logging.INFO)
  logger.info("Бот запущен")
  await dp.start_polling(bot)

if __name__ == '__main__':
  asyncio.run(main())
