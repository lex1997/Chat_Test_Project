import telebot
from telebot import types
from machine_of_states import TG_Chat_Bot

TOKEN = '5091123162:AAHBysF8mVfpg-Nry8ufd-bFGks0RK-CnXM'



bot = telebot.TeleBot(TOKEN)
TG_bot = TG_Chat_Bot()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Какую вы хотите пиццу? Большую или маленькую?')

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
            bot.send_message(call.from_user.id, 'Ну тогда всего хорошего!)')

    elif TG_bot.state == 'accept an order':
        if call.data == 'big':

            TG_bot.get_type_of_pizza(call.data)
            TG_bot.customer_has_chosen_the_form_of_payment()
            keyboard = types.InlineKeyboardMarkup()
            key_cash = types.InlineKeyboardButton(text='Наличкой', callback_data='b.cash')
            keyboard.add(key_cash)
            key_card = types.InlineKeyboardButton(text='Картой', callback_data='b.card')
            keyboard.add(key_card)
            bot.send_message(call.from_user.id, 'Как вы будете платить? Наличкой или картой?', reply_markup=keyboard)
        elif call.data == 'small':

            TG_bot.get_type_of_pizza(call.data)
            TG_bot.customer_has_chosen_the_form_of_payment()
            keyboard = types.InlineKeyboardMarkup()
            key_cash = types.InlineKeyboardButton(text='Наличкой', callback_data='s.cash')
            keyboard.add(key_cash)
            key_card = types.InlineKeyboardButton(text='Картой', callback_data='s.card')
            keyboard.add(key_card)
            bot.send_message(call.from_user.id, 'Как вы будете платить? Наличкой или картой?', reply_markup=keyboard)

    elif TG_bot.state == 'payment selection':
        # if call.data == 'b.cash':
        #     Type_of_Payment = 'наличкой'
        #     Type_of_Pizza = 'большую'
        # elif call.data == 'b.card':
        #     Type_of_Payment = 'картой'
        #     Type_of_Pizza = 'большую'
        # elif call.data == 's.cash':
        #     Type_of_Payment = 'наличкой'
        #     Type_of_Pizza = 'маленькую'
        # elif call.data == 's.card':
        #     Type_of_Payment = 'картой'
        #     Type_of_Pizza = 'большую'
        TG_bot.get_type_of_payment(call.data)
        TG_bot.summarized_the_order()

        keyboard = types.InlineKeyboardMarkup()
        key_cash = types.InlineKeyboardButton(text='Наличкой', callback_data='cash')
        keyboard.add(key_cash)
        key_card = types.InlineKeyboardButton(text='Картой', callback_data='card')
        keyboard.add(key_card)
        bot.send_message(call.from_user.id, f'Вы хотите {TG_bot.type_of_pizza} пиццу, оплата - {TG_bot.type_of_payment}?', reply_markup=keyboard)

        # bot.register_next_step_handler(call, accept_an_order)
    # elif TG_bot.states == 'accept an order':
    # elif TG_bot.states == 'payment selection':
    # elif TG_bot.states == 'order summary':

bot.polling()








