#
# @file   bot.py
# @brief  Main entry point for the bot.
# @author ben <bwilliams@lincoln.ac.uk>
# 

import os
import discord
import random
from discord.ext import commands
# --
import util
from flickr import FlickrPhotosAPI
from puppers import PuppersAPI     


# Get tokens
bot_token     = util.get_token_from_file("auth/.token");
owner_id      = util.get_token_from_file("auth/.owner_id");
flickr_token  = util.get_token_from_file("auth/.flickr_api_key");

# Get puppy api
puppy_api = PuppersAPI(flickr_token);

# Make new client
bot = commands.Bot(command_prefix='!');


@bot.event
async def on_ready() -> None:
    print(f'{bot.user} connected! Token is <{bot_token}>');


@bot.command()
async def puppies(ctx, arg=None) -> None:

    # No arguments? Show error
    if arg == None:
        return await ctx.send(f"You gotta give me a number! Like: `!puppies 3`. The number must between 1 and 5 ok?");

    # Nae numeric? Error message ok
    if not arg.isnumeric():
        return await ctx.send(f"Sorry but `{arg}` doesn't look like a number to me. Pls give me a number between 1 and 5.");

    # Parse num, clamp to valid range
    num = int(arg);
    num = max(1, min(num, 5))

    # Run that many times, call puppy
    for i in range(0, num):
        await puppy(ctx);


@bot.command()
async def puppy(ctx) -> None:

    # They're a bot for some reason? Die
    if ctx.author.bot:
        return;

    try:
        # Get a random photo url
        url = puppy_api.random_pupper();

        # Choose a random rating unaffected by state, unique to photo
        state = random.getstate();
        random.seed(url);
        rating = random.randrange(11, 15);
        random.setstate(state);

        # Format into string
        rating_str = f"{rating}/10"

        # Format into a usable message and send it
        random_msg = puppy_api.random_rating(rating_str);

        # Make a new embed, set fields, set image
        e = discord.Embed(title=rating_str, description=random_msg);
        e.set_image(url=url);

        # And send the embed
        await ctx.send(embed=e);
        
    
    except Exception as e:

        # Otherwise.. an error
        await ctx.send(puppy_api.random_error());
        await ctx.send(util.markdown_code_teletype(f"{puppy_api.last_url}\n{puppy_api.last_response[:200]}"));


@bot.command()
async def quit(ctx) -> None:

    # Not the owner? Get out of town
    if str(ctx.author.id) != owner_id:
        return await ctx.send(f"Nice try, {ctx.author.name}");

    # Otherwise:
    print("Quit command found! Closing!");
    await ctx.send("Leaving :person_running:");
    await ctx.bot.close();


# Run ittttttt
bot.run(bot_token);
