#! Python 3.9.1
# Searchs google for a specific word or phrase and then displays the results on the first page

import requests
import bs4
import sys

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
        for el in soup.find_all("div", {"class" : "yuRUbf"}):
            # Change this print to call the write_to_excel() method!
            print(el.text)

    # TODO Write search results to an excel file and format it
    def write_to_excel(self):
        pass

searching = WordSearch()
searching.search()
