from bs4 import BeautifulSoup

with open('website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.string)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string)

name = soup.select_one(selector="#name")
print(name)

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(selector=".heading")

