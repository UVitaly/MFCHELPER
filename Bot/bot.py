from typing import Text
import telebot
import time
import firestore_service
from booking import Booking
from firestore_service import booking_list
import keyboard
import io
# import methods

import emoji
from credentials import TOKEN
import datetime as dt
questions={}
for line in io.open('questions.txt',encoding='utf-8'):
    linea=line.split(":::")
    questions[linea[0]]=linea[1].replace('%'+'%'+'%','\n')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(chat_id=message.chat.id,
        text='Добро пожалоать в MFHelper.\nЧтобы оставить заявку нажмите /register.',
        reply_markup=keyboard.main_keyboard()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Что-то не так, попробуйте еще раз.'
        )

@bot.message_handler(commands=['register'])
def register(message):
    date = ''
    try:
        new_booking = Booking()
        
        def get_name(message):
            try:
                check_input(message.text)
                new_booking.name = message.text
                bot.send_message(chat_id=message.chat.id, text='Пожалуйста введите ваш номер телефона.')
                bot.register_next_step_handler(message,get_phonenumber)
            except:
                bot.send_message(chat_id=message.chat.id, text='Что-то не так, попробуйте еще раз.',reply_markup=keyboard.remove_keyboard())

        def get_phonenumber(message):
            try:
                check_input(message.text)
                new_booking.phone_number = message.text
                bot.send_message(chat_id=message.chat.id, text='Пожалуйста введите ваш адрес проживания.')
                bot.register_next_step_handler(message,get_petname)
            except:
                bot.send_message(chat_id=message.chat.id, text='Что-то не так, попробуйте еще раз.',reply_markup=keyboard.remove_keyboard())

        def get_petname(message):
            try:
                check_input(message.text)
                new_booking.pet_name = message.text
                bot.send_message(chat_id=message.chat.id, 
                text='Пожалуйста, выберите дату.',
                reply_markup=keyboard.date_keyboard()
                )
                bot.register_next_step_handler(message,get_date)
            except:
                bot.send_message(chat_id=message.chat.id, text='Что-то не так, попробуйте еще раз.',reply_markup=keyboard.remove_keyboard())

        def get_date(message):
            try:
                check_input(message.text)
                nonlocal date
                date = message.text
                bot.send_message(chat_id=message.chat.id,text='Пожалуйста, выберите временной интервал.',reply_markup=keyboard.time_keyboard())
                bot.register_next_step_handler(message,get_time)
            except:
                bot.send_message(chat_id=message.chat.id, text='Что-то не так, попробуйте еще раз.',reply_markup=keyboard.remove_keyboard())

        def get_time(message):
            try:
                check_input(message.text)
                hour = message.text
                converted_time = convert_string_to_datetime(date,hour)
                exist = False
                same_time = 0
                for booking in booking_list:
                    if booking.user_id==message.from_user.id:
                        exist = True
                        break
                    if booking.time_slot == converted_time.timestamp():
                        same_time +=1
                if not exist:
                    if(same_time < 3):
                        new_booking.time_slot = int(converted_time.timestamp())
                        new_booking.user_id = message.from_user.id
                        firestore_service.add_booking(new_booking)
                        bot.send_message(chat_id=message.chat.id, text='Регистрация прошла успешна.',reply_markup=keyboard.main_keyboard())
                    else:
                        bot.send_message(chat_id=message.chat.id, text='Резервирование на это время заполнено. пожалуйста, попробуйте в другой раз.',reply_markup=keyboard.main_keyboard())
                else:
                    bot.send_message(chat_id=message.chat.id, text='Регистрация не удалась. Вы уже сделали заявку.',reply_markup=keyboard.main_keyboard())
            except:
                bot.send_message(chat_id=message.chat.id, text='Что-то не так, попробуйте еще раз.',reply_markup=keyboard.main_keyboard())

        bot.send_message(chat_id=message.chat.id, text='Пожалуйста, введите ваше ФИО.')
        bot.register_next_step_handler(message,get_name)
        
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Что-то не так, попробуйте еще раз.'
        )

@bot.message_handler(commands=['bookinglist'])
def send_booking_list(message):
    try:
        delete_past_booking()
        bot.send_message(chat_id=message.chat.id,text=firestore_service.display,
        reply_markup=keyboard.main_keyboard())
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Что-то не так, попробуйте еще раз.',
        reply_markup=keyboard.main_keyboard()
        )

@bot.message_handler(commands=['withdraw'])
def send_Message(message):
    try:
        can_delete = firestore_service.delete_booking_by_userid(message.from_user.id)
        if can_delete:
            bot.send_message(chat_id=message.chat.id, text='Бронирование успешно удалено.',
            reply_markup=keyboard.main_keyboard())
        else:
            bot.send_message(chat_id=message.chat.id, text='С вашей учетной записью не связано ни одного бронирования.',
            reply_markup=keyboard.main_keyboard())
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Что-то не так, попробуйте еще раз.',
        reply_markup=keyboard.main_keyboard()
        )

@bot.message_handler(commands=['help'])
def send_help(message):
    try:
        bot.send_message(chat_id=message.chat.id,text=
        '''
    Руководство по использованию бота.\n
чтобы создать заявку, нажмите /register
чтобы проверить список заявлений, нажмите  /bookinglist
для проверки статуса, нажмите /withdraw
        ''',
        reply_markup=keyboard.main_keyboard()
        )
    except:
        bot.send_message(chat_id=message.chat.id,
        text='Что-то не так, попробуйте еще раз.',
        reply_markup=keyboard.main_keyboard()
            )  

def check_input(text):
    #check if emoji
    if(text=='' or text[0][:1]=='/' or bool(emoji.get_emoji_regexp().search(text))):
        print('raising')
        raise Exception

def delete_past_booking():
    time_now = dt.datetime.now()
    for booking in booking_list:
        if booking.datetime < time_now:
            firestore_service.delete_booking_by_documentid(booking.id)


def convert_string_to_datetime(date,hour):
    time_now = dt.datetime.now()       
    year = ''
    prob_date = dt.datetime.strptime(date+'/'+str(time_now.year),r'%d/%m/%Y')
    if(prob_date<time_now):
        year = str(time_now.year+1)
    else:
        year = str(time_now.year)
    date += '/'+ str(year)
    time = date + ' ' + hour
    converted_time = dt.datetime.strptime(time,r'%d/%m/%Y %H:%M')
    return converted_time

@bot.message_handler(content_types=['text'])
def usualuqns(message):
    if message.text=="Часто задаваемые вопросы":
        bot.send_message(chat_id=message.chat.id,text="Выберите интересующий Вас вопрос",reply_markup=keyboard.questions_keyboard())
    elif message.text=="Назад":
        bot.send_message(chat_id=message.chat.id,text="Возвращаемся назад",reply_markup=keyboard.main_keyboard())
    else:
        try:
            bot.send_message(chat_id=message.chat.id,text=questions[message.text],reply_markup=keyboard.questions_keyboard())
        except:
            bot.send_message(chat_id=message.chat.id,text='Мы вас не понимаем, выберите необходимое Вам действие!',reply_markup=keyboard.questions_keyboard())

while True:
    bot.polling(none_stop=False)
    print('crash')
    time.sleep(1)