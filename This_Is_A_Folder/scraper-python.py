#OPEN ENVIRONMENT WITH THE RUN BUTTON FIRST BEFORE DOING ANYTHING!!!!!!!!!!!!
import requests as reqs
from bs4 import BeautifulSoup

def scrape():
    
    url = 'https://www.google.com/search?client=firefox-b-1-d&q=ddefinition+of+woke'
    response = reqs.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.get_text())


scrape()




