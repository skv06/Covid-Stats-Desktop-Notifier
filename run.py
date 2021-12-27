import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

country = "India"

# link from where we are fetching data
url = "https://www.worldometers.info/coronavirus/"

while True:
    try:
        pageData = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e) #ConnectionError
        continue

    bs = BeautifulSoup(pageData.content,'html.parser')
    search = bs.select("div tbody tr td")

    start = -1
    for i in range(len(search)):
        if(search[i].get_text().find(country)!=-1):
            start = i
            break

    data = []
    for i in range(1,9):
        try:
            data = data + [search[start+i].get_text()]
        except:
            data = data + ["0"]


    notification.notify(title = "Coronavirus Stats of INDIA", message = "Total infected = {}, New Case = {}, Total Deaths = {}, New Deaths = {}, Total Recovred = {}, New Recovred = {},Active Case = {}, Serious Critical = {}".format(*data) , timeout = 20)
    time.sleep(3600)











