from bs4 import BeautifulSoup
import requests
import csv
res = requests.get('https://www.meteoblue.com/en/weather/forecast/week/23.548N87.293E89_Asia%2FCalcutta')
soup = BeautifulSoup(res.text,'lxml')

csv_file=open('weather_data_details.csv','w')
csv_writer = csv.writer(csv_file)

classes= list()
inc=0
description=["Temperature (°C)","Temperature felt (°C)","Wind direction","Wind speed (km/h)","Precipitation (mm/3h)","Precipitation probability","Precipitation hourly"]
data = soup.find('table' , class_='picto')
csv_writer.writerow([data.find('div',class_='cell').find('span',class_='description').find('time')['datetime'],'08:00','11:00','14:00','17:00','20:00','23:00'])
for items in data.findAll('tr'):
    classes.append((items)['class'])
picto=soup.find('table',class_='picto')
for cl in classes[2:9]:
    data = soup.find('tr',class_=cl)
    l=list()
    for date in data.findAll('td'):
        l.append(date.text)
    print(l[0],l[1],l[2],l[3],l[4],l[5])
    csv_writer.writerow([description[inc],l[0],l[1],l[2],l[3],l[4],l[5]])
    print(description[inc])
    inc=inc+1
csv_file.close()

