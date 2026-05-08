import telebot
from telebot import types

# Вставь сюда токен, который выдаст @BotFather в Telegram
TOKEN = 'ТВОЙ_ТОКЕН_ЗДЕСЬ'
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения задач (в реальном проекте лучше использовать базу данных, например SQLite)
schedule = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        f"Привет, {message.from_user.first_name}!\n"
        "Я твой Telegram-бот помощник.\n\n"
        "Я храню данные о задачах на день. Для управления мной используй команды:\n"
        "/all - Вывести все задачи\n"
        "/colleague - Вывести задачи по одному из коллег\n"
        "/add_task - Добавить новую задачу\n"
        "/add_colleague - Добавить нового коллегу"
    )
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['all'])
def show_all_tasks(message):
    if not schedule:
        bot.send_message(message.chat.id, "Список коллег и задач пока пуст. Добавьте кого-нибудь с помощью /add_colleague")
        return

    response = "📋 **Список дел на сегодня:**\n\n"
    for name, tasks in schedule.items():
        response += f"👤 **{name}**\n"
        if tasks:
            for i, task in enumerate(tasks, 1):
                response += f"  {i}. {task}\n"
        else:
            response += "  Нет задач\n"
        response += "\n"
    
    bot.send_message(message.chat.id, response, parse_mode='Markdown')

@bot.message_handler(commands=['add_colleague'])
def add_colleague_start(message):
    msg = bot.send_message(message.chat.id, "Введите имя нового коллеги:")
    bot.register_next_step_handler(msg, process_add_colleague)

def process_add_colleague(message):
    name = message.text.strip()
    if name in schedule:
        bot.send_message(message.chat.id, f"Коллега {name} уже существует!")
    else:
        schedule[name] = []
        bot.send_message(message.chat.id, f"✅ Коллега {name} успешно добавлен!")
        show_all_tasks(message)

@bot.message_handler(commands=['add_task'])
def add_task_start(message):
    if not schedule:
        bot.send_message(message.chat.id, "Сначала добавьте хотя бы одного коллегу через /add_colleague")
        return
    
    # Создаем клавиатуру с именами коллег для удобного выбора
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for name in schedule.keys():
        markup.add(types.KeyboardButton(name))
        
    msg = bot.send_message(message.chat.id, "Выберите или введите имя коллеги:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_task_colleague_name)

def process_task_colleague_name(message):
    name = message.text.strip()
    if name not in schedule:
        bot.send_message(message.chat.id, f"Коллеги {name} нет в списке. Попробуйте снова или добавьте его.", reply_markup=types.ReplyKeyboardRemove())
        return
    
    msg = bot.send_message(message.chat.id, f"Введите задачу для {name}:", reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, process_add_task, name)

def process_add_task(message, name):
    task = message.text.strip()
    schedule[name].append(task)
    bot.send_message(message.chat.id, f"✅ Задача добавлена коллеге {name}!")
    show_all_tasks(message)

@bot.message_handler(commands=['colleague'])
def show_colleague_tasks_start(message):
    if not schedule:
        bot.send_message(message.chat.id, "Список коллег пока пуст.")
        return
        
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for name in schedule.keys():
        markup.add(types.KeyboardButton(name))
        
    msg = bot.send_message(message.chat.id, "Чьи задачи вы хотите посмотреть?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_show_colleague)

def process_show_colleague(message):
    name = message.text.strip()
    # Убираем клавиатуру после выбора
    if name not in schedule:
        bot.send_message(message.chat.id, f"Коллега {name} не найден.", reply_markup=types.ReplyKeyboardRemove())
        return
        
    tasks = schedule[name]
    if not tasks:
        bot.send_message(message.chat.id, f"У коллеги {name} пока нет задач.", reply_markup=types.ReplyKeyboardRemove())
        return
        
    response = f"📋 **Список дел по коллеге {name}:**\n"
    for i, task in enumerate(tasks, 1):
        response += f"{i}. {task}\n"
        
    bot.send_message(message.chat.id, response, parse_mode='Markdown', reply_markup=types.ReplyKeyboardRemove())

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    # none_stop=True означает, что бот не перестанет работать при возникновении ошибок
    bot.polling(none_stop=True)