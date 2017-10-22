import telepot
from pprint import pprint

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

if __name__ == '__main__':
    elfibot0_main()
