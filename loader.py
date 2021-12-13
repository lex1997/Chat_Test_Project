import telebot
from telebot import types
from machine_of_states import TG_Chat_Bot

TOKEN = '5091123162:AAHBysF8mVfpg-Nry8ufd-bFGks0RK-CnXM'


bot = telebot.TeleBot(TOKEN)
TG_bot = TG_Chat_Bot()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Здравствуйте!')


@bot.message_handler(func=lambda m: True)
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, 'Вы хотите пиццу?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    Type_of_Pizza = ''
    Type_of_Payment = ''
    if TG_bot.state == 'asleep':
        if call.data == 'yes':
            TG_bot.customer_reported_order()
            keyboard = types.InlineKeyboardMarkup()
            key_big = types.InlineKeyboardButton(text='Большую', callback_data='big')
            keyboard.add(key_big)
            key_small = types.InlineKeyboardButton(text='Маленькую', callback_data='small')
            keyboard.add(key_small)
            bot.send_message(call.from_user.id, 'Какую вы хотите пиццу? Большую или маленькую?', reply_markup=keyboard)
        elif call.data == 'no':
            TG_bot.stop()
            bot.send_message(call.from_user.id, 'Ну тогда всего хорошего!)')


    elif TG_bot.state == 'accept an order':

        TG_bot.get_type_of_pizza(call.data)
        TG_bot.customer_has_chosen_the_form_of_payment()
        keyboard = types.InlineKeyboardMarkup()
        key_cash = types.InlineKeyboardButton(text='Наличкой', callback_data='cash')
        keyboard.add(key_cash)
        key_card = types.InlineKeyboardButton(text='Картой', callback_data='card')
        keyboard.add(key_card)
        bot.send_message(call.from_user.id, 'Как вы будете платить? Наличкой или картой?', reply_markup=keyboard)

    elif TG_bot.state == 'payment selection':

        TG_bot.get_type_of_payment(call.data)
        TG_bot.get_type_of_payment(call.data)
        TG_bot.summarized_the_order()

        if TG_bot.type_of_pizza == 'big':
            Type_of_Pizza = 'большую'
        elif TG_bot.type_of_pizza == 'small':
            Type_of_Pizza = 'маленькую'

        if TG_bot.type_of_payment == 'cash':
            Type_of_Payment = 'наличкой'
        elif TG_bot.type_of_payment == 'card':
            Type_of_Payment = 'картой'

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        answer = f'Вы хотите {Type_of_Pizza} пиццу, оплата - {Type_of_Payment}?'
        bot.send_message(call.from_user.id, answer, reply_markup=keyboard)

    elif TG_bot.state == 'order summary':

        if call.data == 'yes':
            bot.send_message(call.from_user.id, 'Спасибо за заказ')
            TG_bot.stop()
        elif call.data == 'no':
            TG_bot.stop()

    else:
        TG_bot.stop()


bot.polling()
