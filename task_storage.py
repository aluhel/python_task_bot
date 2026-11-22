import json

from config import TASKS_FILE

def load_tasks():
    with open(TASKS_FILE, 'r', encoding='utf-8') as file:
        all_tasks = json.load(file)

    return all_tasks

def get_task_by_level(level, solved_ids):
    """задача уровня, которой нет в решённых, или None"""
    all_tasks = load_tasks()
    for item in all_tasks:
        item_id = item['id']
        item_level = item['level']
        if item_level == level and item_id not in solved_ids:
            return item
        
    return None

def get_task(task_id):
    """задача по id или None"""
    all_tasks = load_tasks()

    for item in all_tasks:
        item_id = item['id']
        if item_id == task_id:
            return item
        
    return None
