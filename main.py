# Author: Addi Amaya
# Last Editted: May 19, 2022
#
# Grabs the Newsletter from the University of Saskatchewan and College of Engineering 
# and post in chat periodically and on demand

import discord

# Instatiate discord Client
client = discord.Client()

# Discord Event to check when the bot is online
@client.event
async def on_ready(): 
    print(f'{client.user} is now online!')

# Discord Event to response to message
@client.event
async def on_message(message):
    
    # make sure bot doesnt respond to its own message to avoid infinite loop
    if message.author == client.user:
        return
      # lower case message
    message_content = message.content.lower()  
    
    if message.content.startswith(f'$hello'):
        await message.channel.send('''Fuck you.''')
    
# Retrieve Token
client.run("OTc2OTY4NTgxOTczNjkyNDc2.G9_FY5.b4Rqk3g1NuMs20oJbowRZmerWjrzrDWglBvekA")
