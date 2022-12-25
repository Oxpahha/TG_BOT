from telegram import Update
from telegram.ext import CallbackContext
import config as config
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup
# import tic_tac_toe

com_list = ('Список доступных команд:\n'\
            '/info - показать список команд\n')

def logger(update: Update, context: CallbackContext):
    config.add_log(update.message.text,\
                update.message.from_user.id,\
                update.message.from_user.username,\
                update.message.from_user.first_name,\
                update.message.from_user.last_name)


def greetings(update: Update, context: CallbackContext):
    update.message.reply_text('Добрый день!')

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

def get_video(update: Update, context: CallbackContext):
    logger(update,context)
    pid = context.bot.getFile(update.message.video.file_id)
    pid.download()

def test_funk():
    return (com_list)


button_list = [
    InlineKeyboardButton("Кнопка", callback_data='Текст'),
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
    #context.bot.send_message(chat_id=update.message.chat_id, text="Меню", reply_markup=reply_markup)
    update.message.reply_text('Меню:', reply_markup=reply_markup)
    push(update)









#     # writing to a custom file
#     with open((f'./.files/{update.message.photo}.{config.datetime.now()}'), 'wb') as f:
#         context.bot.get_file(update.message.photo).download(out=f)

# else: data.message.reply_text(f'Что значит {msg}?')




# def greetings(update: Update, context: CallbackContext):
#     after_command = context.args
#     print(after_command)
#     update.message.reply_text('Добрый день!')    