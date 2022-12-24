from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import functions as f
import config as config


updater = Updater(config.read_token()[0])
dispetcher = updater.dispatcher
config.log_init()
print('Bot starting')


start_hand = CommandHandler('start', f.greetings)
info_hand = CommandHandler('info', f.command_list)
msg_hand = MessageHandler(Filters.text, f.get_msg)
photo_hand = MessageHandler(Filters.photo, f.get_photo)
video_hand = MessageHandler(Filters.video, f.get_video)


dispetcher.add_handler(start_hand)
dispetcher.add_handler(info_hand)
dispetcher.add_handler(msg_hand)
dispetcher.add_handler(photo_hand)
dispetcher.add_handler(video_hand)


updater.start_polling(poll_interval=0.5)
updater.idle()

