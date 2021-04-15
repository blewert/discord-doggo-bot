# Main
import os
import discord



def get_token_from_file(filename):

    # No file? Die:
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Couldn't find {filename} (token for discord bot).");

    # File? cool, strip, return:
    with open(filename, 'r') as f:
        return f.readline().strip();
        



# Get bot token
bot_token = get_token_from_file(".token");

# Make new client
bot_client = discord.Client();

@bot_client.event
async def on_ready():
    print(f'{bot_client.user} connected! Token is <{bot_token}>');

# Run ittttttt
bot_client.run(bot_token);
