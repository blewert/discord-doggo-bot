#
# @file   bot.py
# @author ben <bwilliams@lincoln.ac.uk>
# 


import os
import discord
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
flickr_token = get_token_from_file(".flickr_api_key");

# Get flickr api search instance
flickr_api = FlickrPhotosAPI(flickr_token);

# Do a random search for something
flickr_api.random_search(["corgi", "dog"]);



# # Make new client
# bot_client = discord.Client();

# @bot_client.event
# async def on_ready():
#     print(f'{bot_client.user} connected! Token is <{bot_token}>');

# # Run ittttttt
# bot_client.run(bot_token);
