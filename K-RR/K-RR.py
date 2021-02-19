import discord
from discord.ext import commands
import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

file = open('token.txt', 'r')

token = file.read()


driver = webdriver.Chrome('C:/Users/SH/Downloads/selenium/chromedriver.exe')

driver.get("https://github.com/TripleJBlog/PriceLogger/blob/master/price_list.csv")



SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

time.sleep(15)  

i = 130

while i < 9999:



   
    repr(i)

    print(i)


    time = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[2]").text

    oil = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[3]").text

    ore = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[4]").text

    uranium = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[5]").text

    diamonds = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[6]").text

    helium = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[7]").text

    rivalium = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[8]").text

    tanks = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[9]").text

    aircrafts = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[10]").text

    missiles = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[11]").text

    bombers = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[12]").text

    drones = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr["+ str(i) +"]/td[13]").text

    print(time)

    print(oil)

    print(ore)

    
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
    @commands.Cog.listener()
    async def on_ready(self):
        print('로그인: {0}({0.id})'.format(self.bot.user))
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('!도움말 입력'))

    @client.command()
    async def 안녕(ctx):
        await ctx.send('안녕하세요')

    @client.command()
    async def 가격(ctx):
        await ctx.send("현재 시각 "+ time +" 자원 시세\n석유: " + str(oil) + "\n광물: " + str(ore) + "\n우라늄: " + str(uranium) + "\n다이아몬드: " + str(diamonds) + "\n헬륨: " + str(helium) + "\n라이발륨: " + str(rivalium) + "\n탱크: " + str(tanks) + "\n전투기: " + str(aircrafts) + "\n미사일:" + str(missiles) + "\n폭격기: " + str(bombers) + "\n드론: " + str(drones))
    
    @client.command()
    async def 석유(ctx):
        await ctx.send("현재 시각 "+ time + "\n" + str(oil))
    
    @client.command()
    async def 광물(ctx):
        await ctx.send("현재 시각 "+ time + "\n" + str(ore))
    
    @client.command()
    async def 우라늄(ctx):
        await ctx.send("현재 시각 "+ time + "\n" + str(uranium))
    
    @client.command()
    async def 다이아몬드(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(diamonds))
    @client.command()
    async def 헬륨(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(helium))

    
    @client.command()
    async def 라이발륨(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(rivalium))
    
    @client.command()
    async def 탱크(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(tanks))

    
    @client.command()
    async def 전투기(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(aircrafts))

    
    @client.command()
    async def 미사일(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(missiles))

    
    
    @client.command()
    async def 폭격기(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(bombers))

    
    @client.command()
    async def 드론(ctx):
        await ctx.send("현재 시각 "+ time + "\n"+ str(drones))

    
    @client.command()
    async def 도움말(ctx):
        await ctx.send("RR 실시간 자원 시세 알리미 봇무장관은 석유님의 데이터 베이스를 기반으로 하여 10분마다 자동 업데이트 되지만 서버 사정으로 업데이트가 지연될 수 있으니 양해바랍니다.\n불편하신 점이나 개선 사항은 석유님에게 DM바랍니다.\n명령어 모음: \n!가격: 전체 실시간 RR 인게임 자원 시세를 확인합니다.\n!석유:석유의 실시간 시세를 확인합니다.\n!광물: 광물의 실시간 시세를 확인합니다.\n!우라늄:우라늄의 실시간 시세를 확인합니다.\n!다이아몬드: 다이아몬드의 실시간 시세를 확인합니다.\n!헬륨: 헬륨의 실시간 시세를 확인합니다.\n!라이발륨:라이발륨의 실시간 시세를 확인합니다.\n!탱크: 탱크의 실시간 시세를 확인합니다.\n!전투기: 전투기의 실시간 시세를 확인합니다.\n미사일: 미사일의 실시간 시세를 확인합니다.\n!폭격기: 폭격기의 실시간 시세를 확인합니다.\n!드론: 드론의 실시간 시세를 확인합니다.\nMade By. RR 한국과학기술원")

    







    client.run(token)

    time.sleep(int(600))

    int(i)

    i=i+1
    print(i)
    
    driver.refresh()
    time.sleep(int(5))
        # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


