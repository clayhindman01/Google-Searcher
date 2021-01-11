#! Python 3.9.1
# Searchs google for a specific word or phrase and then displays the results on the first page

import requests
import bs4
import sys
from openpyxl import Workbook

class WordSearch():
    
    def __init__(self):
        print("Searching google for %s..." % ' '.join(sys.argv[1:]))

    # Calls the requests library and pulls the search results out using bs4
    def search(self):
        word_to_search = ''.join(sys.argv[1:])
        url = "https://www.google.com/search?q=" + word_to_search

        # Opens the url provided and checks that the url exists
        response = requests.get(url, headers = {
            'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        })
        response.raise_for_status()

        # Uses bs4 to extract the search results and print them out
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        book = Workbook()
        sheet = book.active
        sheet.column_dimensions['A'].width = 55
        sheet.column_dimensions['B'].width = 30
        sheet["A1"] = "Search Result"
        sheet["B1"] = "URL"

        counter = 2
        for element in soup.find_all("h3", {"class" : ["LC20lb DKV0Md", ]}):
            row = ("A%s" % counter)
            # Change this print to call the write_to_excel() method!
            sheet[row] = element.text
            counter += 1

        counter2 = 2
        for div_element in soup.find_all("div", {'class': 'yuRUbf'}):
            a_tags = div_element.find_all('a', href= True)
            for i in a_tags:
                if i.find(class_="fl"):
                    continue
                row = ("B%s" % counter2)
                sheet[row] = i.text
                counter2 += 1

        book.save("search.xlsx")

searching = WordSearch()
searching.search()
