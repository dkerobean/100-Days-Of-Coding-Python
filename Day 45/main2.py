import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)

article_link = soup.select_one(selector=".titleline a").get("href")
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

highest_vote = max(article_upvote)
highest_index = article_upvote.index(highest_vote)

print(article_texts[highest_index])
print(article_links[highest_index])






