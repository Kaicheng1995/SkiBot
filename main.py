import Constants as keys
from telegram.ext import *
import Responses as R

print("SkiBot started...")

def start_command(update, context):
    update.message.reply_text("Type anything to get started")

def help_command(update, context):
    update.message.reply_text("Here are the instructions:" + "\n" * 3
                              + "#1 Get started:" + "\n"
                              + "—————————" + "\n"
                              + '"Hi" / "hello" / "hola" / "hey" / ...' + "\n" * 3
                              + "#2 Ask for recommendation:" + "\n"
                              + "——————————————" + "\n"
                              + '"go skiing" / "ski resorts" / '
                                '"Can you recommend to me some ski resorts" / '
                                '"I want to go skiing" / ...' + "\n" * 3
                              + "#3 Query feature in a resort:" + "\n"
                              + "——————————————" + "\n"
                              + '"What is the [feature] in [resort]"' + "\n" * 3
                              + "#4 Query weather feature on a day:" + "\n"
                              + "——————————————————" + "\n"
                              + '"What is the [weather feature] in [resort] on [day]" /\n'
                                '"I wanna go to [resort] on [day]" / \n'
                                '"I wanna go to [resort] after [number] days"' + "\n" * 3
                              + "# Hints:" + "\n"
                              + 'You may also use "Can you tell me" or "Show me" to substitute "What is".'
                                ' Or you can just delete the prefix "What is". You can only the query weather '
                                'feature at most in the future five days from now on. The date format should be like '
                                '12/15/2021. You can also just type the resort name to query basic info.' + "\n" * 3
                              + "[weather feature]:" + "\n"
                              + "******************" + "\n"
                              + "[snowfall], [rainfall], [visibility], [temperature]" + "\n" * 3
                              + "Other [feature]:" + "\n"
                              + "******************" + "\n"
                              + "[ticket price], [open date], [close date], [number of lifts], [rating]" + "\n" * 3
                              + 'Type "bye" or "goodbye" to quit')

# handle the user message and give a reply
def handle_message(update, context):
    # receive the text from user
    text = str(update.message.text).lower()
    # able to handle multiple return value
    return_value = R.sample_responses(text)
    for response in return_value:
        update.message.reply_text(response)

# logs the errors
def error(update, context):
    print(f"Update {update} caused error {context.error}")


"""
    main function
"""

def main():

    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # instruction menu
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    # handle user message
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    # just to start??
    updater.start_polling()
    # keep active even if nothing happens
    updater.idle()


if __name__ == '__main__':
    main()
