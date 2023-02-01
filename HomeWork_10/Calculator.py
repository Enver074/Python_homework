import telebot
from telebot import types
import time


bot = telebot.TeleBot("6000531795:AAFlbWGFbFuzqWixG116H0IIZw1lKgmvd_0")

typeNums = 0

@bot.message_handler(commands = ["start"])
def calc(message):
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton("Рациональные")
    key2 = types.KeyboardButton("Комплексные")
    mrk.add(key1, key2)
    bot.send_message(message.chat.id, f"Калькулятор", reply_markup=mrk)
    

@bot.message_handler(content_types="text")
def buttons(message):
    global typeNums
    if message.text == "Рациональные":
        bot.send_message(message.chat.id, f'Выбран режим рациональных чисел')
        bot.send_message(message.chat.id, f'Введите выражения разделяя пробелом')
        bot.register_next_step_handler(message, controller)
        typeNums = 0
    elif message.text == "Комплексные":
        bot.send_message(message.chat.id, f'Выбран режим комплексных чисел')
        bot.send_message(message.chat.id, f'Введите выражения разделяя пробелом')
        bot.register_next_step_handler(message, controller)
        typeNums = 1
        
        
def controller(message):
    line = message.text.split()
    znak = line[1]
    a = line[0]
    b = line[2]
    
    if typeNums == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])
    
    if znak == "+":
        res = summ_nums(a, b)
    elif znak == "-":
        res = sub_nums(a, b)
    elif znak == "*":
        res = mult_nums(a, b)   
    elif znak == "/":
        res = div_nums(a, b)
    elif typeNums == 1 and (znak == "//" or znak == "%"):
        bot.send_message(message.chat.id, f"Не верное выражение, повторите ввод выражения")
        bot.register_next_step_handler(message, controller)
    elif znak == "//":
        res = div_int(a, b)   
    elif znak == "%":
        res = div_rem(a, b)
    
    calc_log(message, res)   
    bot.send_message(message.chat.id, str(res))
    bot.register_next_step_handler(message, controller)
    
def calc_log(message, res):
    global typeNums
    time_calc = time.ctime()
    file = open('HomeWork_10\\log.csv', 'a', encoding='utf-8')
    if typeNums == 0:
        a = "Рациональные"
    else:
        a = "Комплексные"
    file.write(f'{time_calc} | {message.chat.first_name } | {a} : {message.text} = {res}\n')
        
           
def summ_nums(a,b):
    return a+b

def sub_nums(a,b):
    return a-b

def mult_nums(a,b):
    return a*b

def div_nums(a,b):
    return a/b

def div_int(a,b):
    return a//b

def div_rem(a,b):
    return a%b

bot.infinity_polling()