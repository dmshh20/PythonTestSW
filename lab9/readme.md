# Звіт до роботи — Lab9: Робота з базами даних (SQLite)

Мета роботи: Навчитись створювати локальні бази даних SQLite, працювати з SQL-запитами (CREATE, INSERT, SELECT, UPDATE, DELETE), виконувати параметризовані запити та експортувати результати.

---

### Виконання роботи — кроки
1. Перейдіть у папку:
   cd d:\pythonTestSW\PythonTestSW\lab9

2. Запустіть демонстраційний скрипт:
   python db_demo.py

3. Перегляньте створені файли:
   - lab9_demo.db — SQLite база
   - students_export.csv — експорт даних

4. Скопіюйте консольний вивід у звіт або зробіть скриншоти.

---

### Що робить скрипт db_demo.py
- Створює або підключається до файлу lab9_demo.db
- Створює таблицю students (empid INTEGER PRIMARY KEY, firstname, lastname)
- Видаляє існуючі рядки (щоб повторний запуск був чистим для демонстрації)
- Додає приклади записів (SAMPLE_STUDENTS)
- Виконує SELECT * і виводить результат
- Демонструє параметризований SELECT (з WHERE)
- Оновлює lastname для одного запису
- Видаляє один запис
- Виводить PRAGMA table_info для перегляду схеми
- Експортує поточну таблицю у students_export.csv

---

### Приклад очікуваного виводу (фрагмент)
- Table 'students' ensured.
- Inserting sample students...
- Students after insert:
  (1, 'Bohdan', 'Ivanov')
  (2, 'Marta', 'Petrenko')
  (3, 'Olena', 'Kovalenko')
- Parameterized query (firstname='Marta'):
  [(2, 'Marta', 'Petrenko')]
- Updating empid=1 lastname -> 'UpdatedName'
- After update: [(1, 'Bohdan', 'UpdatedName'), ...]
- Deleting empid=2
- After delete: [...]
- Table info (PRAGMA table_info):
  (0, 'empid', 'INTEGER', 0, None, 1)
  (1, 'firstname', 'TEXT', 1, None, 0)
  (2, 'lastname', 'TEXT', 1, None, 0)
- Exported students to students_export.csv

---

### Що вставити у фінальний звіт
- Консольний вивід db_demo.py або скриншот терміналу
- Файл students_export.csv (фрагмент або приклад рядків)
- Короткий SQL-скрипт, який ви виконали (приклади INSERT/SELECT/UPDATE/DELETE)
- Відповіді на питання:
  - Як створюється таблиця в SQLite?
  - Як виконуються параметризовані запити та чому це важливо (безпека / SQL injection)?
  - Що робить PRAGMA table_info?

---

### Примітки
- Файл lab9_demo.db можна відкрити в DB Browser for SQLite або інструменті IDE.
- Не додавайте бази даних до репозиторію — додано .gitignore нижче.

...existing code...