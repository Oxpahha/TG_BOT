from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext import CallbackQueryHandler
import functions as f
import config



updater = Updater(config.read_token()[0])
dp = updater.dispatcher

config.log_init()
print('Bot starting')


start_hand = CommandHandler('start', f.greetings)
info_hand = CommandHandler('info', f.command_list)
calcl_hand = CommandHandler('calc', f.calc)

menu_hand = CommandHandler('menu', f.menu)
push_button = CallbackQueryHandler(f.push)

# calc_hand = CommandHandler('calc',f.getMessage)
# calc_push = CallbackQueryHandler(f.calc_func)

msg_hand = MessageHandler(Filters.text, f.get_msg)
photo_hand = MessageHandler(Filters.photo, f.get_photo)
video_hand = MessageHandler(Filters.video, f.get_video)



dp.add_handler(start_hand)
dp.add_handler(info_hand)
dp.add_handler(calcl_hand)

dp.add_handler(menu_hand)
dp.add_handler(push_button)

# dp.add_handler(calc_hand)
# dp.add_handler(calc_push)

dp.add_handler(msg_hand)
dp.add_handler(photo_hand)
dp.add_handler(video_hand)



updater.start_polling(poll_interval=0.5)
updater.idle()