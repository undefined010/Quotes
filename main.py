import requests
import json
import random
import pyautogui
import time
import webbrowser
from colorama import Fore

URL = 'https://type.fit/api/quotes'


def url_to_chat():
    # you must enter an url to the current chat
    link: str = input(Fore.RED + "enter  a url : ")
    req = requests.get(link)

    if req.status_code != 200:
        print(Fore.RED + f'server don\'t return 2xx code server code : {req.status_code}')
        input('press any key to exit...')
        exit()

    webbrowser.open(link)
    time.sleep(10)


def write_messages(arg: str):
    pyautogui.write(arg)
    pyautogui.press('enter')


def get_quotes():
    req = requests.get(URL)

    if req.status_code != 200:
        print('error')

    return json.loads(req.content)


if __name__ == '__main__':

    random_number: int = random.randint(0, 1643)
    quotes = '\'{}\'\n-{}'.format(get_quotes()[random_number]['text'], get_quotes()[random_number]['author'])
    print(Fore.BLUE + quotes + Fore.GREEN)
    confirm = str(input('Do you want to write this quote ? yes [y] , no [n] : '))

    if confirm == 'n':
        exit()

    elif confirm == 'y':
        url_to_chat()
        print('message will be type after 10 seconds')
        write_messages(quotes)
        exit()

    else:
        exit()
