import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint

def parse_msg(chat_id, messageText):
    if messageText == 'start':
        elfibot0.sendMessage(chat_id, 'Command start received')
        return
    if messageText == 'stop':
        elfibot0.sendMessage(chat_id, 'Command stop received')
        return

    errorMsg = 'Unknown command received: ' + messageText
    print(errorMsg)
    elfibot0.sendMessage(chat_id, errorMsg)

def elfibot0_msg_handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        messageText = msg['text']
        parse_msg(chat_id, messageText)
        return

    errorMsg = 'Unknown content type: ' + content_type
    print(errorMsg)
    elfibot0.sendMessage(chat_id, errorMsg)

def elfibot0_main():
    global elfibot0
    global telegram_bot_token

    configFileName = '..\..\elfibot0.txt'

    try:
        with open(configFileName, 'r') as configFile:
            telegram_bot_token = configFile.read(45)
    except FileNotFoundError:
        print('Error: Could not open config file ' + configFileName)
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
