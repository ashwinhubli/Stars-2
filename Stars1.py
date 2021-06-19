from bs4 import BeautifulSoup 
import requests
import pandas as pd

Start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(Start_url)
soup =  BeautifulSoup(page.text,'html.parser')
star_table = soup.find('table')
templist = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    templist.append(row)

star_mag = []
star_name = []
star_bayer = []
star_distance =[]
star_spectral = []
star_mass = []
star_radius =[]
star_luminosity = []

temp = len(templist)

for i in range(1,temp):
    star_mag.append(templist[i][0])
    star_name.append(templist[i][1])
    star_bayer.append(templist[i][2])
    star_distance.append(templist[i][3])
    star_spectral.append(templist[i][4])
    star_mass.append(templist[i][5])
    star_radius.append(templist[i][6])
    star_luminosity.append(templist[i][7])
    
df = pd.DataFrame(list(zip(star_mag,star_name,star_bayer,star_distance,star_spectral,star_mass,star_radius,star_luminosity)),columns=['VMag','Star_name','Bayer Designation','Distance','Spectral Class','Mass','Radius','Luminosity'])
df.to_csv('stars.csv')
