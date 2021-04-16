#
# @file   bot.py
# @author ben <bwilliams@lincoln.ac.uk>
# 


import os
import discord
import random
from discord.ext import commands

from flickr import FlickrPhotosAPI
from puppers import PuppersAPI

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

# Get puppy api
puppy_api = PuppersAPI(flickr_token);

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

    try:
        url = puppy_api.random_pupper();
        await ctx.send(url);

        # Choose a random rating unaffected by state, unique to photo
        state = random.getstate();
        random.seed(url);
        rating = random.randrange(11, 15);
        random.setstate(state);

        # Format into string
        rating_str = f"{rating}/10"

        # Format into a usable message and send it
        random_msg = puppy_api.random_rating(rating_str);
        await ctx.send(random_msg);
        
    
    except Exception as e:
        await ctx.send(puppy_api.random_error());
        await ctx.send(f"```\n{puppy_api.last_url}\n{puppy_api.last_response}\n```");


@bot.command()
async def quit(ctx):

    # Not the owner? Get out of town
    if str(ctx.author.id) != owner_id:
        return await ctx.send("Nice try");

    # Otherwise:
    print("Quit command found! Closing!");
    await ctx.send("Leaving :person_running:");
    await ctx.bot.close();

# Run ittttttt
bot.run(bot_token);
