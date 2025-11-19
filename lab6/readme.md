# Звіт до роботи — Lab6: Віртуальні середовища та сторонні бібліотеки

Мета роботи: Ознайомитись зі створенням і використанням ізольованих віртуальних середовищ (venv, pipenv, poetry), роботою з pip, встановленням сторонніх бібліотек (requests, flask, jikanpy) та запуском прикладних скриптів.

---
### Виконання роботи — кроки
1. Перевірити інсталяцію pip:
   - pip -V
   - pip --help
   - pip list
   Скопіюйте вивід цих команд у звіт (або зробіть скриншот).

2. Встановити та перевірити requests:
   - pip install requests
   - python -c "import requests; print(requests.__version__)"
   - pip show requests
   - pip uninstall requests
   У звіт вставте вивід команд (версія, location).

3. Запустити приклад sample_requests.py:
   - Перехід у теку:
     cd d:\pythonTestSW\PythonTestSW\lab6
   - Запуск:
     python sample_requests.py
   Скопіюйте консольний вивід (status code, заголовки, приклади iter_lines).

4. Flask + Jikan приклад:
   - Встановити залежності:
     pip install flask jikanpy
   - Запустити:
     python flask_jikan.py
   - Відкрити у браузері: http://127.0.0.1:5000
   У звіт вставте скриншот або текст відповіді/помилки.

5. Практика з venv:
   - Створити середовище:
     python -m venv ./my_env
   - Активувати (Windows):
     my_env\Scripts\activate
     (Unix: source my_env/bin/activate)
   - Встановити requests:
     pip install requests
   - Перевірити:
     pip show requests
   - Деактивувати:
     deactivate
   - Після деактивації виконати:
     pip show requests
   У звіті поясніть результат останньої команди (чи видно package глобально або ні).

6. Pipenv (опціонально):
   - pip install pipenv
   - pipenv --python 3.10
   - pipenv install requests
   - pipenv --venv
   - pipenv run python -c "import requests; print(requests.__version__)"
   Переконайтесь у наявності Pipfile та Pipfile.lock — вставте їх фрагменти у звіт.

7. Poetry (опціонально):
   - pip install poetry
   - poetry new demo_project  (або poetry init)
   - cd demo_project
   - poetry add requests
   - poetry show
   - poetry run python app.py  (або poetry shell → python app.py)
   Вставте вивід poetry show або фрагмент pyproject.toml у звіт.

8. .env та змінні середовища:
   - Створіть .env з прикладом:
     HELLO=world
   - Перевірка у Python:
     python -c "import os; print(os.environ.get('HELLO'))"
   Поясніть, що зміниться без активації середовища (pipenv читає .env у своїй сесії; інші інструменти — ні, залежить від способу запуску).

---
### Що вставити у звіт (чеклист)
- pip -V вивід
- pip list (або скриншот)
- pip show requests (до/після установки або у venv)
- Вивід sample_requests.py (статус, приклади заголовків, строки iter_lines)
- Результат запуску flask_jikan.py (сервер стартував / помилка)
- Фрагменти Pipfile / Pipfile.lock (якщо використовували pipenv)
- Фрагмент pyproject.toml або вивід poetry show (якщо використовували poetry)
- Пояснення результату pip show requests після деактивації venv
- Примітка про .gitignore і ігнорування папок віртуальних середовищ

---
### Файли в папці lab6
- sample_requests.py — приклад роботи з requests і iter_lines
- flask_jikan.py — приклад Flask + jikanpy (потрібно встановити залежності)
- poetry_app/pyproject.toml, poetry_app/app.py — мінімальний poetry-проєкт
- lab6_report.md — шаблон звіту з інструкціями
- .gitignore — ігнорування середовищ та тимчасових файлів

---
### Очікуваний фрагмент виводу (приклад)
- pip -V -> pip X.Y.Z from C:\...\site-packages\pip (python 3.x)
- sample_requests.py -> Status code: 200; заголовки: Content-Type: application/json; iter_lines -> декілька JSON рядків
- flask_jikan.py -> Running on http://127.0.0.1:5000/  (або повідомлення про помилку API/залежностей)

---
### Поради
- Не комітьте каталоги віртуальних середовищ (використайте .gitignore).
- Для Flask/Jikan переконайтесь, що є інтернет-з'єднання та дотримуйтеся лімітів API.
- Збережіть консолі-вивід у окремий файл report_results.md або вставте в цей readme.