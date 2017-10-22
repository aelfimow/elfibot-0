import telepot
from pprint import pprint

def elfibot0_main():
    global elfibot0

    elfibot0 = telepot.Bot('')

    elfibot0_Info = elfibot0.getMe()
    pprint(elfibot0_Info)

if __name__ == '__main__':
    elfibot0_main()
