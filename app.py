import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Le bot est en ligne : {bot.user}")

@bot.tree.command(name="ping", description="Latence du bot")
async def bonjour(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"Latence du bot : {latency}ms")

bot.run("LE-TOKEN") 
