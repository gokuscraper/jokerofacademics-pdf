import requests
from bs4 import BeautifulSoup

url = "https://jokerofacademics.com/articles.php?page=2"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

articles = []
for card in soup.select(".article-card"):
    title_tag = card.select_one(".card-title a")
    article = {
        "id": title_tag['href'].split('=')[1],
        "title": title_tag.text.strip(),
        "author": card.select_one(".card-author").text.strip(),
        "tag": card.select_one(".card-tag").text.strip(),
        "abstract": card.select_one(".card-abstract").text.strip(),
        "cover": card.select_one(".card-cover img")['src'],
        "date": card.select(".card-meta span")[0].text.strip(),
        "views": card.select(".card-meta span")[1].text.strip(),
        "downloads": card.select(".card-meta span")[2].text.strip(),
        "comments": card.select_one(".waline-comment-count")['data-path']
    }
    articles.append(article)

print(articles)