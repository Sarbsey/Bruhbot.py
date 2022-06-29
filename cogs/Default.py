from discord.ext import commands
import discord


class Default(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print(f"{self.bot.user} has logged in!")

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(
            embed=discord.Embed(
                title="Ping",
                description=f"My ping is: {round(self.bot.latency * 100, 2)} ms"
            )
        )


def setup(bot):
    bot.add_cog(Default(bot))
