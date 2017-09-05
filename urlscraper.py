# coding=utf-8

# @azerpas 


import BeautifulSoup
import requests
import json
import os , time , random , datetime , threading


category = ["accessories","jackets","shirts","tops_sweaters","sweatshirts","pants","hats","bags","shoes","skate"]

base_url = "http://www.supremenewyork.com/shop/all/"
sup_url = "http://supremenewyork.com"
items = {}

headers = {
	"Host": "www.supremenewyork.com",
	"Connection": "keep-alive",
	"Cache-Control": "max-age=0",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

threads = 1  #change this variable to edit how many thread you want
active_threads = 0

def main():
	for i in range(0,threads):
		t = threading.Thread(target=retrieveURL)
		t.daemon = True
		t.start()
		print("Thread n°" + str(i) + " launched")
		time.sleep(3)
	while not active_threads == 0:
		print('Active Threads ----..---- ' + str(active_threads))
		time.sleep(5)

	print(items)

def retrieveURL():
	soCount = 0
	global active_threads
	active_threads += 1

	for i in category:
		s = requests.session()
		url = str(base_url)+str(i)
		req = s.get(url, headers=headers).text
		soup = BeautifulSoup.BeautifulSoup(req)
		for div in soup.findAll('div',{"class":"turbolink_scroller"}):
			for ka in div.findAll('a'):
				name = ka.text.lower()
				if "sold out" in name:
					soCount += 1 #FUN
				else:
					link = ka['href']
					print("Item is: " + name.encode('utf-8') + " " + link.encode('utf-8'))
					items[name] = str(link)
		print('\n\n')
		print("----------------------------")
		print("----------------------------")
		print("Sleeping 3 seconds")
		print("----------------------------")
		print("----------------------------")
		print('\n\n')
		time.sleep(3)
	active_threads -= 1
	print("Sold Out Counter = " + str(soCount))

if __name__ == "__main__":
    main()
