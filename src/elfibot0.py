import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

def elfibot0_msg_handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        elfibot0.sendMessage(chat_id, msg['text'])

def elfibot0_main():
    global elfibot0
    global telegram_bot_token

    try:
        with open("..\..\elfibot0.txt", "r") as configFile:
            telegram_bot_token = configFile.read(45)
    except FileNotFoundError:
        print("Error: Could not open config file")
        return

    print(telegram_bot_token);
    elfibot0 = telepot.Bot(telegram_bot_token)

    elfibot0_Info = elfibot0.getMe()
    pprint(elfibot0_Info)

    MessageLoop(elfibot0, elfibot0_msg_handler).run_as_thread()

    while 1:
        time.sleep(10)

if __name__ == '__main__':
    elfibot0_main()
