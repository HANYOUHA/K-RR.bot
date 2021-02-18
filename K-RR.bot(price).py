# import discord
# from discord.ext import commands
import time
import csv
import pandas as pd

f_path = "~/Documents/PriceLogger/price_list.csv"
last_row = pd.read_csv(f_path).iloc[-1]
for c in last_row:
    print(str(c))

'''
message = "현재 "+ last_row[0] +" RR 인게임 자원 가격은 다음과 같습니다.\n석유: "
                   + oil +"\n광물: " + ore + "\n우라늄: " + uranium + "\n다이아몬드: "
                   + diamonds + "\n헬륨: " + helium + "\n라이발륨: " + rivalium +
                   "\n탱크: " + tanks + "\n전투기: " + aircrafts + "\n미사일:" + missiles +
                   "\n폭격기: " + bombers + "\n드론: " + drones
client = commands.Bot(command_prefix='!')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 가격(ctx):
    await ctx.send()

client.run(디코봇 토큰)
'''