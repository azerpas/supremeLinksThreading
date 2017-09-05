# supremeLinksThreading
Supreme Threaded Bot that will scrape every links from supreme website and then export it as JSON

Uses BeautifulSoup, Requests, JSON, time, threading

This bot will use threading module to scrape URL from Supreme webshop and output it in JSON format ('item':'itemURL')

You can choose how many threads will scrape at the same time. There's a delay between every thread launching. 

TO,DO:

- Handle exceptions.
- Delete colors from JSON data.
- Add non stop scraping until user decides to end it. 
- Proxy support
