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
    
    message_content = message.content.lower()  
    print(f'The message is: {message_content}')
    
    if message.content.startswith(f'$Insult Me'):
        await message.channel.send('''Fuck you.''')
        
    if f'$search' in message_content:
        search_words = university_news.search_words(message_content)
        result_links = university_news.search()
        links = university_news.send_link(result_links, search_words)
        
        counter = 0
        if len(links) > 0:
            for link in links:
                # Limits message to avoid spam
                if (counter >= 10):
                    break
                else:
                    await message.channel.send(link)
                    counter += 1
        else:
            await message.channel.send(no_result_message)
    
    if f'$random' in message_content:
        result_links = university_news.search()
        temp = set()
        link = university_news.random_link(result_links)
        temp.add(link)
        print(f"\nlink: {temp}\n")
        
        if len(temp) == 1:
            for link in temp:
                await message.channel.send(link)    
        else:
            await message.channel.send(no_result_message)
            
    if f'$most recent' in message_content:
        result_links = university_news.search()
        links = university_news.most_recent(result_links)
        
        print(f"\nMost Recent Links: {links}\n")
        
        if (len(links) > 0):
            for link in links:
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)
            
    if f'$featured' in message_content:
        result_links = university_news.searchFeatured()
        # links = university_news.send_link(result_links)
        
# ----------------------------------Retrieve Token------------------------------------
client.run("OTc2OTY4NTgxOTczNjkyNDc2.G9_FY5.b4Rqk3g1NuMs20oJbowRZmerWjrzrDWglBvekA")
