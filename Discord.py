import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
bot.remove_command("help")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
@bot.command()
async def test(ctx):
    await ctx.send(f"こんにちは。{ctx.author.mention}さん。私は有能なBotです。")
@bot.command()
async def time(ctx):
    now = datetime.now()
    current_time = now.strftime("%Y/%m/%d %H:%M:%S")
    await ctx.send(f"現在時刻: {current_time}")

bot.run("とーくん！")
# 僕が普通にgithubにトークンアップロードしてディスコード本部から連絡が来たことは、口が裂けても言えません^ - ^
