#!/usr/bin/python3

# desenvolvido por preguiça de ficar pegando os valores de selects 

# Copyright (c) 2024 Carlos Alberto

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import requests as re
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from os import system

global url

textos_ascii = '''
 _____ _____ __ __ _____ _____ _____ _ 
|_   _|   __|  |  |_   _|     |   __|_|
  | | |   __|-   -| | | |  |  |__   |_ 
  |_| |_____|__|__| |_| |_____|_____|_|
'''

valores_ascii = '''
 _____ _____ __    _____ _____ _____ _____ _ 
|  |  |  _  |  |  |     | __  |   __|   __|_|
|  |  |     |  |__|  |  |    -|   __|__   |_ 
 \___/|__|__|_____|_____|__|__|_____|_____|_|
'''

parser = ArgumentParser()
parser.add_argument('--url', '-U', type=str, help='--url https://example.com')
url = parser.parse_args().url

class get_values:
    def __init__(self):
        system('clear')
        if not url:
            print("\n\033[31m[!] DIGITE UMA URL [!]\033[m\n")
            quit()

    def get_input_values(self):
        result = re.get(url).text
        result_bs4 = BeautifulSoup(result, 'html.parser')
        selects = result_bs4.find_all("select")
        print(f"\033[1;35m{textos_ascii}\033[m")
        for select in selects:
            options = select.find_all("option")
            value = ""
            for option in options:
                if (option.get('value') != None and option.get('value') != ""):
                    value+=f"{option.contents[0]} | "
            print(f"\033[7;35m{value.strip()[:-1]}\033[m")
        print("\n")
        print(f"\033[1;35m{valores_ascii}\033[m")
        for select in selects:
            options = select.find_all("option")
            value = ""
            for option in options:
                if (option.get('value') != None and option.get('value') != ""):
                    value+=f"{option.get('value')} | "
            print(f"\033[7;35m{value.strip()[:-1]}\033[m")
        print("\n")

if __name__ == '__main__':
    get_values().get_input_values()