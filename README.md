# 🚀 TerminAI (FixIt)

**TerminAI** — это ваш умный второй пилот для терминала.
Он автоматически обнаруживает ошибки в консольных командах, анализирует их с помощью AI и предлагает готовые решения для исправления.

![AI-Powered](https://img.shields.io/badge/AI--Powered-blue) ![Python](https://img.shields.io/badge/Python-3.10+-yellow) ![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Возможности

- 🤖 **AI-анализ:** Понимает контекст ошибки (Python, Docker, Git, System).
- ⚡ **Мгновенный фикс:** Предлагает исправленную команду.
- 🛡 **Безопасность:** Вы сами подтверждаете выполнение исправления.
- 🚀 **Поддержка Groq:** Использует сверхбыстрые модели Llama 3 бесплатно.

## 🛠 Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/ВАШ_НИК/terminai.git
   cd terminai
   ```

2. **Установите инструмент:**
   ```bash
   pip install -e .
   ```

3. **Получите бесплатный API ключ (для скорости):**
   - Зайдите на [console.groq.com](https://console.groq.com)
   - Создайте новый API Key.
   - Скопируйте его (начинается на `gsk_...`).

4. **Настройте ключ:**
   ```bash
   # Linux / macOS
   export OPENAI_API_KEY="ваш_ключ_gsk_..."
   
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="ваш_ключ_gsk_..."
   ```

## 💻 Использование

Просто добавьте `fixit` перед любой вашей командой:

```bash
fixit "apt-get install python3"
```

Если команда упадет (например, вы забыли `sudo`), TerminAI проанализирует ошибку и предложит решение:

```text
🔴 Problem: Permission denied. You need root privileges.
🟢 Suggested Fix: sudo apt-get install python3

Apply this fix? [Y/n]: 
```

## 🧪 Как протестировать (Безопасная Песочница)

В проекте есть встроенный Docker-стенд, где можно безопасно "ломать" систему, не боясь за свой компьютер.

1. Перейдите в папку тестов:
   ```bash
   cd tests
   ```

2. Запустите песочницу (передав свой ключ):
   ```bash
   # Windows PowerShell
   $env:OPENAI_API_KEY="ваш_ключ_gsk..."
   docker-compose build
   docker-compose run terminai-test
   ```

3. Внутри контейнера попробуйте эти сценарии:

   **Сценарий 1: Несуществующий файл**
   ```bash
   fixit "cat /nonexistent.txt"
   # AI предложит создать файл
   ```

   **Сценарий 2: Отсутствующий пакет Python**
   ```bash
   fixit "python3 -c 'import numpy'"
   # AI предложит pip install numpy
   ```

   **Сценарий 3: Запуск сервисов**
   ```bash
   fixit "docker ps"
   # AI поймет, что сервис Docker не запущен
   ```

## 📋 Примеры реакций

| Сценарий | Команда пользователя | Реакция AI |
|----------|---------------------|------------|
| **Опечатка** | `git comit` | `git commit` |
| **Python** | `import numpy` (нет модуля) | `pip install numpy` |
| **Доступ** | `cat /root/secret` | `sudo cat /root/secret` |

---
Created with 🤍 by **SanMog** for **Xsires**