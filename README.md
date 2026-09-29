# 🌌 Space Photo to Telegram Bot

Асинхронный Telegram-бот на Python, который автоматически собирает уникальный медиаконтент космической тематики из открытых API и публикует его в Telegram.
A Python-based Telegram bot that automatically fetches, filters, and uploads space imagery from **NASA API** and **SpaceX API** directly to a Telegram channel. Backed by an **SQLite** database to prevent duplicate posts.


## 🚀 Стек технологий
* **Язык:** Python 3.x
* **Библиотека бота:** `python-telegram-bot` (Асинхронная реализация)
* **Работа с сетью:** `requests` / `urllib`
* **База данных:** `SQLite` (для логирования и контроля отправленных медиа)

## 🚀 Features
* **Multi-source Parsing:** Downloads dynamic image content via official and community space APIs.
* **Smart Duplication Filter:** Uses SQLite database to track already sent images.
* **Asynchronous Design:** Powered by `python-telegram-bot` for smooth and stable performance.
* **Clean Logging:** Integrated production-ready logging system for easy debugging.


## 🛠️ Функционал и модули
* **NASA Модуль:** Интеграция с официальным NASA API для получения снимков Земли и космоса.
* **SpaceX Модуль:** Парсинг данных о запусках ракет и получение официальных медиа-материалов.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** `python-telegram-bot`
* **API Integration:** `requests`


## ⚙️ Как запустить проект локально

1. Клонируйте репозиторий:
```bash
git clone https://github.com
```

2. Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл конфигурации или укажите ваши токены (`BOT_TOKEN` и `NASA_API_KEY`) в настройках проекта.

4. Запустите бота:
```bash
python main.py
```


## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd photo_to_telegram
   ```

2. **Install dependencies:**
   ```bash
   pip install python-telegram-bot requests
   ```

3. **Configure Environment:**
   Replace the placeholders in the script with your actual `TELEGRAM_TOKEN`, `CHANNEL_ID`, and `NASA_API_KEY`.

4. **Run the Bot:**
   ```bash
   python main.py
   ```

## 📬 Контакты для связи
Если вам нужен похожий бот, парсер или скрипт для автоматизации рутины — пишите мне в Telegram: @Vladus_Dev0
Developed by an independent Python contractor specializing in automation, parsers, and Telegram ecosystem solutions. Telegram: @Vladus_Dev0
