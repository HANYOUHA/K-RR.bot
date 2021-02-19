import discord
from discord.ext import commands
import asyncio
import time
import csv
import pandas as pd

f_path = "~/Documents/PriceLogger/price_list.csv"
last_row = pd.read_csv(f_path).iloc[-1]

message = "현재 " + str(last_row[0]) + " RR 인게임 자원 가격은 다음과 같습니다.\n" \
                              "석유: " + str(last_row[1]) + "\n광물: " + str(last_row[2])

file = open('token.txt', 'r')

token = file.read()



print(message)
'''

oil = "{:,}".format(int(oil))
ore = "{:,}".format(int(ore))
uranium = "{:,}".format(int(uranium))
diamonds = "{:,}".format(int(diamonds))
helium = "{:,}".format(int(helium))
rivalium = "{:,}".format(int(rivalium))
tanks = "{:,}".format(int(tanks))
aircrafts = "{:,}".format(int(aircrafts))
missiles = "{:,}".format(int(missiles))
bombers = "{:,}".format(int(bombers))
drones = "{:,}".format(int(drones))


client = commands.Bot(command_prefix='!')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 가격(ctx):
    await ctx.send("현재 시각 "+ last_row[0] +" 자원 시세\n석유: " + str(last_row[1]) + "\n광물: " + str(last_row[2]) + "\n우라늄: " + str(last_row[3]) + "\n다이아몬드: " + str(last_row[4]) + "\n헬륨: " + str(last_row[5]) + "\n라이발륨: " + str(last_row[6]) + "\n탱크: " + str(last_row[7]) + "\n전투기: " + str(last_row[8]) + "\n미사일:" + str(last_row[9]) + "\n폭격기: " + str(last_row[10]) + "\n드론: " + str(last_row[11]))
    
@client.command()
async def 석유(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n" + str(last_row[1]))
    
@client.command()
async def 광물(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n" + str(last_row[2]))
    
@client.command()
async def 우라늄(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n" + str(last_row[3]))
    
@client.command()
async def 다이아몬드(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[4]))
    
@client.command()
async def 헬륨(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[5]))

    
@client.command()
async def 라이발륨(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(rlast_row[6]))
    
@client.command()
async def 탱크(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[7]))

    
@client.command()
async def 전투기(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[8]))

    
@client.command()
async def 미사일(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[9]))

    
    
@client.command()
async def 폭격기(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[10]))

    
@client.command()
async def 드론(ctx):
    await ctx.send("현재 시각 "+ last_row[0] + "\n"+ str(last_row[11]))

    
@client.command()
async def 도움말(ctx):
    await ctx.send("RR 실시간 자원 시세 알리미 봇무장관은 석유님의 데이터 베이스를 기반으로 하여 10분마다 자동 업데이트 되지만 서버 사정으로 업데이트가 지연될 수 있으니 양해바랍니다.\n불편하신 점이나 개선 사항은 석유님에게 DM바랍니다.\n명령어 모음: \n!가격: 전체 실시간 RR 인게임 자원 시세를 확인합니다.\n!석유:석유의 실시간 시세를 확인합니다.\n!광물: 광물의 실시간 시세를 확인합니다.\n!우라늄:우라늄의 실시간 시세를 확인합니다.\n!다이아몬드: 다이아몬드의 실시간 시세를 확인합니다.\n!헬륨: 헬륨의 실시간 시세를 확인합니다.\n!라이발륨:라이발륨의 실시간 시세를 확인합니다.\n!탱크: 탱크의 실시간 시세를 확인합니다.\n!전투기: 전투기의 실시간 시세를 확인합니다.\n미사일: 미사일의 실시간 시세를 확인합니다.\n!폭격기: 폭격기의 실시간 시세를 확인합니다.\n!드론: 드론의 실시간 시세를 확인합니다.\nMade By. RR 한국과학기술원")




client.run(token)
'''
