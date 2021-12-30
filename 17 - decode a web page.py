import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,features="html.parser")

for title in soup.find_all(class_="story-heading"):
    if title.a:
       print(story_heading.a.text.replace("\n", " ").strip())
   else:
       print(story_heading.contents[0].strip())
