import telebot
TOKEN = "8001551459:AAG4yghPSN3VdFrc86k4Gq5hS_E6HUwqC2Q" # توکن رباتت از BotFather
bot = telebot.TeleBot(TOKEN)
دستور /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! ربات تست شد. حالا میتونی متن یا فایل بفرستی.")
دریافت متن
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.reply_to(message, f"تو گفتی: {message.text}")
bot.polling()
