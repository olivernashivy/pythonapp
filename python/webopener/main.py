#create a python proram that convert internet pages into pdf
#install the following modules

#pip install pdfkit
#pip install requests
#pip install bs4

# import the required modules
import pdfkit
import os
import requests

from bs4 import BeautifulSoup

# specify the url
url = "https://www.geeksforgeeks.org/python-programming-language/?ref=shm"

# make a request to fetch the content of the webpage in text format
r = requests.get(url)

# parse the content of the request with BeautifulSoup

soup = BeautifulSoup(r.content, 'html5lib')

# remove script and style elements
for script in soup(["script", "style"]):
    script.extract()

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())

# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

# drop blank lines
text = '    '.join(chunk for chunk in chunks if chunk)

# write the text to a file
with open('geeks.txt', 'w') as f:
    f.write(text)

# convert the text file to pdf

pdfkit.from_file('geeks.txt', 'geeks.pdf')

# open the pdf file
os.startfile('geeks.pdf')


