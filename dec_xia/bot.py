from discord.ext import commands
from data import checkdatabase, begdata, viewbank
import random
import discord
import json

bot = commands.Bot(command_prefix="!")

with open('bot_id.json', "r", encoding = "utf8") as datafile:
    jsondata = json.load(datafile)

        
@bot.event
async def on_ready():
    print("Bot in ready")

    
@bot.command()
async def hello(ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")
    
#check data and embed bank   
@bot.command()
async def check(ctx):
    await ctx.send("請稍等大約4秒鐘左右")
    re = checkdatabase(ctx.author, ctx.author.id)
    if re == False:
        await ctx.send("不在資料庫中，現在碼上創建")
    else:
        await ctx.send("已在資料庫中，正在讀取資料，請稍後")
        w, b = viewbank(ctx.author, ctx.author.id)
        em = discord.Embed(title = f"{ctx.author.name}'s 錢包", color = discord.Color.red())
        em.set_thumbnail(url = ctx.author.avatar_url)
        em.add_field(name = "Wallet", value = w)
        em.add_field(name = "Bank", value = b)
        await ctx.send(embed = em)
        

#beg monry
@bot.command()
async def beg(ctx):
    begnums = random.randint(1, 100)
    begdata(ctx.author, ctx.author.id, begnums)
    await ctx.send(f"你獲得了{begnums}$")

bot.run(jsondata['token']) 