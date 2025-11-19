# Звіт до роботи — Lab7: Тестування (assert, unittest, pytest, coverage)

Мета роботи: Навчитись писати перевірки (assert), обробляти помилки при валідації, створювати юніт-тести (unittest та pytest) та збирати просту інформацію про покриття тестами.

--- 
### Файли
- app.py — реалізація класів Figure та Name (з валідацією та доданим методом get_angles).
- sample_asserts.py — приклади використання assert і валідації вводу.
- test_app.py — тести на unittest для класу Figure.
- test_pytest.py — приклад pytest тесту.
- .gitignore — ігнорування __pycache__ та віртуальних середовищ.

--- 
### Як виконати (швидко)
1. Перейти в теку проекту:
   cd d:\pythonTestSW\PythonTestSW\lab7

2. Запустити unittest:
   python -m unittest -v

3. Запустити pytest (якщо встановлено):
   pytest -q

4. (опціонально) Зібрати покриття (якщо встановлено coverage/pytest-cov):
   coverage run -m pytest
   coverage report
   coverage html  # згенерує html-репорт

--- 
### Що перевірити і вставити у звіт
- Результат виконання `python -m unittest -v` (які тести пройшли/провалилися).
- Результат `pytest -q` (якщо використали).
- Логи помилок при запуску sample_asserts.py або при створенні об'єктів з неправильними даними.
- HTML-репорт coverage (index.html) — додати як артефакт.

--- 
### Очікувані кейси для перевірки
- a) Ввести нечислове значення у sample_asserts.py -> assert відпрацьовує.
- b) Створити Figure("коло", 1) -> AssertionError.
- c) Тест test_figure_type та test_figure_length повинні проходити (коли клас реалізовано вірно).
- d) pytest тест test_app_triangle повинен підтвердити створення трикутника.

--- 
### Поради
- Не комітьте __pycache__ або папки venv у репозиторій (.gitignore додано).
- Якщо використовуєте pytest/coverage — встановіть їх у віртуальному середовищі.