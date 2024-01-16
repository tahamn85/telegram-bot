import telebot
from telebot import types
bot = telebot.TeleBot("6328836533:AAF298_ADP4AnABhWXPxPp1xK41Hq_PWLAg")

commands = ["start" , "help" , "clear" , ]

@bot.message_handler(commands=[commands[1]])
def send_welcome(message):
	bot.reply_to(message, ". چطور میتوانیم کمکتون کنم.")


@bot.message_handler(commands=[commands[0]])
	
def send_menu(message):
    
    bot.reply_to(message, "سلام\n چطور میتوانیم کمکتون کنم.")
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    button1 = types.InlineKeyboardButton(text='اطلاعات کاربرهای چنل', callback_data='comfig_users_in_chanel')
    button2 = types.InlineKeyboardButton(text='داخل چنل چیکار میکنیم و چه اتفاقی میفتد', callback_data='config')
    button3 = types.InlineKeyboardButton(text='درج اطلاعات خود', callback_data='add-id')

    keyboard.add(button1, button2, button3)
    

    bot.send_message(chat_id=message.chat.id, text='ایا شما دنبال این موارد هستید.', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.callback_data == 'comfig_users_in_chanel':
        bot.send_message(chat_id=call.message.chat.id, text='شما گزینه 1 را انتخاب کردید.')
    elif call.callback_data == 'config':
        bot.send_message(chat_id=call.message.chat.id, text='شما گزینه 2 را انتخاب کردید.')
    elif call.callback_data == 'add-id':
        bot.send_message(chat_id=call.message.chat.id, text='شما گزینه 3 را انتخاب کردید.')


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = respond_to_message(message)
    bot.reply_to(message, response)
    
@bot.message_handler(commands=[commands[2]])
def clear_chat(message):

    chat_id = message.chat.id

    last_message_date = message.date

    messages = bot.get_chat_history(chat_id, limit=1000000)

    for msg in messages:
        if msg.date < last_message_date:
            bot.delete_message(chat_id, msg.message_id)

    bot.reply_to(message, "چت با موفقیت پاک شد.")
    
def respond_to_message(message):
    text = message.text.lower()
    
    if('hi' or 'hello' in text):
        response = "سلام\nامیدوارم حالتون خوب باشه ."
    elif('سلام' in text):
        response = "سلام\nامیدوارم حالتون خوب باشه ."
    elif():
        response = ""
    return response

bot.infinity_polling()






