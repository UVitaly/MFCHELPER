from datetime import timedelta
from telebot import types
from telebot.types import Message
import datetime as dt
import io

def main_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    itembtna = types.KeyboardButton('/register')
    itembtnv = types.KeyboardButton('/bookinglist')
    itembtnc = types.KeyboardButton('/withdraw')
    itembtnd = types.KeyboardButton('/help')
    itembtnq = types.KeyboardButton('Часто задаваемые вопросы')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd)
    markup.row(itembtnq)
    return markup


def date_keyboard():
    now = dt.datetime.now()
    dates = []
    itembtns = []
    itembtns.clear()
    markup = types.ReplyKeyboardMarkup(row_width=5,one_time_keyboard=True)


    for i in range(0,14):
        dates.append((now + timedelta(days=i)))


    for date in dates:
        itembtn = types.KeyboardButton(str(date.date().day)+'/'+str(date.date().month))
        itembtns.append(itembtn)
    

    markup.add(itembtns[0],itembtns[1],itembtns[2],itembtns[3],itembtns[4],
    itembtns[5],itembtns[6],itembtns[7],itembtns[8],itembtns[9],
    itembtns[10],itembtns[11],itembtns[12],itembtns[13])
    return markup


def time_keyboard():
    markup = types.ReplyKeyboardMarkup(row_width=6,one_time_keyboard=True)
    itembtns = []

    time_slots = ['8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30'
    ,'14:00','14:30','15:00','15:30','16:00','16:30']
    itembtns.clear()


    for time_slot in time_slots:
        itembtn = types.KeyboardButton(time_slot)
        itembtns.append(itembtn)


    markup.add(itembtns[0],itembtns[1],itembtns[2],itembtns[3],itembtns[4],
    itembtns[5],itembtns[6],itembtns[7],itembtns[8],itembtns[9],
    itembtns[10],itembtns[11],itembtns[12],itembtns[13],itembtns[14],
    itembtns[15],itembtns[16],itembtns[17])
    return markup

def questions_keyboard():
    markup = types.ReplyKeyboardMarkup()
    itemsbtns=[1000]
    questionsdat=io.open('questions.txt',encoding='utf-8', mode='r')
    i=0
    itemsbtns[0]=types.KeyboardButton('Назад')
    markup.row(itemsbtns[0])
    for line in questionsdat:
        itemsbtns[i]=types.KeyboardButton(line.split(":::")[0])
        markup.row(itemsbtns[i])
    i=0
    return markup


def remove_keyboard():
    markup = types.ReplyKeyboardRemove()
    return markup

