import time
import requests
import random
from selenium import webdriver
from bs4 import BeautifulSoup

class UniversityNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://news.usask.ca/index.php'
        
    # Create search words part
    def search_words(self, user_message):
        words = user_message.split()[1:]
        search_words = ' '.join(words)
        return search_words
    
    # Search on expanded webpage
    def search(self):
        driver = webdriver.Chrome('C:\Drivers\chromedriver.exe')
        driver.get(self.url)
        
        # Need to expand the webpage in order to scrap all articles
        for i in range(10):
            driver.find_element_by_xpath("//button[@class='btn btn-default btn-block more-stories']").click()
            time.sleep(0.5)
        
        # parse the html and pull the data we want
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        result_links = soup.find_all('a', href=True)

        return result_links
    
    # Search on expanded webpage
    def searchFeatured(self):
        response = requests.get('https://news.usask.ca/feeds/featured-articles.xml')
        content = response.content
        
        soup = BeautifulSoup(content, 'xml')

        links = soup.find_all('link')
        
        return links
    
    # Send Link to server
    def send_link(self, result_links, search_words):
        send_link = set()
        
        for link in result_links:
            text = link.text.lower()
            if search_words in text:
                # Some links return without the "https://... some with, condition statement to deal with it"
                if ("http" in str(link)):
                    send_link.add(str(link.get('href')))
                else:
                    send_link.add("https://news.usask.ca/"+str(link.get('href')))
        
        return send_link
    
    # Send featured links to server
    def send_featured(self, result_links):
    
        send_link = set()
        
        for link in result_links:
            hyperlink = link.get_text()
            
            # '"/articles" is a key word all featured links have'
            if "/articles" in hyperlink:
                send_link.add(hyperlink)
                
        return send_link
                 
    # send one random link 
    def random_link(self, result_links):
        all_links = list()
        # final_link = set()
        
        # Need to count how many articles total to generate a random number later
        counter = 1
        for i in result_links:
            if '<a href=' and '/articles/' in str(i):
                counter += 1
                # Some links return without the "https://... some with, condition statement to deal with it"
                if ("http" in str(i)):
                    all_links.append(str(i.get('href')))
                else:
                    all_links.append("https://news.usask.ca/"+str(i.get('href')))
        
        # Generate random link
        randNum = random.randint(1,counter)
        
        return all_links[randNum]
    
    # Send the most recent links (x3)
    def most_recent(self, result_links):
        all_links = list()
        final_links = set()

        for i in result_links:
            if '<a href=' and '/articles/' in str(i):
                # Some links return without the "https://... some with, condition statement to deal with it"
                if ("http" in str(i)):
                    all_links.append(str(i.get('href')))
                else:
                    all_links.append("https://news.usask.ca/"+str(i.get('href')))
        
        # Website has repeats are the beginning and some other links that werent filtered out
        ii=1
        while ii < 6:
            final_links.add(all_links[ii])
            ii+=2
        
        return final_links

class CollegeNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://engineering.usask.ca/about/publications.php'
        
    def searchPublications(self):
        response = requests.get(self.url)
        content = response.content
        
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.find_all('a', href=True)
        
        return result_links
    
    def send_thorough(self, hrefs):
        
        send_link = list()
        
        for href in hrefs:
            text = href.text.lower()
            
            if "thorough" in text:
                send_link.append("https://engineering.usask.ca/"+str(href.get('href')))
                
        return send_link
        
        