# Importing modules Requests, BeautifulSoup and XPath
import requests
from bs4 import BeautifulSoup
from lxml import etree

URL = 'https://www.nosdeputes.fr/deputes'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

links = []
names = []
emails = []

# Get URL links of each deputy
tds = soup.findAll("td")
for td in tds:
  link = td.findAll("a")
  for a in link:
    link = a['href']
    links.append('https://www.nosdeputes.fr' + link)

# # Test with the first deputy
# URL_DEPUTY = 'https://www.nosdeputes.fr/damien-abad'
# response = requests.get(URL_DEPUTY)
# soup = BeautifulSoup(response.text, "html.parser")
# name = soup.find("h1")
# print(name.text)
# dom = etree.HTML(str(soup))
# email = dom.xpath('//*[@id="b1"]/ul[2]/li[1]/ul/li[1]/a')[0]
# print(email.text)
  
# Get emails and names of each deputy in links
for i in links:
  response = requests.get(i)
  soup = BeautifulSoup(response.text, "html.parser")
  # Get name from h1
  name = soup.find("h1")
  names.append(name.text)
  # Get email using XPath
  dom = etree.HTML(str(soup))
  try:
    email = dom.xpath('//*[@id="b1"]/ul[2]/li[1]/ul/li[1]/a')[0]
    emails.append(email.text)
  except IndexError:
    emails.append(None)
print("------------------- List of names -------------------")
print(names)
print("------------------- List of emails -------------------")
print(emails)
print("------------------- Deputy nº 500 -------------------")
print(names[499])
print(emails[499])