# Импортируем необходимые библиотеки
import logging
import asyncio
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import schedule
import time
import datetime

# Устанавливаем уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализируем бота и диспетчера
bot = Bot(token="6091626104:AAHPxXmAeRaPjnMBe1VO_6JI05lQfl21gKw")
dp = Dispatcher(bot)


# Обработчик команды /start
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("💻🌐 Добро пожаловать на наш интернет-агрегатор! 🤝 Мы рады помочь вам найти лучшие предложения от ведущих провайдеров в Белгородской области. 🏙✨")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
    markup.add(KeyboardButton("Выбрать тариф"))
    markup.add(KeyboardButton("Информация"))
    markup.add(KeyboardButton("Связаться с нами"))
    await message.answer("Выберите провайдера:", reply_markup=markup)


# Обработчик кнопки "выбрать тариф"
@dp.message_handler(lambda message: message.text == "Выбрать тариф")
async def process_service_order(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
    markup.add(KeyboardButton("Ростелеком"), KeyboardButton("МТС"))
    markup.add(KeyboardButton("Мегафон"), KeyboardButton("Оборудование"))
    markup.add(KeyboardButton("Вернуться"))
    await message.answer("Выберите провайдера:", reply_markup=markup)


# Обработчик кнопки "Информация"
@dp.message_handler(lambda message: message.text == "Информация")
async def process_service_info(message: types.Message):
    text = """
    🔹 Multinet - это интернет-агрегатор, который сравнивает предложения от разных интернет-провайдеров на одной платформе. Multinet помогает пользователям найти наиболее подходящие и выгодные тарифы на домашний интернет. 💻🌐💰
🔹 Multinet выводит на экран список предложений от каждого провайдера, содержащий информацию о цене, скорости соединения, тарифных планах и других деталях. 🏠🌐📊
🔹 Пользователи могут сравнить предложения от разных провайдеров на одной странице и выбрать наиболее подходящий для себя. Multinet может быть полезным инструментом для пользователей, которые ищут выгодные предложения на рынке интернет-услуг. 👍
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
    markup.add(KeyboardButton("выбрать тариф"))
    await message.answer(text, reply_markup=markup)


# Обработчики для каждой кнопки
# обработчик кнопки "Ростелеком"
# Обработчик тарифов МТС
# Функция для создания кнопки "Подключить тариф"
def create_button():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Подключить тариф", url="https://www.tbforum.ru/hs-fs/hubfs/%D0%A2%D0%A1%D0%A1%20(+%D0%BA%D0%A1%D0%A1%D0%92)/%D0%A0%D0%BE%D1%81%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC-4.jpg?width=2560&name=%D0%A0%D0%BE%D1%81%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D0%BE%D0%BC-4.jpg"))
    return markup

@dp.message_handler(lambda message: message.text == "Ростелеком")
async def process_rostelecom(message: types.Message):
    # Создаем список с тарифами
    tariffs =[
        {"name": " Тариф Технологии доступа",
         "description": " Домашний интернет\n Скорость: 100 Мбит/сек",
         "price": " 450 рублей/месяц\n Надежный и быстрый интернет по выгодной цене - это реальность!"},
        {"name": "Технологии возможностей",
         "description": "домашний интернет: 100 мбит/с, Интерактивное телевидение :187 каналов",
         "price": "700 рублей/месяц"},
        {"name": "Технологии общения",
         "description": "домашний интернет: 100 мбит/с, мобильная связь: 50 гб интернета / 1200 минут",
         "price": "590 рублей/месяц"},
        {"name": "Технологии выгоды",
         "description": "домашний интернет 100 мбит/с, интерактивное телевидение 187 каналов, мобильная связь: 50 гб интернета / 1200 минут",
         "price": "780 рублей/месяц"},
        {"name": "Технологии выгоды+",
         "description": "домашний интернет 100мбит/с, Интерактивное телевидение 197 каналов, мобильная связь 3 сим 50гб интернета/ 2000 минут",
         "price": "950 рублей/месяц"}
    ]

    # Отправляем каждый тариф в отдельном сообщении с кнопкой "Подключить тариф"
    for tariff in tariffs:
        text = f"Тариф {tariff['name']}\n{tariff['description']}\nСтоимость: {tariff['price']}"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Подключить тариф", url="https://t.me/NoName_1101"))
        await message.answer(text, reply_markup=markup)

# Обработчик кнопки "МТС"
@dp.message_handler(lambda message: message.text == "МТС")
async def process_mts(message: types.Message):
    # Создаем список с тарифами МТС
    tariffs = [
        {"name": "Smart", "description": "500 минут, 30 ГБ интернета", "price": "500 рублей/месяц"},
        {"name": "Ultra", "description": "Безлимитные звонки, 50 ГБ интернета", "price": "800 рублей/месяц"},
        {"name": "Max", "description": "3000 минут, 100 ГБ интернета", "price": "1500 рублей/месяц"},
        {"name": "Lite", "description": "200 минут, 10 ГБ интернета", "price": "300 рублей/месяц"},
        {"name": "Super", "description": "1000 минут, 60 ГБ интернета", "price": "1000 рублей/месяц"}
    ]

    # Отправляем каждый тариф в отдельном сообщении с кнопкой "Подключить тариф"
    for tariff in tariffs:
        text = f"Тариф {tariff['name']}\n{tariff['description']}\nСтоимость: {tariff['price']}"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Подключить тариф", url="https://t.me/NoName_1101"))
        await message.answer(text, reply_markup=markup)

# обработчик кнопки "Мегафон"
@dp.message_handler(lambda message: message.text == "Мегафон")
async def process_mts(message: types.Message):
    # Создаем список с тарифами
    tariffs = [
        {"name": "#ДляДома Интернет", "description": "Домашний интернет 100 мбит/с\nРоутер 99р на 36 мес\n344р в месяц"},
        {"name": "#ДляДома Всё",
         "description": "Домашний интернет 100мбит/с\nИнтерактивное телевидение 180 каналов\nРоутер 99р на 36 мес\nПриставка 159 на 36 мес"},
        {"name": "#ДляДома Максимум",
         "description": "Домашний интернет 100мбит/с\nИнтерактивное телевидение 250 каналов\nРоутер 99р на 36 мес\nПриставка 159 на 36 мес\nЦена: 664р"},
        {"name": "#Объединяй! Два Интернета",
         "description": "Домашний интернет 100 мбит/с\nМобильная связь: 30 ГБ, 1000 минут\nРоутер 89р на 36 мес.\nЦена: 420р"},
        {"name": "#Объединяй! Хит",
         "description": "Домашний интернет 100 мбит/с\nИнтерактивное телевидение: 180 каналов\nМобильная связь: 30 ГБ, 1300 минут\nРоутер: 89р на 36 мес\nТв приставка: 149р на 36 мес.\nЦена: 350р"},
        {"name": "#Объединяй! Максимум",
         "description": "Домашний интернет 100 мбит/с\nИнтерактивное телевидение 180 каналов\nМобильная связь: 45 ГБ, 2000 минут\nРоутер аренда: 89р\nПриставка аренда: 109р\nЦена: 630р"}
    ]

    # Отправляем каждый тариф в отдельном сообщении с кнопкой "Подключить тариф"
    for tariff in tariffs:
        text = f"{tariff['name']}\n{tariff['description']}"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Подключить тариф", url="https://t.me/NoName_1101"))
        await message.answer(text, reply_markup=markup)

#Обработчик кнопки "Вернуться"
@dp.message_handler(lambda message: message.text == "Вернуться")
async def process_return(message: types.Message):
   markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
   markup.add(KeyboardButton("выбрать тариф"))
   markup.add(KeyboardButton("Информация"))
   markup.add(KeyboardButton("Связаться с нами"))
   await message.answer("Выберите провайдера:", reply_markup=markup)

# Обработчик всех остальных сообщений
@dp.message_handler()
async def unknown_message(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
    markup.add(KeyboardButton("выбрать тариф"))
    markup.add(KeyboardButton("Информация"))
    markup.add(KeyboardButton("Связаться с нами"))
    await message.answer("Упс 😬, кажется, я не понимаю ваш запрос. Для получения необходимой информации, пожалуйста, воспользуйтесь кнопками меню или свяжитесь с нашим специалистом по номеру 89205552222 ☎️. Они смогут помочь вам решить вашу проблему или ответить на ваши вопросы. Будьте уверены, что мы сделаем все возможное, чтобы помочь вам! 😊", reply_markup=markup)

# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


