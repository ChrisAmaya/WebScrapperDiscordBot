import time
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
        for i in range(10):
            driver.find_element_by_xpath("//button[@class='btn btn-default btn-block more-stories']").click()
            time.sleep(0.5)
            print(i)
        
        # parse the html and pull the data we want
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print('\n########################################################\n')
        
        result_links = soup.find_all('a', href=True)
        for i in result_links:
            print(i)
            
        print('\n########################################################\n')
        return result_links
    
    # Send Link to server
    def send_link(self, result_links, search_words):
        send_link = set()
        # print('\n----------------------------------------------------------\n')
        # counter = 1
        # for i in result_links:
        #     if '<a href=' and '/articles/' in str(i):
        #         print()
        #         print(counter)
        #         print(i)
        #         print()
        #         counter += 1
        # print('\n----------------------------------------------------------\n')
        
        for link in result_links:
            text = link.text.lower()
            print(f"Send_link: {text}")
            if search_words in text:
                send_link.add("https://news.usask.ca/"+str(link.get('href')))
        return send_link
    
    # send one random link 
    def random_link(self, result_links):
        all_links = list()
        final_link = set()
        print('\n----------------------------------------------------------\n')
        counter = 1
        for i in result_links:
            if '<a href=' and '/articles/' in str(i):
                print()
                print(counter)
                print(i)
                print()
                counter += 1
                # all_links.append("https://news.usask.ca/"+str(i.get('href')))
                all_links.append(str(i.get('href')))
        print('\n----------------------------------------------------------\n')
        
        randNum = random.randint(1,counter)
        print(randNum)
        print(all_links[randNum])
        temp = all_links[randNum]
        final_link.add(temp)
        
        return temp
        