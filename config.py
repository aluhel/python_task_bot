import os
from dotenv import load_dotenv
load_dotenv()

TIMEOUT = 5
LEVELS = {'Простой': 'easy', 'Средний': 'middle', 'Сложный': 'hard'}
TASKS_FILE = 'tasks.json'
USERS_DIR = 'users/'
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
allowed_raw = os.getenv("ALLOWED_USERS")
if allowed_raw:
    ALLOWED_USERS = set(int(number) for number in allowed_raw.split(','))
else:
    raise ValueError('В .env нет ALLOWED_USERS')
    
