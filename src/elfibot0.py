import socket
import time
import telepot

from telepot.loop import MessageLoop
from pprint import pprint

def send_cmd(cmd):
    host = 'localhost'
    port = 50000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(cmd)

def parse_msg(chat_id, messageText):
    timeStamp = time.asctime(time.localtime())
    if messageText == 'start':
        responseText = timeStamp + ': Command start received'
        result = ''
        try:
            send_cmd(b'start')
        except:
            result = '(result: error)'
        elfibot0.sendMessage(chat_id, responseText + ' ' + result)
        return
    if messageText == 'stop':
        responseText = timeStamp + ': Command stop received'
        result = ''
        try:
            send_cmd(b'stop')
        except:
            result = '(result: error)'
        elfibot0.sendMessage(chat_id, responseText + ' ' + result)
        return

    errorMsg = timeStamp + ': Unknown command received: ' + messageText
    print(errorMsg)
    elfibot0.sendMessage(chat_id, errorMsg)

def elfibot0_msg_handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        messageText = msg['text']
        parse_msg(chat_id, messageText)
        return

    timeStamp = time.asctime(time.localtime())
    errorMsg = timeStamp + ': Unknown content type: ' + content_type
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
