import discord
import os
# Replace 'YOUR_TOKEN_HERE' with your bot's token
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.typing = False  # Disable typing notifications (optional)

# Create a Discord client with intents
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print(f'Bot ID: {client.user.id}')
    print('------')

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent loops
    if message.author == client.user:
        return

    # Check if the message content is "!hello"
    if message.content == '!hello':
        # Send a reply
        await message.channel.send(f'Hello, {message.author.mention}!')

# Run the bot with your token
client.run(TOKEN)
