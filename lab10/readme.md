# Звіт до роботи — Lab10: Створення портфоліо з GitHub Pages

Мета роботи: Навчитись розгортати статичний сайт-портфоліо за допомогою GitHub Pages, налаштувати Jekyll (_config.yml), обрати тему та наповнити сторінки. Використати ChatGPT для генерації текстів/описів.

---
### Виконання роботи — кроки
1. Розмістіть файли сайту в папці проекту (ця папка — lab10). Переконайтесь, що у корені репозиторію є README.md або index.md.
2. Додайте `_config.yml` (вже підготовлено у цій теці).
3. Додайте `index.md` (сторінка портфоліо — вже підготовлена).
4. Зробіть коміт і пуш у гілку main:
   - git add .
   - git commit -m "Add GitHub Pages portfolio (lab10)"
   - git push origin main
5. Перейдіть у GitHub → Settings → Pages:
   - Source: Branch = main, Folder = / (root)
   - Натисніть Save
6. Зачекайте до ~10 хвилин — сайт стане доступним за URL: https://<username>.github.io/<repository_name>
7. (Опційно) Виберіть тему в `_config.yml` або через Settings → Themes. Після кожного коміту Pages буде автоматично деплоїтись (workflow pages-build-deployment).

---
### Що включено в цю папку
- `_config.yml` — базове налаштування сайту (title, description, theme)
- `index.md` — готова головна сторінка портфоліо (можна редагувати)
- `readme.md` — цей файл з інструкцією

---
### Поради щодо наповнення сторінки та використання ChatGPT
- Запитайте у ChatGPT підказку для написання розділу "Про мене" або описів проектів. Приклад prompt:
```
I am a student creating a portfolio site with GitHub Pages. Write a concise "About me" paragraph (3 sentences) and 3 short project descriptions (2–3 sentences each) suitable for a GitHub Pages index.md in Ukrainian.
```
- Вставте відповіді ChatGPT у `index.md` або окремі markdown-файли в папці.

---
### Чеклист для звіту (що вставити у файл звіту)
- Посилання на опублікований сайт (https://<username>.github.io/<repo>)
- Скриншот головної сторінки
- Вміст `_config.yml` (фрагмент)
- Фрагмент `index.md` з наповненням (або коментар ChatGPT)
- Опис дій: як ви обрали тему, чи змінювали конфіг, чи працював автоматичний workflow pages-build-deployment

---
### Приклад очікуваного результату
- Сайт: "Portfolio Example" з описом, розділами Projects/Contact.
- GitHub Actions: pages-build-deployment workflow запустився та успішно завершив деплой.

---
### Примітки
- Якщо ви хочете кастомну тему, перевіряйте сумісність теми з GitHub Pages (багато тем доступні як `remote_theme` або `theme`).
- Після внесення змін робіть новий коміт — Pages автоматично оновить сайт.
- Для локального попереднього перегляду можна встановити Jekyll та запускати `bundle exec jekyll serve`.

---