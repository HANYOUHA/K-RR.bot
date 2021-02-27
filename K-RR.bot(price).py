import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import csv
import pandas as pd

f_path = "~/Documents/PriceLogger/price_list.csv"
last_row = pd.read_csv(f_path).iloc[-1]
price_index = last_row.index[1:]
now = datetime.now()


def price(item):
    global now
    global last_row

    if datetime.now() > now + timedelta(minutes=10):
        last_row = pd.read_csv(f_path).iloc[-1]
        now = datetime.now()

    m = f"현재 시각 {last_row[0]}\n"
    if item == "가격":
        the_series = last_row[1:]
        for i, p in zip(price_index, the_series):
            m = m + f"{i} {p:,}\n"
    elif item == "oil":
        m = m + f"{last_row[item]:,}"
    elif item == "ore":
        m = m + f"{last_row[item]:,}"
    elif item == "uranium":
        m = m + f"{last_row[item]:,}"
    elif item == "diamonds":
        m = m + f"{last_row[item]:,}"
    elif item == "helium-3":
        m = m + f"{last_row[item]:,}"
    elif item == "rivalium":
        m = m + f"{last_row[item]:,}"
    elif item == "tanks":
        m = m + f"{last_row[item]:,}"
    elif item == "aircrafts":
        m = m + f"{last_row[item]:,}"
    elif item == "missiles":
        m = m + f"{last_row[item]:,}"
    elif item == "bombers":
        m = m + f"{last_row[item]:,}"
    elif item == "laser drones":
        m = m + f"{last_row[item]:,}"

    return m


app = commands.Bot(command_prefix='!')


@app.event
async def on_ready():
    print(f'다음으로 로그인합니다: {app.user.name}')
    print('connection was successful.')
    await app.change_presence(status=discord.Status.online, activity=None)


@app.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')


@app.command()
async def 가격(ctx):
    await ctx.send(price("가격"))


@app.command()
async def 석유(ctx):
    await ctx.send(price("oil"))


@app.command()
async def 광물(ctx):
    await ctx.send(price("ore"))


@app.command()
async def 우라늄(ctx):
    await ctx.send(price("uranium"))


@app.command()
async def 다이아몬드(ctx):
    await ctx.send(price("diamonds"))

@app.command()
async def 헬륨(ctx):
    await ctx.send(price("helium-3"))


@app.command()
async def 라이벌륨(ctx):
    await ctx.send(price("rivalium"))

@app.command()
async def 라이발륨(ctx):
    await ctx.send(price("rivalium"))


@app.command()
async def 탱크(ctx):
    await ctx.send(price("tanks"))


@app.command()
async def 전투기(ctx):
    await ctx.send(price("aircrafts"))


@app.command()
async def 미사일(ctx):
    await ctx.send(price("missiles"))


@app.command()
async def 폭격기(ctx):
    await ctx.send(price("bombers"))


@app.command()
async def 드론(ctx):
    await ctx.send(price("laser drones"))


@app.command()
async def 도움말(ctx):
    await ctx.send(
        "RR 실시간 자원 시세 알리미 봇무장관은 석유님의 데이터베이스를 기반으로 하여 10분마다 자동 업데이트 되지만 서버 사정으로 업데이트가 지연될 수 있으니 양해바랍니다.\n불편하신 점이나 개선 사항은 석유님에게 DM바랍니다.\n명령어 모음: \n!가격: 전체 실시간 RR 인게임 자원 시세를 확인합니다.\n!석유:석유의 실시간 시세를 확인합니다.\n!광물: 광물의 실시간 시세를 확인합니다.\n!우라늄:우라늄의 실시간 시세를 확인합니다.\n!다이아몬드: 다이아몬드의 실시간 시세를 확인합니다.\n!헬륨: 헬륨의 실시간 시세를 확인합니다.\n!라이발륨:라이발륨의 실시간 시세를 확인합니다.\n!탱크: 탱크의 실시간 시세를 확인합니다.\n!전투기: 전투기의 실시간 시세를 확인합니다.\n!미사일: 미사일의 실시간 시세를 확인합니다.\n!폭격기: 폭격기의 실시간 시세를 확인합니다.\n!드론: 드론의 실시간 시세를 확인합니다.\nMade By. RR 한국과학기술원")


file = open('../token.txt', 'r')
token = file.read()
app.run(token)
