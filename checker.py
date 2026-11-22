import subprocess
import sys
import json

from config import TIMEOUT

def check(user_decision, task):
    """Получает решение пользователя и проверяет правильность решения по тестам. Возвращает кортеж (bool, str): решено или нет, текст для пользователя"""
    function = task['function']
    all_args = [
        input_data['input'] for input_data in task['tests']
        ]
    expected = [
        correct_answers['expected'] for correct_answers in task['tests']
        ]
    errors = []
    try:
        result = subprocess.run(
            [sys.executable, '-c', 
            f'import json\n{user_decision}\nprint(json.dumps([{function}(*args) for args in {all_args}]))'
            ],
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return (False, 'Слишком долго')
    else:
        if result.returncode == 0:
            for i, got in enumerate(json.loads(result.stdout.splitlines()[-1])):
                if got == expected[i]:
                    continue
                else:
                    errors.append(
                        f'Тест {i + 1}: вход {all_args[i]} — ожидалось {expected[i]}, получено {got}'
                        )
            if not errors:
                return (True, 'Все тесты пройдены')
            else:
                return (False, '\n'.join(errors))
        else:
           return (
               False, f'Ошибка в коде\nошибки: {result.stderr.splitlines()[-1]}'
               )
