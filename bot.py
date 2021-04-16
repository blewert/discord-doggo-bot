#
# @file   bot.py
# @author ben <bwilliams@lincoln.ac.uk>
# 


import os
import discord
from discord.ext import commands

from flickr import FlickrPhotosAPI

def get_token_from_file(filename):

    # No file? Die:
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Couldn't find {filename} (token for discord bot).");

    # File? cool, strip, return:
    with open(filename, 'r') as f:
        return f.readline().strip();
        

# Get tokens
bot_token = get_token_from_file(".token");
owner_id = get_token_from_file(".owner_id");
flickr_token = get_token_from_file(".flickr_api_key");

# Get flickr api search instance
flickr_api = FlickrPhotosAPI(flickr_token);

# Do a random search for something
flickr_api.random_search(["corgi", "dog"]);



# Make new client
bot = commands.Bot(command_prefix='!');

@bot.event
async def on_ready():
    print(f'{bot.user} connected! Token is <{bot_token}>');


@bot.command()
async def puppy(ctx):

    # They're a bot for some reason? Die
    if ctx.author.bot:
        return;

    # Otherwise! Do this
    return await ctx.send("hello");

@bot.command()
async def quit(ctx):

    # Not the owner? Get out of town
    if str(ctx.author.id) != owner_id:
        return await ctx.send("Nice try");

    # Otherwise:
    print("Quit command found! Closing!");
    await ctx.send("Leaving!");
    await ctx.bot.close();

# Run ittttttt
bot.run(bot_token);
