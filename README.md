## Python: Telegram Чат-бот / Менеджер задач

---

## 🇷🇺 Русская версия

### 📝 Описание

**``Python: Telegram Чат-бот / Менеджер задач``** - это удобный и простой Telegram-бот, написанный на Python. Он предназначен для управления задачами внутри небольшой команды. Бот позволяет добавлять коллег, назначать им задачи и просматривать текущий список дел прямо в мессенджере Telegram.

Этот проект отлично подходит для демонстрации навыков работы с библиотекой pyTelegramBotAPI (Telebot) и создания интерактивных ботов.

**✨ Основной функционал**

``
/add_colleague - Добавление нового коллеги (создание нового списка задач).
``

``
/add_task - Назначение новой задачи для выбранного коллеги (с использованием удобной клавиатуры).
``

``
/all - Просмотр всех текущих задач по всем коллегам.
``

``
/colleague - Просмотр списка задач конкретного пользователя.
``

Интерактивное меню - Бот предлагает кнопки для быстрого выбора имени коллеги, чтобы не вводить его вручную.

**🛠 Требования**

Для запуска бота на вашем компьютере или сервере потребуется:

Python версии 3.7 или выше.

Установленная библиотека pyTelegramBotAPI.

Уникальный токен Telegram-бота (можно получить у **``@BotFather``** в Telegram).

**🚀 Установка и запуск**

Клонируйте репозиторий:

``
git clone https://github.com/ВАШ_USERNAME/PY-TGBot.git
``

``
cd PY-TGBot
``

Установите зависимости:

``
pip install pyTelegramBotAPI
``

Настройте токен бота:
Откройте файл Chatbot_Telegram.py в любом текстовом редакторе и замените строку **``'ТВОЙ_ТОКЕН_ЗДЕСЬ'``** на ваш реальный токен, полученный от BotFather.

TOKEN = **``'123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ'``**


**🤖 Запустите бота:**

``python Chatbot_Telegram.py``


Перейдите в Telegram, найдите своего бота и отправьте команду **``/start``**!

### Лицензия / Отказ от ответственности

Этот проект распространяется под лицензией **MIT** — подробности см. в файле [LICENSE](LICENSE).

### ⚠️ ВАЖНО:

* **Использование на свой страх и риск:** Данный скрипт и инструкция предоставляются «как есть» (as is). Автор не несет ответственности за любые сбои в работе вашей системы, потерю данных или повреждение оборудования.
* **Внешние зависимости:** При установке библиотек через `requirements.txt` вы используете стороннее ПО, за безопасность которого автор ответственности не несет.
* **Проверка кода:** Настоятельно рекомендуется изучить код перед запуском и протестировать его в безопасной среде, а перед применением выполнить создание точки восстановления системы.

---

**Авторские права © 2026 [Иван Бирючков / https://github.com/biryuchkov-ia]**

---

## 🇬🇧 English Version

### 📝 Description

**``Python: Telegram Chatbot / Task Manager``** - is a convenient and straightforward Telegram bot written in Python. It is designed for task management within a small team. The bot allows you to add colleagues, assign tasks to them, and view the current to-do list directly in the Telegram messenger.

This project is perfect for showcasing skills in working with the pyTelegramBotAPI (Telebot) library and building interactive bots.

**✨ Features**

``
/add_colleague - Add a new colleague (creates a new task list for them).
``

``
/add_task - Assign a new task to a selected colleague (using a user-friendly custom keyboard).
``

``
/all - View all current tasks for all colleagues.
``

``
/colleague - View the task list of a specific user.
``

Interactive Menu - The bot provides reply keyboards for quick colleague selection, minimizing manual typing.

**🛠 Prerequisites**

To run the bot on your local machine or server, you will need:

Python 3.7 or higher.

The pyTelegramBotAPI library installed.

A unique Telegram Bot Token (can be obtained from **``@BotFather``** in Telegram).

**🚀 Installation and Setup**

Clone the repository:

``
git clone https://github.com/YOUR_USERNAME/PY-TGBot.git
``

``
cd PY-TGBot
``

Install dependencies:

``
pip install pyTelegramBotAPI
``

Configure the bot token:
Open the Chatbot_Telegram.py file in any text editor and replace the **``'ТВОЙ_ТОКЕН_ЗДЕСЬ'``** string with your actual token received from BotFather.

TOKEN = **``'123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ'``**


**🤖 Run the bot:**

``python Chatbot_Telegram.py``


Go to Telegram, find your bot, and send the **``/start``** command!

### License / Disclaimer

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

### ⚠️ IMPORTANT:

* **Use at your own risk:** These script and instruction are provided "as is". The author is not liable for any system failures, data loss, or hardware damage.
* **External dependencies:** By installing packages from `requirements.txt`, you are using third-party software at your own discretion.
* **Code review:** It is highly recommended to study the code before execution and test it in a safe environment. It is also advised to create a system restore point before use.

---

**Copyright © 2026 [Ivan Biryuchkov / https://github.com/biryuchkov-ia]**

---