# Author: Addi Amaya
# Last Editted: May 19, 2022
#
# Grabs the Newsletter from the University of Saskatchewan and College of Engineering 
# and post in chat periodically and on demand

# ------------------------------------Imports-------------------------------------
import discord
# from selenium import webdriver
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
        
        # driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
        # driver.get('https://news.usask.ca/index.php')
        # for i in range(10):
        #     driver.find_element_by_xpath("//button[@class='btn btn-default btn-block more-stories']").click()
        #     print(i)
        
        search_words = university_news.search_words(message_content)
        result_links = university_news.search()
        links = university_news.send_link(result_links, search_words)
        
        counter = 0
        if len(links) > 0:
            for link in links:
                if (counter >= 10):
                    break
                else:
                    await message.channel.send(link)
                    counter += 1
        else:
            await message.channel.send(no_result_message)
    
# ----------------------------------Retrieve Token------------------------------------
client.run("OTc2OTY4NTgxOTczNjkyNDc2.G9_FY5.b4Rqk3g1NuMs20oJbowRZmerWjrzrDWglBvekA")
