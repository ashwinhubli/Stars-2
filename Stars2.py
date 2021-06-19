from bs4 import BeautifulSoup 
import requests
import pandas as pd

Start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(Start_url)
soup = BeautifulSoup(page.text,'html.parser')
star_table = soup.find_all('table')
print(len(star_table))

templist= []
table_rows = star_table[4].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    single_row = [i.text.rstrip() for i in td]
    templist.append(single_row)
print(templist)

star_name = []
star_distance =[]
star_mass = []
star_radius =[]
star_constellation = []
star_discovery_date = []

temp = len(templist)

for i in range(1,temp):
    star_name.append(templist[i][0])
    star_constellation.append(templist[i][1])
    star_distance.append(templist[i][5])
    star_mass.append(templist[i][7])
    star_radius.append(templist[i][8])
    star_discovery_date.append(templist[i][9])

df = pd.DataFrame(list(zip(star_name,star_constellation,star_distance,star_mass,star_radius,star_discovery_date)),columns=['Star_name','Constellation','Distance','Mass','Radius','Discovery Year'])
df.to_csv('stars2.csv')