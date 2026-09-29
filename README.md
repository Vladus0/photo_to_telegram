# 🌌 Space Photo to Telegram Bot

Асинхронный Telegram-бот на Python, который автоматически собирает уникальный медиаконтент космической тематики из открытых API и публикует его в Telegram.
A Python-based Telegram bot that automatically fetches, filters, and uploads space imagery from **NASA API** and **SpaceX API** directly to a Telegram channel. Backed by an **SQLite** database to prevent duplicate posts.


## 🚀 Стек технологий
* **Язык:** Python 3.x
* **Библиотека бота:** `python-telegram-bot` (Асинхронная реализация)
* **Работа с сетью:** `requests` / `urllib`

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
git clone https://github.com/Vladus0/photo_to_telegram
```

2. Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл конфигурации `.env` и укажите ваши токены (`TELEGRAM_TOKEN` токен бота, `NASA_API_KEY` API-ключ, который создается на сайте nasa, `TG_CHAT_ID` id чата в который будут выкладываться картинки и `PROXY_URL` если вы используете vpn/proxy для работы tg).

4. Скачать картинки с сайта nasa:
```bash
python nasa.py
```

5. Запуск бота:
```bash
python unload_to_telegram.py
```


## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vladus0/photo_to_telegram
   cd photo_to_telegram
   ```

2. **Install dependencies:**
   ```bash
   pip install python-telegram-bot requests
   ```

3. **Configure Environment:**
   Replace the placeholders in the script with your actual `TELEGRAM_TOKEN`, `NASA_API_KEY`, `PROXY_URL` and `TG_CHAT_ID`.

4. **Download images from nasa:**
   ```bash
   python nasa.py
   ```

5. **Unload images to TG:**
```bash
python unload_to_telegram.py
```


## 📬 Контакты для связи
Если вам нужен похожий бот, парсер или скрипт для автоматизации рутины — пишите мне в Telegram: @Vladus_Dev0
Developed by an independent Python contractor specializing in automation, parsers, and Telegram ecosystem solutions. Telegram: @Vladus_Dev0
