async def on_button_level(callback: CallbackQuery):
    """Нажата кнопка уровня.
    - user_storage.save_complexity(user_id, уровень) — всегда.
    - user_storage.get_user(user_id): есть current_task → напомнить о задаче,
      кнопки «Доделать» / «Снять»; нет → предложить /begin.
    """

async def on_button_unfinished(callback: CallbackQuery):
    """Ответ на «Доделать» / «Снять».
    - «Доделать» → показать условие (task_storage.get_task(current_task)).
    - «Снять» → user_storage.drop_task(user_id, current_task), предложить /begin.
    """