import requests,telebot
from text import token 
from telebot import types
from AppOpener import *

bot = telebot.TeleBot(token)
open("Telegram")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/weather")
    btn2 = types.KeyboardButton("/help")
    markup.add(btn1, btn2)
    bot.reply_to(message, "Привет! Я  eco_bot . Напиши команду /help  для ознакомлений с командам или команду /weather для ознакомления с погодой в твоем городе на сегодня".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_message_begin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/who_are_you")
    btn2 = types.KeyboardButton("/about_your_site")
    btn3 = types.KeyboardButton("/ssilka_on_site")
    btn4 = types.KeyboardButton("/bye")
    btn5 = types.KeyboardButton("/start")
    markup.add(btn1, btn2,btn3,btn4,btn5)
    bot.send_message(message.chat.id, "Я могу отвечать на такие команды как:  ".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['who_are_you'])
def send_message_1(message):
    bot.send_message(message.chat.id, "Я экологический бот который отправит тебе ссылочку на сайт о экологии")


@bot.message_handler(commands=['about_your_site'])
def send_message_2(message):
    bot.send_message(message.chat.id, "Статья рассматривает глобальное потепление как насущную проблему, которая уже сегодня затрагивает нашу повседневную жизнь. В ней подробно описаны реальные изменения климата, вызванные человеческой деятельностью (сжигание ископаемого топлива, вырубка лесов, неустойчивое сельское хозяйство и промышленное производство), а также последствия этих процессов для здоровья, экономики, продовольственной безопасности и биоразнообразия. Автор приводит практические рекомендации по снижению углеродного следа, рациональному потреблению, поддержке экологически ответственных компаний, повышению информированности и политической активности, подчёркивая, что бездействие недопустимо для сохранения нашей планеты.")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.send_message(message.chat.id, "Пока! Удачи!")

@bot.message_handler(commands=['ssilka_on_site'])
def send_message_3(message):
    bot.send_message(message.chat.id, "ок держи.ссылочка ")

@bot.message_handler(commands = ['weather'])
def weather(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("/start")
  markup.add(btn1)
  bot.send_message(message.chat.id,"Напиши тот город в котором ты находишься.Если хочешь вернуться в начало тогда нажми на кнопку start ".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types='text')
def weather(message):
    city = message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_base = requests.get(url).json()
    print(weather_base)
    try:
        temperature = weather_base['main']['temp']
        temperature_feels = weather_base['main']['feels_like']
        wind_speed = weather_base['wind']['speed']
        humidity = weather_base['main']['humidity']
        weather_description = weather_base['weather'][0]['description'] 
        weather_message = (
                            f" Погода в городе {city}:\n"
                            f"Температура: {temperature}°C\n"
                            f"Ощущается как: {temperature_feels}°C\n"
                            f"Влажность: {humidity}%\n"
                            f"Ветер: {wind_speed} м/с\n"
                            f"Описание: {weather_description}\n"
                        )    
        bot.send_message(message.chat.id,weather_message)
    except Exception as e:
        eror = "Произошла ошибка при выводе данных или при неверном названии города .Перезапустите бота и запишите ещё раз название города"
        bot.reply_to(e,eror=eror)
try:
    if __name__ == "__main__":
            bot.polling()
            bot.run(debug=True)
except Exception as e:
    print("Произошла ошибка при выводе данных")
    bot.send_message(e,"Наверное произошёл сбой в программе")
    
    