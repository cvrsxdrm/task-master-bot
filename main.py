import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот, хранитель целей и задач. Я умею записывать то, что ты хочешь запомнить, только напиши свою цель или задачу в чат!")

@bot.message_handler(commands=['read'])
def send_goals(message):
    with open("goals.txt", "r", encoding = "utf-8") as f:
        all_goals = f.read()
        if all_goals:
            bot.send_message(message.chat.id, f"Твои цели:\n{all_goals}")
        else:
            bot.send_message(message.chat.id, "Список пока пуст!")

@bot.message_handler(func=lambda message: True)
def handle_txt(message):
    with open("goals.txt", "a", encoding = "utf-8") as f:
        f.write(message.text + "\n")
    bot.reply_to(message, "Сохранил! Для просмотра запсией используйте команду /read")

print("Bot is running...")
bot.infinity_polling(skip_pending=True)