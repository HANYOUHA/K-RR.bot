import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(크롬드라이버 경로)

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


time = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[2]").text

oil = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[3]").text

ore = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[4]").text

uranium = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[5]").text

diamonds = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[6]").text

helium = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[7]").text

rivalium = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[8]").text

tanks = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[9]").text

aircrafts = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[10]").text

missiles = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[11]").text

bombers = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[12]").text

drones = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[3]/div[2]/div[2]/table/tbody/tr[109]/td[13]").text

print(time)

print(oil)

print(ore)

    
client = commands.Bot(command_prefix='!')

@client.command()
async def 안녕(ctx):
    await ctx.send('안녕하세요')

@client.command()
async def 가격(ctx):
    await ctx.send("현재 "+ time +" RR 인게임 자원 가격은 다음과 같습니다.\n석유: " + oil +"\n광물: " + ore + "\n우라늄: " + uranium + "\n다이아몬드: " + diamonds + "\n헬륨: " + helium + "\n라이발륨: " + rivalium + "\n탱크: " + tanks + "\n전투기: " + aircrafts + "\n미사일:" + missiles + "\n폭격기: " + bombers + "\n드론: " + drones)




client.run(디코봇 토큰)
