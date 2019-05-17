#from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

class WebCrawl(object):
    base_url=""
    visited_url=[]
    pending_url=[]
    #output=[]

    def __init__(self,base_url):
        self.base_url=base_url
        self.pending_url.append(self.base_url)

    def getLinks(self,link):
        if link in self.visited_url:
            self.pending_url.remove(link)
            return

        try:
            source_code=requests.get(link)
            response=source_code.text
            soup=BeautifulSoup(response,"html.parser")

            self.visited_url.append(link)
            print(link)

            for a in soup.find_all('a',href=True):
                links=str(a['href'])
                if links.startswith("http"):
                    links=urljoin(link,links)

                if links in self.visited_url:
                    continue
                elif links not in self.pending_url:
                    self.pending_url.append(links)

        except:
            pass


    def startCrawling(self):
         #while(len(pending_url) > 0):
        for links in self.pending_url:
            self.getLinks(links)
            if len(self.visited_url)>10:
                break

        return self.visited_url
