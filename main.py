import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("Посмотреть цели 🎯")
    button2 = types.KeyboardButton("Что ты умеешь?")
    button3 = types.KeyboardButton("Очистить цели и задачи 🗑️")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "🌟 Привет!\n\n Я бот, хранитель целей и задач. Я помогу тебе запомнить важное!\n\n 🚀 Удачи в достижении целей.", reply_markup = markup)

@bot.message_handler(func=lambda message: message.text == "Посмотреть цели 🎯")
def send_goals(message):
    with open("goals.txt", "r", encoding = "utf-8") as f:
        goals = f.readlines()
        result = "Твои цели:\n"
        if goals:
            for index, goal in enumerate(goals, start=1):
                result += f"{index}. {goal}"
            bot.send_message(message.chat.id, result)
        else:
            bot.send_message(message.chat.id, "Список пока пуст!")

@bot.message_handler(func=lambda message: message.text == "Что ты умеешь?")
def send_skills(message):
    bot.send_message(message.chat.id, "Я умею записвать твои цели и задачи. Только напиши в чат - что ты хочешь запомнить? ✏️")

@bot.message_handler(func=lambda message: message.text == "Очистить цели и задачи 🗑️")
def clear_all_goals (message):
    with open("goals.txt", "w", encoding = "utf-8") as f:
        f.write('')
    bot.reply_to(message, "Файл успешно очищен.")

@bot.message_handler(commands=['del'])
def delete_goal(message):
    with open("goals.txt", "r", encoding = "utf-8") as f:
        lines = f.readlines()

    try:
        idx = int(message.text.split()[1]) - 1
        lines.pop(idx)
        with open("goals.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)
        bot.reply_to(message, f"Цель №{idx + 1} успешно удалена! ✅")
    except:
        bot.reply_to(message, "Ошибка! Введи номер цели, например: /del 1")

@bot.message_handler(func=lambda message: True)
def handle_txt(message):
    with open("goals.txt", "a", encoding = "utf-8") as f:
        f.write(message.text + "\n")
    bot.reply_to(message, "Сохранил!")

print("Bot is running...")
bot.infinity_polling(skip_pending=True)