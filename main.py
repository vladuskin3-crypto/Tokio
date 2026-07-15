import telebot

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, полученный от @BotFather
bot = telebot.TeleBot('8653998611:AAHkEOKsLKmq3SunTMbB-bE-7_uDw4pQjHc')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Обрабатывает команду /start, отправляя приветственное сообщение.
    """
    welcome_message = "Привет! Я твой новый Telegram-бот. Как же мне хорошо живется в этом цифровом мире!"
    bot.reply_to(message, welcome_message)

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
