# Звіт до роботи — Lab8: Автоматизація з GitHub Actions

Мета роботи: Навчитись створювати та налаштовувати GitHub Actions workflows для:
- ручного запуску (workflow_dispatch),
- тригерів по розкладу (schedule / cron),
- CI для Python: встановлення залежностей, запуск тестів, збір coverage, відправка звітів.

---
### Виконання роботи — кроки
1. Зберегти файли workflow у теку .github/workflows у папці lab8.
2. Запушити зміни у репозиторій і перейти у вкладку Actions — переконатися, що з'явились два воркфлови.
3. Запустити Manual workflow вручну (Actions → обрати workflow → Run workflow), передати параметр name щоб продемонструвати передачу input.
4. Запустити CI workflow на push або вручну; переглянути логи кроків: Checkout, Setup Python, Install deps, Run tests, Generate coverage, Upload to Codecov.

---
### Які файли додано
- .github/workflows/manual_workflow.yml — ручний + schedule воркфлоу з параметром inputs.name і прикладом кроку, що запускає python run_me.py
- .github/workflows/python_ci.yml — CI воркфлоу: встановлює Python, встановлює pytest/coverage, запускає тести та генерує coverage xml; використовує codecov action для завантаження (параметр token опціональний)
- run_me.py — демонстраційний скрипт, який запускається з workflow

---
### Інструкції по перевірці / приклади команд
- Перевірити на CI кроці запуск скрипта: python run_me.py — очікуваний вивід: "Lab8 demo run_me executed"
- Для coverage: coverage run -m pytest && coverage xml — після цього перевірити файл coverage.xml

---
### Badge / статус
1. У GitHub Actions оберіть workflow → Create status badge → скопіюйте markdown і додайте у верх README.md вашого репозиторію.
2. Для coverage badge використайте сервіс codecov.io → створіть badge → додайте у README.md.

---
### Що вставити у звіт (чеклист)
- Скриншот вкладки Actions з двома воркфлоу.
- Логи запуску одного workflow (вкладення або витяг тексту).
- Вміст файлу .github/workflows/python_ci.yml (короткий фрагмент).
- Вміст coverage.xml або посилання на codecov.io.
- Markdown badge вищезгаданої CI збірки (скопійований код).

--- 
Приклад очікуваного фрагмента виводу:
- run_me.py -> Lab8 demo run_me executed
- CI -> Tests: collected X passed Y failed 0
- Coverage -> coverage.xml згенеровано