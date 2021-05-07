import requests
from bs4 import BeautifulSoup
import csv

page_id = 1
headphones = []
total = []
links = []

while(True):
    #url
    url = f'https://egypt.souq.com/eg-en/Headphones%20and%20Headsets/l/?fbs3_eg=yes&ref=nav&section=2&page={page_id}'
    #get whole page content
    request = requests.get(url).content
    #parsing page
    soup = BeautifulSoup(request, 'html.parser')

    #get itmes in list
    items = soup.find_all('a', {'class':'itemLink block sPrimaryLink'})
    prices = soup.find_all('span', {'class': 'itemPrice'})
    #print(items)

    #get each item name,link and price
    for i in range(len(items)):
        # print(items[i].text)
        headphones.append(items[i].text.strip())
        # print(items[i]['href'])
        links.append(items[i]['href'].strip())
        # print(prices[i].text)
        total.append(prices[i].text.strip())

    print(f'page {page_id} was completed')
    print('>>collected items: '+str((len(headphones))))
    page_id += 1

    if len(items) < 60 :# number of items per page 60 and last page will be less than 60 :D so i will go out loop
        break



with open ('file.csv', 'w') as Ofile : #open/create csv file
    writer = csv.writer(Ofile) #prepair csv file for writing
    writer.writerow(['Name', 'Price', 'Link']) #each column name
    #get all collected items 
    for k in range(len(headphones)):
        # print(headphones[k], total[k], links[k])
        csv_array = [headphones[k].strip(), total[k].strip(), links[k].strip()] #row to be inserted in csv file
        # print(csv_array)
        try:
            writer.writerow(csv_array)
        except:
            pass