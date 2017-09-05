# coding=utf-8

# @azerpas on IG // @azrpas on Twitter


import BeautifulSoup
import requests
import json
import os , time , random , datetime , threading

colors = ["Black" , "Blue" , "Red" , "Off White" , "Navy" , "Multi" ,"Teal" , "Bright Yellow" , "Yellow Plaid" , "Olive Drab", "Dark Red" , "Magenta" , "White" , "Pink" , "Woodbine" , "Light Yellow" , "Light Burgundy" , "Denim" , "Green" , "Royal" , "Pale Peach" , "Heater Grey","Heather Mustard" , "Navy Digi Camo" , "Dark Purple" , "Orange" , "Rose" , "Ice Blue" , "Plum" , "Pale Lime" , "Bright Orange", "Hickory Stripe", "Washed Blue", "Peach", "Tan Digi Camo", "Pink Digi Camo", "pale violet", "indigo", "gold", "dark olive","navy digi camo","emerald green","silver","dusty teal","rigid indigo","yellow","brown","desrt camo","olive","charcoal","pine","burgundy","purple","maroon","snakeskin","rust","woodland camo","oxblood","ash grey","khaki","tan"]
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
		log("Thread n°" + str(i) + " launched")
		time.sleep(random.uniform(3.4,5.2))
	while not active_threads == 0:
		log('Active Threads ----..---- ' + str(active_threads))
		time.sleep(5)

	log("Ended")
	print(items)

def log(event):
    print('SupremeScrap by Azerpas :: ' + str(datetime.datetime.now().strftime('%H:%M:%S')) + ' :: ' + str(event))


def retrieveURL():
	soCount = 0
	global active_threads
	active_threads += 1
	d = datetime.datetime.now().strftime('%H:%M')

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
					for key in colors:
						if key.lower() in name:
							name = 'error'
					link = ka['href']
					log("Item is: " + name.encode('utf-8') + " " + link.encode('utf-8'))
					items[name] = str(link)
					dicttt = {name:link}
					try:
						with open(str(d)+'.json') as f:
							data = json.load(f)
							data.update(dicttt)
						with open(str(d)+'.json','w') as f:
							json.dump(data,f)
					except IOError:
						with open(str(d)+'.json','w') as f:
							json.dump(dicttt,f)
		print('\n\n')
		print("----------------------------")
		print("----------------------------")
		print("Sleeping 0 seconds")
		print("----------------------------")
		print("----------------------------")
		print('\n\n')
		time.sleep(0)
	active_threads -= 1
	log("Sold Out Counter = " + str(soCount))
	log("JSON SAVED IN: " + str(d) + ".json")

if __name__ == "__main__":
    main()
