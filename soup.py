from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url='https://www.terralogic.com/about-us/'

uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html, "html.parser")

#print(page_soup)


container=page_soup.findAll("div",{"class":"col-md-3 leader-1rem"})
containers=container[0]
ceo=containers.findAll("h5",{"class":"fnt-lg tr-leader__name"})
print(ceo[0].text.strip())

