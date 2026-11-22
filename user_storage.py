import os
import json

from config import USERS_DIR

def user_path(user_id):
    return f'{USERS_DIR}{user_id}.json'

def save_user(user_id, user_file):
    os.makedirs(USERS_DIR, exist_ok=True)
    with open(user_path(user_id), 'w', encoding='utf-8') as file:
         json.dump(user_file, file, ensure_ascii=False, indent=4)

def load_user(user_id):
    with open(user_path(user_id), 'r', encoding='utf-8') as file:
        user_data = json.load(file)

    return user_data

def get_user(user_id):
    """Возвращает данные пользователя или None, если он новый.

    Словарь:
        'complexity'   — уровень: 'easy' / 'middle' / 'hard'
        'current_task' — id выданной задачи, на которую ещё нет ответа, или None
        'results'      — словарь {id задачи: True/False} — итог последней проверки
    """
    if os.path.exists(user_path(user_id)):
        return load_user(user_id)
    else:
        return None

def save_complexity(user_id, complexity):
    """Записывает выбранный уровень в файл пользователя. Создаёт файл, если пользователь новый"""
    if os.path.exists(user_path(user_id)):
        user_file = load_user(user_id)
        user_file['complexity'] = complexity
    else:
        user_file = {
            'complexity': complexity, 
            'current_task': None, 
            'results': {}
            }
        
    save_user(user_id, user_file)

def begin_task(user_id, task_id):
    """Записывает выданную задачу в файл пользователя"""
    user_file = load_user(user_id)
    user_file['current_task'] = task_id

    save_user(user_id, user_file)


def checked_task(user_id, task_id, result: bool):
    """Записывает результат проверки в results.
    True — решено: current_task очищается (None).
    False — решено неверно: current_task остаётся, можно прислать ещё раз.
    """
    user_file = load_user(user_id)
    user_file['results'][task_id] = result
    if result:
        user_file['current_task'] = None

    save_user(user_id, user_file)

def drop_task(user_id, task_id):
    """Пользователь снял задачу: results[task_id] = False, current_task = None."""
    user_file = load_user(user_id)
    user_file['results'][task_id] = False
    user_file['current_task'] = None

    save_user(user_id, user_file)
