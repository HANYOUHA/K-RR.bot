# import discord
# from discord.ext import commands
import time
import csv
import pandas as pd

f_path = "~/Documents/PriceLogger/price_list.csv"
last_row = pd.read_csv(f_path).iloc[-1]

message = "현재 " + str(last_row[0]) + " RR 인게임 자원 가격은 다음과 같습니다.\n" \
                              "석유: " + str(last_row[1]) + "\n광물: " + str(last_row[2])

print(message)
'''
client = commands.Bot(command_prefix='!')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 가격(ctx):
    await ctx.send()

client.run(디코봇 토큰)
'''