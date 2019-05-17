from django.shortcuts import render
from django.http import HttpResponse
from . import crawler
# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    urllist=['jhkj','jhgkh2']
    if request.GET.get('url'):
        source=request.GET.get('url')
        #print("inside get")
        #urllist.extend([source])

        spider=crawler.WebCrawl(source)
        urllist=spider.startCrawling()
        urllist.append("Breaking after visiting 10 links")


    return render(request,'WebCrawlerApp/index.html',{'urllist':urllist,})
