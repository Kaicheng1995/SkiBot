# import Constants as keys
# from telegram.ext import *
# import Responses as R
#
# print("SkiBot started...")
#
# def start_command(update):
#     update.message.reply_text("Type anything to get started")
#
# def help_command(update):
#     update.message.reply_text("If you need help please search on google")
#
# # handle the user message and give a reply
# def handle_message(update):
#     # receive the text form user
#     text = str(update.message.text).lower()
#     # process it
#     response = R.sample_responses(text)
#     # reply to user
#     update.message.reply_text(response)
#
# # logs the errors
# def error(update, context):
#     print(f"Update {update} caused error {context.error}")
#
#
# """
#     main function
# """
#
# def main():
#
#     updater = Updater(keys.API_KEY, use_context=True)
#     dp = updater.dispatcher
#
#     # instruction menu
#     dp.add_handler(CommandHandler("start", start_command))
#     dp.add_handler(CommandHandler("help", help_command))
#
#     # handle user message
#     dp.add_handler(MessageHandler(Filters.text, handle_message))
#
#     dp.add_error_handler(error)
#
#     # just to start??
#     updater.start_polling()
#     # keep active even if nothing happens
#     updater.idle()
#
#
# if __name__ == '__main__':
#     main()




from resort import Resort
from data_operation import set_operation
from data_weather import set_weather


# create 5 Resort objects
kirkwood = Resort("Kirkwood")
aspen = Resort("Aspen Snowmass")
crystal = Resort("Crystal Mountain")
gore = Resort("Gore Mountain")
heavenly = Resort("Heavenly")

# append all resorts objects to a list
Resorts = [kirkwood, aspen, crystal, gore, heavenly]


def get_realtime_data():
    set_weather()














