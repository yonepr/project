import telebot
from config import api
from telebot import types

bot = telebot.TeleBot(f"{api}", parse_mode='MARKDOWN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("👋 Авторизация")
	btn2 = types.KeyboardButton("❓ Помощь")
	phone_number = types.KeyboardButton("Отправить контакт", request_contact=True)
	markup.add(btn1, btn2,phone_number)
	bot.send_message(message.chat.id, text="Привет, {0.first_name}! 🚗 \n Данный бот позволяет открывать шлагбаум 😎, находящийся на территории КБО для сотрудников \"ТКС Саров 📞\"".format(message.from_user), reply_markup=markup, parse_mode='MARKDOWN')
@bot.message_handler(content_types='text')
def message_reply(message):
	if message.text=="👋 Авторизация":
		a = telebot.types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id,"Отправьте свой контакт для авторизации, пожалуйста. (Нажмите на кнопку)")
		btn = types.ReplyKeyboardMarkup(resize_keyboard=True)


@bot.message_handler(content_types=['contact'])
def contact(message):
	if message.contact is not None:
		print(message.contact.phone_number)

@bot.message_handler(content_types='text')
def message_reply(message):
	if message.text=="❓ Помощь":
		bot.send_message(message.chat.id, "Для использования данного телеграм-бота пройдите этап авторизации, запросите пароль у Вашего администратора. После того как Вы авторизируйтесь, Вам откроются функции по открытию шлагбаума")






bot.polling(none_stop=True)