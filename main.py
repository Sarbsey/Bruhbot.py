from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ['DISCORD_TOKEN']

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("b!"),
    description="sucks dick"
)


cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("./cogs/") if filename.endswith(".py")
]
for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)

bot.run(token)
