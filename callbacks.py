from aiogram import Router, F
from aiogram.types import CallbackQuery

from config import ALLOWED_USERS, LEVELS
from user_storage import save_complexity

router = Router()
router.callback_query.filter(F.from_user.id.in_(ALLOWED_USERS))

@router.callback_query(F.data.startswith("level:"))
async def on_button_level(callback: CallbackQuery):
  """Нажата кнопка уровня.
  - user_storage.save_complexity(user_id, уровень) — всегда.
  - user_storage.get_user(user_id): есть current_task → напомнить о задаче,
    кнопки «Доделать» / «Снять»; нет → предложить /begin.
  """
  actual_level = callback.data.split(':')[1]
  save_complexity(callback.from_user.id, actual_level)
  await callback.answer()
  await callback.message.answer('Уровень сохранён. Возьми задачу: /begin')

async def on_button_unfinished(callback: CallbackQuery):
  """Ответ на «Доделать» / «Снять».
  - «Доделать» → показать условие (task_storage.get_task(current_task)).
  - «Снять» → user_storage.drop_task(user_id, current_task), предложить /begin.
  """