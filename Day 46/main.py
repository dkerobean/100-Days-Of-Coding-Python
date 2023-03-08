from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
chart = response.text

soup = BeautifulSoup(chart, "html.parser")

titles = soup.find_all(name="h3", id="title-of-a-story")
print(titles)