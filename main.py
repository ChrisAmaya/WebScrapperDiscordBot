# Author: Addi Amaya
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
    print("\n---------------BOT MESSAGE--------------\n")
    print(f'{client.user} is now online!')
    print("\n----------------------------------------\n")

# response to message
@client.event
async def on_message(message):
    
    # make sure bot doesnt respond to its own message to avoid infinite loop
    if message.author == client.user:
        return
    
    # Convert message to all lowercase for normailzation
    message_content = message.content.lower()  
        
    # User wants to search for an Article with a key word
    if f'$search' in message_content:
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has received a search request!')
        print("\n----------------------------------------\n")
        
        # Generate Key words that will be used in filter process
        search_words = university_news.search_words(message_content)
        
        # Grab all articles on the University of Saskatchewan News website
        result_links = university_news.search()
        
        # Generate a list of relavent articles with key words
        links = university_news.send_link(result_links, search_words)
        
        # Send links to where ever the bot was called
        counter = 0
        if len(links) > 0:
            for link in links:
                # Limits message to avoid spam
                if (counter >= 5):
                    break
                else:
                    await message.channel.send('----------------------')
                    await message.channel.send(link)
                    counter += 1
        else:
            await message.channel.send(no_result_message)
        
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has finished its search request!')
        print("\n----------------------------------------\n")
    
    # User wants one random article from the website
    if f'$random' in message_content:
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has received a random request!')
        print("\n----------------------------------------\n")
        
        randomArticle = set()
        
        # Grab all articles on the University of Saskatchewan News website
        result_links = university_news.search()
        
        # Generate a link for a random article
        link = university_news.random_link(result_links)
        
        # Send Article to Discord
        randomArticle.add(link)
        if len(randomArticle) == 1:
            for link in randomArticle:
                await message.channel.send(link)    
        else:
            await message.channel.send(no_result_message)
        
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has finished its random request!')
        print("\n----------------------------------------\n")
            
    # User wants the most recent articles from the website (top 3)
    if f'$most recent' in message_content:
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has received a most recent request!')
        print("\n----------------------------------------\n")
        
        # Grab all articles on the University of Saskatchewan News website
        result_links = university_news.search()
        
        # Returns the most recent articles from the website 
        links = university_news.most_recent(result_links)
        
        # Send Articles to Discord        
        if (len(links) > 0):
            for link in links:
                await message.channel.send('----------------------')
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)
        
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has finished its most recent request!')
        print("\n----------------------------------------\n")
        
    # User wants the articles in the featured section
    if f'$featured' in message_content:
        result_links = university_news.searchFeatured()
        # links = university_news.send_link(result_links)
        
# ----------------------------------Retrieve Token------------------------------------
client.run("OTc2OTY4NTgxOTczNjkyNDc2.G9_FY5.b4Rqk3g1NuMs20oJbowRZmerWjrzrDWglBvekA")
