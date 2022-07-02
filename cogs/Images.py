from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup


def getdata(url):
    r = requests.get(url)
    return r.text


class PFP(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(name="pfp")
    async def pfp(self, ctx: commands.Context):
        await ctx.send(file=discord.File('./images/capybara.png'))

    @commands.command()
    async def showme(self, ctx: commands.Context):
        htmldata = getdata("https://a-z-animals.com/animals/")
        soup = BeautifulSoup(htmldata, 'html.parser')
        link_dict = []
        for link in soup.find_all('a'):
            image_link = link.get('href')
            image_link = str(image_link)
            if image_link.startswith('https://a-z-animals.com/animals/'):
                link_dict.append(image_link)
            else:
                pass
        print(link_dict)


def setup(bot):
    bot.add_cog(PFP(bot))
