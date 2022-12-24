from telegram import Update
from telegram.ext import CallbackContext
import config as config



def logger(update: Update, context: CallbackContext):
    config.add_log(update.message.text,\
                update.message.from_user.id,\
                update.message.from_user.username,\
                update.message.from_user.first_name,\
                update.message.from_user.last_name)


def greetings(update: Update, context: CallbackContext):
    update.message.reply_text('Добрый день!')

def command_list(update: Update, context: CallbackContext):
    update.message.reply_text('Список доступных команд:\n'\
                              '/info - показать список команд\n')

def get_msg(update: Update, context: CallbackContext):
    logger(update,context)
    print(f'{config.current_time()} {update.message.text}')
    if 'сколько время?' in update.message.text.lower():
        update.message.reply_text(config.current_time())

def get_photo(update: Update, context: CallbackContext):
    logger(update,context)
    pid = context.bot.getFile(update.message.photo[1])
    pid.download()

def get_video(update: Update, context: CallbackContext):
    logger(update,context)
    pid = context.bot.getFile(update.message.video.file_id)
    pid.download()
    
# def downloader(update: Update, context: CallbackContext):
#     context.bot.get_file(update.message.photo).download()

#     # writing to a custom file
#     with open((f'./.files/{update.message.photo}.{config.datetime.now()}'), 'wb') as f:
#         context.bot.get_file(update.message.photo).download(out=f)

# else: data.message.reply_text(f'Что значит {msg}?')




# def greetings(update: Update, context: CallbackContext):
#     after_command = context.args
#     print(after_command)
#     update.message.reply_text('Добрый день!')    