import requests
from bs4 import BeautifulSoup

# get HTTP response from detik.com
page = requests.get("https://www.detik.com/")

# create an instance of BeautifulSoup and parse the response html
soup = BeautifulSoup(page.content, 'html.parser')

# Find class container that contain header_top class
container = soup.find(class_ = "container")
header_top = container.find(class_ = "header_top")

# Find the list of menu
menu = header_top.find(class_ = "menu")
child_menu = list(menu.children)[1]

# get the Tag <a></a> content
a_all = child_menu.find_all("a")

# get the menu text
menu_text = [a.get_text() for a in a_all]
print(menu_text)

# Find the list of menu2
menu2 = header_top.find(class_ = "menu2")

# get the Tag <a></a> content
a_all2 = menu2.find_all("a")

# get the menu text
menu_text2 = [a2.get_text() for a2 in a_all2]
print(menu_text2)
