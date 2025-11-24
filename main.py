import discord
from discord.ext import commands, tasks
import json
import socket
import os


bot = commands.Bot(command_prefix='!',intents=discord.Intents.none())

# load channel id from json file
with open("data.json") as f: 
    channel_id = json.load(f)["channel_id"]




# get bot token from env variable
def get_token():
        token = os.getenv("Token")
        if token is None:
            print("Error reading env did you forget to add it in system variables?")
            exit()
        return token


# check if the minecraft server is online
def is_online(host="127.0.0.1", port=25565):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except:
        return False


# print when bot is ready
@bot.event
async def on_ready():
    infochannel = await bot.fetch_channel(channel_id)
    check_server_status.start()
    #await infochannel.send(f"Server status: {is_online()}")
    print(f'Logged in as {bot.user}!')

@tasks.loop(seconds=10)
async def check_server_status():
    online = is_online()
    status = discord.Status.online if online else discord.Status.dnd
    activity = discord.Game(("Online" if online else "Offline"))
    await bot.change_presence(status=status,activity=activity)
# run
bot.run(get_token())