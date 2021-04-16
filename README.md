# Discord Bot: Random doggo pictures

## What is this?
This is a fun discord bot I created one late night instead of sleeping. The idea is simple. You type in `!puppy` into your chat, and the bot goes off and retrieves a random cute dog picture for you. It posts it in the channel along with a randomly-generated rating & accompanying message. So yeah, pretty dumb, but fun!

## What's its purpose?
It doesn't really serve a purpose, but I have been wanting to create some materials for teaching students about Python & Discord integration for a while. So maybe this will come in useful in that area, at least, somewhere down the line.

## Installation
Here are some rough steps for you to follow the installation of this project. This assumes you already have created a application + bot on your [Discord Developers](https://discord.com/developers/applications/) portal -- if not, do that first, because you'll need the bot's token to use it (the bot only requires read + send message scopes).
1) Install Python (>= 3.6.0) on your local machine. 
2) Download / clone this repo (`git clone https://github.com/blewert/discord-doggo-bot`)
3) Navigate to this directory and install dependencies with pip, e.g. `py -m pip install -r requirements.txt`. Currently there is only one requirement for this project, `discord.py@1.7.1`.
4) Create a folder in the project folder called `auth`, if it doesn't exist already. Inside `auth/`, make the following files:
   1) `.flickr_api_key`, i.e. `auth/.flickr_api_key`.
   2) `.owner_id` i.e. `auth/.owner_id`.
   3) `.token` i.e. `auth/.token`.
5) Add the relevant authentication details inside of these files (for a guide, see below). 

### Authentication files
The project relies on a few files with authentication details inside them in order to work. A table is shown below to explain this.

| Name | Relative path (from project root) | Purpose |
| ---- | --------------------------------- | ------- |
| Flickr API key | `auth/.flickr_api_key` | To search Flickr for dog images. |
| Discord Owner ID | `auth/.owner_id` | The user ID who "owns" this bot. Used so that privileged commands can only be accessed by one person. |
| Bot Token | `auth/.token` | The discord bot's token, for access. You can find this on the [Discord Developers portal](https://discord.com/developers/applications/).

Once you have created these files in the correct place, you need to only fill them up with their relevant details. Make sure the token/key is the *only* thing in the file. There should only be one line, no whitespace, and *just* the token.

### Why put them in files though?
Because otherwise your secret auth tokens get listed on github! 😋


## Running the project
After installing, it's fairly to run the project, just type:

```py
python bot.py
```

You can then interact with the bot in your server. The following is a list of commands you can use.

| Command | Description |
| ------- | ----------- |
| `!puppy` | Finds a random dog picture and sends it to the channel the user requested it on. |
| `!quit` | Exits the process hosting the bot, will only work for users whose user id matches the one found in `auth/.owner_id`. |


##  Closing notes
I'm too lazy to add a license to this project, but feel free to modify + develop on this without crediting me. I'd like to hear what you get up to though! Just have fun with it! 🙂