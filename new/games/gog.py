import requests
from bs4 import BeautifulSoup
import argparse
parser = argparse.ArgumentParser(description = 'getting an age rating')
parser.add_argument("-agent",dest = 'name')
parser.add_argument("-site",dest = 'url')
args = parser.parse_args()

if args.name == "ageRating":
    r = requests.get(args.url)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('div', class_='age-restrictions')
    f = open("age_rating.txt", "w")
    for item in items:
      f.write(item.text.strip())
    f.close()


