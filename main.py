# Author: Addi Amaya
# Last Editted: May 19, 2022
#
# Grabs the Newsletter from the University of Saskatchewan and College of Engineering 
# and post in chat periodically and on demand

# ------------------------------------Imports-------------------------------------
import discord
import UniversityScrapper

# --------------------------------Instatiatations---------------------------------
client = discord.Client()
university_news = UniversityScrapper.UniversityNews()

# --------------------------------Global Variables--------------------------------
no_result_message = '''Nada, sorry'''

# ---------------------------------Discord Events---------------------------------
# check when the bot is online
@client.event
async def on_ready(): 
    print(f'{client.user} is now online!')

# response to message
@client.event
async def on_message(message):
    
    # make sure bot doesnt respond to its own message to avoid infinite loop
    if message.author == client.user:
        return
      # lower case message
    message_content = message.content.lower()  
    print(f'The message is: {message_content}')
    
    if message.content.startswith(f'$hello'):
        await message.channel.send('''Fuck you.''')
        
    if f'$search' in message_content:
        key_words, search_words = university_news.key_words_search_words(message_content)
        result_links = university_news.search(key_words)
        links = university_news.send_link(result_links, search_words)
        
        if len(links) > 0:
            for link in links:
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)
    
# Retrieve Token
client.run("OTc2OTY4NTgxOTczNjkyNDc2.G9_FY5.b4Rqk3g1NuMs20oJbowRZmerWjrzrDWglBvekA")
