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
college_news = UniversityScrapper.CollegeNews()

# --------------------------------Global Variables--------------------------------
no_result_message = '''There does not seem to be any results, sorry'''
article_post_amount = 5

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
        
    # User wants to search for an Article with a key word(s)
    if f'$search' in message_content:
        print("\n---------------BOT MESSAGE--------------\n")
        print(f'{client.user} Has received a search request!')
        print("\n----------------------------------------\n")
        
        # Generate Key words that will be used in filter process
        search_words = university_news.search_words(message_content)
        
        # Grab all articles on the University of Saskatchewan News website
        result_links_university_website = university_news.search()
        
        # Grab all articles on the College of Engineering Website
        result_links_college_website = college_news.search()
        
        # Generate a list of relavent articles from U of S website with key words
        links_university_website = university_news.send_link(result_links_university_website, search_words)
        
        # Generate a list of relavent articles from College website with key words
        links_college_website = college_news.send_link(result_links_college_website, search_words)
        
        # Concatenate both sets from both websites
        links = links_university_website.union(links_college_website)
        
        # Send links to where ever the bot was called
        counter = 0
        if len(links) > 0:
            for link in links:
                # Limits message to avoid spam
                if (counter >= article_post_amount):
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
        result_links_university_website = university_news.search()
        
        # Grab all articles on the College of Engineering Website
        result_links_college_website = college_news.search()
        
        # Generate a link for a random article
        link_university_website = university_news.random_link(result_links_university_website)
        
        # Generate a random link from the college website
        link_college_website = college_news.random_link(result_links_college_website)
        
        randomArticle.add(link_college_website)
        randomArticle.add(link_university_website)
        
        # Send Articles to Discord
        if len(randomArticle) == 2:
            for link in randomArticle:
                await message.channel.send('-----------')
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
        result_links_university_website = university_news.searchMostRecent()
        
        # Grab all articles on the College of Engineering Website
        result_links_college_website = college_news.search()
        
        # Returns the most recent articles from the website 
        links_university_website = university_news.most_recent(result_links_university_website)
        links_college_website = college_news.most_recent(result_links_college_website)
        links = links_university_website.union(links_college_website)
        
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
        
        # Searched xml file for links (features are treated differently on website)
        result_links = university_news.searchFeatured()
        
        # Filters out all non articles
        links = university_news.send_featured(result_links)
        
        if len(links) != 0:
                for link in links:
                    await message.channel.send('----------------------')
                    await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)
        
    # User wants the most recent Thorough Article
    if f'$thorough' in message_content:
        
        send_links = set()
        
        # Grabs all hrefs with thorough to it
        result_links = college_news.searchPublications()
        
        # filters out unrelated hrefs
        links = college_news.send_thorough(result_links)
        
        # Removes repeats 
        links = list(dict.fromkeys(links))
        
        # Adds the most recent thorough article
        send_links.add(links[-2])
        
        if len(send_links) != 0:      
            for link in send_links:
                await message.channel.send(link)
        else:
            await message.channel.send(no_result_message)
        
# ----------------------------------Retrieve Token------------------------------------
client.run("OTc2OTY4NTgxOTczNjkyNDc2.G9_FY5.b4Rqk3g1NuMs20oJbowRZmerWjrzrDWglBvekA")

