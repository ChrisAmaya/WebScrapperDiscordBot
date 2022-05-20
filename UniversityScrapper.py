import requests
from bs4 import BeautifulSoup

class UniversityNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://news.usask.ca/index.php'

    # Create search words and url keywords part
    def search_words(self, user_message):
        words = user_message.split()[1:]
        search_words = ' '.join(words)
        print(f"Search_Words: {search_words}")
        return search_words
    
    def search(self):
        
        # create requests and get the response
        response = requests.get(self.url)
        content = response.content
        
        # parse the html and pull the data we want
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.find_all("a")
        for i in result_links:
            print(i)
        return result_links
    
    def send_link(self, result_links, search_words):
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            print(f"Send_link: {text}")
            if search_words in text:
                send_link.add("https://news.usask.ca/"+str(link.get('href')))
        return send_link