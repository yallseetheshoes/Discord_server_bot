import discord
from discord.ext import commands
import socket

bot = commands.Bot()

def is_online(host="127.0.0.1", port=25565):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except:
        return False

bot.run("YOUR_BOT_TOKEN")