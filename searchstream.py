import os
import requests
from bs4 import BeautifulSoup
import lxml
import argparse

parser = argparse.ArgumentParser(
    description='Searching translation for AceMediaPlayer. Usage python searchstream.py -ch {name channel}')

parser.add_argument("channel")
args = parser.parse_args()

channel = args.channel
r = requests.get(f"https://acestreamsearch.net/?q={channel}")
src = r.text

soup = BeautifulSoup(src, "lxml")

all_links = soup.find_all(class_='list-group-item')

if len(all_links) == 0:
    print('Ничего не найдено')
    exit()

channels = {}
count = 0

for item in all_links:
    item_text = item.text
    item_link = item.find('a')['href']
    count += 1
    tmp = [item_text, item_link]
    ch = {count: tmp}
    channels.update(ch)

for key, value in channels.items():
    print(f"{key} : {value[0]}")

userinput = int(input('Введите номер канала:'))

print(f'Вы выбрали {channels[userinput][0]}, ссылка: {channels[userinput][1]}')

userinput2 = int(
    input('Желаете запустить трансляцию в плеере?\n 1 - Да \n 2 - Нет \n :'))

if userinput2 == 1:
    os.system(f'acestream-launcher -p mpv {channels[userinput][1]}')
else:
    os.system(f'echo {channels[userinput][1]} | xclip -sel clip')
    print('Ссылка скопирована в буфер обмена')
    exit()
