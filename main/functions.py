from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
import config 





com_list = ('Список доступных команд:\n'\
            '/menu - показать список команд\n'\
            '/calc [x]?[y] - просто калькулятор')

def logger(update: Update, context: CallbackContext):
    config.add_log(update.message.text,\
                update.message.from_user.id,\
                update.message.from_user.username,\
                update.message.from_user.first_name,\
                update.message.from_user.last_name)


def greetings(update: Update, context: CallbackContext):
    update.message.reply_text(f'Добрый день!')
    update.message.reply_text(menu(update,context))

def command_list(update: Update, context: CallbackContext):
    update.message.reply_text(com_list)

def get_msg(update: Update, context: CallbackContext):
    logger(update,context)
    print(f'{config.current_time()} {update.message.text}')
    if 'время?' in update.message.text.lower():
        update.message.reply_text(config.current_time())

def get_photo(update: Update, context: CallbackContext):
    logger(update,context)
    pid = context.bot.getFile(update.message.photo[1])
    pid.download()
    update.message.reply_text('Nice!')

def get_video(update: Update, context: CallbackContext):
    logger(update,context)
    pid = context.bot.getFile(update.message.video.file_id)
    pid.download()
    update.message.reply_text('Wow! Video!')

def test_funk():
    return (com_list)


button_list = [
    InlineKeyboardButton("Посчитаем", callback_data=f'Пример: /calc 1+2'),
    InlineKeyboardButton("Время", callback_data=f'{config.current_time()}'),
    InlineKeyboardButton("Список команд", callback_data='3')]

def build_menu(buttons = button_list, n_cols=2,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def push(update: Update, _):
    query = update.callback_query
    variant = query.data
    query.answer()
    if variant == '3':
        query.edit_message_text(text=f"{com_list}")
    else: query.edit_message_text(text=f"{variant}")

reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))

def menu(update: Update, context: CallbackContext):
    # context.bot.send_message(chat_id=update.message.chat_id, text="Меню", reply_markup=reply_markup)
    update.message.reply_text('Меню:', reply_markup=reply_markup)
    push(update)
    
def operator(n_list):
    if '-' in n_list[0]:
        return '-'
    elif '+' in n_list[0]:
        return '+'
    elif '*' in n_list[0]:
        return '*'
    elif '/' in n_list[0]:
        return '/'

oper = ''

def calc(update: Update, context: CallbackContext):
    global oper 
    args = context.args

    if len(args) == 1:
        oper = operator(args)
    if len(args) > 1:
        args = [args[0]+args[1]+args[2]]
        oper = operator(args)
    str_sended = args
    args = str.split(args[0],f'{oper}')

    if oper == '+':
        update.message.reply_text(f'{str(str_sended[0])}={int(args[0])+int(args[1])}') 
    if oper == '-':
        update.message.reply_text(f'{str(str_sended[0])}={int(args[0])-int(args[1])}') 
    if oper == '*':
        update.message.reply_text(f'{str(str_sended[0])}={int(args[0])*int(args[1])}') 
    if oper == '/' :  
        update.message.reply_text(f'{str(str_sended[0])}={int(args[0])/int(args[1])}') 



# keyboard_list = [InlineKeyboardButton(' ', callback_data='no'),
#                 InlineKeyboardButton('C', callback_data='C'),
#                 InlineKeyboardButton('<=', callback_data='<='),
#                 InlineKeyboardButton('/', callback_data='/'),
#                 InlineKeyboardButton('7', callback_data='7'),
#                 InlineKeyboardButton('8', callback_data='8'),
#                 InlineKeyboardButton('9', callback_data='9'),
#                 InlineKeyboardButton('*', callback_data='*'),
#                 InlineKeyboardButton('4', callback_data='4'),
#                 InlineKeyboardButton('5', callback_data='5'),
#                 InlineKeyboardButton('6', callback_data='6'),
#                 InlineKeyboardButton('-', callback_data='-'),
#                 InlineKeyboardButton('1', callback_data='1'),
#                 InlineKeyboardButton('2', callback_data='2'),
#                 InlineKeyboardButton('3', callback_data='3'),
#                 InlineKeyboardButton('+', callback_data='+'),
#                 InlineKeyboardButton(' ', callback_data='no'),
#                 InlineKeyboardButton('0', callback_data='0'),
#                 InlineKeyboardButton(',', callback_data='.'),
#                 InlineKeyboardButton('=', callback_data='=')]

# value = ''
# old_value = ''
# reply_calc = InlineKeyboardMarkup(build_menu(keyboard_list, n_cols=4))

# def getMessage(update: Update, context: CallbackContext):
#     global value
#     value = context.args
#     if value == '':
#         update.message.reply_text('0', reply_markup=reply_calc)
#     else:
#         update.message.reply_text(value, reply_markup=reply_calc)
#     calc_func(update)    


# def calc_func(update: Update, context: CallbackContext):
#     global value, old_value
#     query = update.callback_query
#     data = query.data
#     if data == 'no':
#         pass
#     elif data == 'C':
#         value = ''
#     elif data == '<=':
#         if value != '':
#             value = value[:len(value)-1]
#     elif data == '=':
#         value = str(eval(value))
#     else:
#         value += data
#     if value != old_value:
#         if value == '':
#             context.bot.edit_message_text(
#                 chat_id=query.message.chat.id, message_id=query.message.from_user.id, text='0', reply_markup=reply_calc)
#         else:
#             context.bot.edit_message_text(chat_id=query.message.chat.id,
#                                   message_id=query.message.from_user.id, text=value, reply_markup=reply_calc)
#         old_value = value








#     # writing to a custom file
#     with open((f'./.files/{update.message.photo}.{config.datetime.now()}'), 'wb') as f:
#         context.bot.get_file(update.message.photo).download(out=f)

# else: data.message.reply_text(f'Что значит {msg}?')




# def greetings(update: Update, context: CallbackContext):
#     after_command = context.args
#     print(after_command)
#     update.message.reply_text('Добрый день!')    