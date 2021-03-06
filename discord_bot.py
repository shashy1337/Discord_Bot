from discord import Game
from discord.ext.commands import Bot
import requests
import random
import asyncio



bot_prefix = ('!')
TOKEN = ''

bot = Bot(command_prefix = bot_prefix)
same_extension = ['music']

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(name='btc')
async def bitoc():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()
    await bot.say('Курс лучшей валюты в $ по мнению Алеши Шевцова, составляет: ' + value['bpi']['USD']['rate'])

@bot.command(name='joke')
async def humoreska():
    def getjson(url, data):
        response = requests.get(url, params=data)
        print(response.url)
        response = response.json()
        return response

    access_token = ''
    owner_id = '-92876084'
    count = 100
    version = '5.92'
    filter = 'owner'

    wall = getjson('https://api.vk.com/method/wall.get',
                   {'owner_id': owner_id,
                    'access_token': access_token,
                    'count':count,
                    'filter': filter,
                    'v': version})

    try:
        clear_data_wall = wall['response']['items'].pop(random.randint(1, 100))['text']



        clear_text = [value for value in clear_data_wall if value !=['']]

        new_clear_text = ''.strip().join(clear_text)
        await bot.say(new_clear_text)
    except Exception as err:
        await bot.say('Нихуя нет брат, онли пустые значения' + err)

@bot.command(name='tashkent')
async def tashkent_weather():
    url = 'http://api.apixu.com/v1/current.json?key=14339221d0914c4aa32121507192003&q=Tashkent'
    response = requests.get(url)
    value = response.json()
    await bot.say(str('Погода в Ташкенте на данный момент: ') + str(value['current']['temp_c']) + str('°C'))


@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name='new ride crawl'))

@bot.command(name = 'infa')
async def infa() -> str:
    infa = ['3 на Б',
            '3 на А',
            '2 на Б',
            '2 на А',
            'Раш мид',
            'Раш Б!!11!1',
            'Раш А!!!!!11']
    await bot.say(random.choice(infa))

@bot.command(name = 'roll')
async def roll() -> int:
    await bot.say(random.randint(1, 100))


async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Подключенные каналы:")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)


try:
    for extension in same_extension:
        bot.load_extension(extension)
except Exception as e:
    exc = '{}, {}'.format(type(e).__name__, e)
    print('Ошибка загрузки расширений {} \n{}'.format(extension, exc))
bot.loop.create_task(list_servers())
bot.run(TOKEN)
