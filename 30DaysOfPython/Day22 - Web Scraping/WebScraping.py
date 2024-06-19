######################## Python Web Scraping ########################
    # What is Web Scrapping
    # The internet is full of huge amount of data which can be used for different purposes. 
    # To collect this data we need to know how to scrape data from a website.

    # Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

    # In this section, we will use beautifulsoup and requests package to scrape data. The package version we are using is beautifulsoup 4.
    # To start scraping websites you need requests, beautifoulSoup4 and a website.

    # pip install requests
    # pip install beautifulsoup4
    
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(url)
status = response.status_code
content = response.content

scrape = BeautifulSoup(content, 'html.parser')
# tables = scrape.findall('table', {'cellpadding': '3'})
# table = tables[0]

#print(response)
print(status)
print(scrape.title)
print(scrape.title.get_text())
print(scrape.body)
# for td in table.find('tr').findall('td'):
#     print(td.text)


    
    
