# Код для скачивания фотографий про космос от spacex и nasa

Код скачивает фотографии с сайтов spacex и nasa

### Как установить 

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Далее в .env файле найдете 3 переменные: API_KEY, TOKEN, TIME. 

API_KEY - это ваш айпи от nasa, он нужен чтобы скачивать фото от nasa. Получить его можно, зарегистрировавшись на сайте [nasa](https://api.nasa.gov/)

TOKEN - это токен вашего бота в телеграме, который будет скачивать и присылать фото. Выглядит токен примерно так: `958423683:AAEAtJ5Lde5YYfkjergber`

TIME - это время, через которое бот начнет снова присылать вам фотографии. Время устанавливается в секундах

CHAT_ID - это id вашего бота в телеграме

```
API_KEY=ваш nasa айпи
TOKEN=токен бота в телеграме
TIME=время
CHAT_ID=id вашего бота
```


### Запуск программы

Чтобы скачать фото spacex, вам нужно написать в консоль spacex.py

```
python spacex.py
```

Чтобы скачать фото nasa, вам нужно написать в консоль nasa.py

```
python nasa.py
```

Чтобы скачать фото nasa_epic, вам нужно написать в консоль nasa_epic.py

```
python nasa_epic.py
```

Чтобы запустить программу для вывода фотографий в телеграм вам нужно написать в консоль install_to_telegram.py

```
python install_to_telegram.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).