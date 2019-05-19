# Web_crawler
Project is developed using Django Framework. 

Follow the below mentioned steps to deploy it on local machine and run it:
1. Download folder Web_crawler in local machine
2. From CLI go to that path of folder & create virtual environment
3. Project is developed in Python version 3.5.6
4. Install following packages: 
   pip install django (version 2.1.1),
   pip install BeautifulSoup4 (version 4.7.1),
   pip install requests (version 2.22.0) &
   pip install urllib3 (version 1.25.2)
5. From inside Web_crawler, run command: python manage.py runserver
6. From browser open link 'http;//127.0.0.1:8000/WebCrawlerApp'
7. Provide seed URL in the Textbox (For example: https://www.python.org/)
8. After crawling, it displays 10 links and then stops

Inside crawler.py, from the seed URL, it is scanning source code and fetching URLs, then adding it to a queue.
For the next link in the queue, same procedure is followed. Here Depth First Search is used to crawl through the links.
Since it is an infinite loop, have put a break after visiting 10 links and displayed them over the console as well as web page.
