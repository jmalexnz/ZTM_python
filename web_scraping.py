# <url>/robots.txt
# tells you what you are allowed to scrape
# may also have a crawl delay request to stop 
# users overloading servers
# practice ethical program, check t&c before scraping

# ideally you can avoid having to scrape by using 
# the website's API
# Scrapy is a good tool for scraping
# May want to start looking at databases for storing data


# lets get stories the first two pages from hackernews that have over 100 points

import requests
from bs4 import BeautifulSoup
import pprint



res_pg1 = requests.get('https://news.ycombinator.com/news')
res_pg2 = requests.get('https://news.ycombinator.com/news/?p=2')

# print(res.text)
# use beautifulsoup to clean up the data
soup = BeautifulSoup(res_pg1.text, 'html.parser')
soup_p2 = BeautifulSoup(res_pg2.text, 'html.parser')
soup.extend(soup_p2)
print(type(soup))


# print(soup) # it is no longer one long string
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('a'))
# print(soup.find_all('div'))
# print(soup.title)
# print(soup.a)
# print(soup.find(id='score_35036871'))
# print(soup.select('.score'))

# Get the info we need
links = soup.select(".titleline")
votes = soup.select(".score")
subtext = soup.select('.subtext')
# use subtext instead of votes as sometimes there are no votes

# print(votes[0].get('id'))

def sort_stories_by_vote(hn_list):
    return sorted(hn_list, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for i, link in enumerate(links):
        vote = subtext[i].select('.score')
        if len(vote) > 0:
            points = int(vote[0].getText().replace(' points',''))
            if points > 100:
                title = link.getText()
                href = link.find('a')['href']
                hn.append({'title':title,
                        'url':href,
                        'votes':points})
    return sort_stories_by_vote(hn)



hn = create_custom_hn(links, subtext)

pprint.pprint(hn)