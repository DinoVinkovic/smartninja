from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

#scrape_file = open("Quotes.txt", "w")

url = "http://quotes.yourdictionary.com/theme/marriage/"

html = urlopen(url).read()

soup = BeautifulSoup(html)

quotes = soup.findAll("p", attrs={"class" : "quoteContent"})

for index, quote in enumerate(quotes):
    print "Quote #%s:" % (index+1), quote.text
    if index == 4:
        break
