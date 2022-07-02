from discord.ext import commands
import sqlite3
import random

con = sqlite3.connect('./cogs/fight.db')
cur = con.cursor()


def options_list(topic):
    list_name = []
    for row in cur.execute('SELECT * FROM debate'):
        r = row
        if topic == r[0]:
            list_name.append(r[1])
        else:
            continue
    return list_name


class Debate(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name="fight")
    async def fight(self, ctx: commands.Context, arg, situation="in general"):
        options = options_list(arg)
        # situations = options_list('situation')
        option_a = "d"
        option_b = "d"
        while option_a == option_b:
            option_a = random.choice(options)
            option_b = random.choice(options)

        await ctx.send(f"Debate whether {option_a} or {option_b} is better {situation}")


def setup(bot):
    bot.add_cog(Debate(bot))
