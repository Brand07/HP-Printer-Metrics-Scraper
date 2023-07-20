import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


#STN2
Printer1 = "STN2"
url1_stn2 = 'http://10.10.113.150/hp/device/InternalPages/Index?id=UsagePage'
url2_stn2 = 'http://10.10.113.150/hp/device/DeviceStatus/Index'
url2_stn2 = 'http://10.10.113.150/hp/device/DeviceStatus/Index'

#Page Count
tag1_stn2 = 'UsagePage.ImpressionsByMediaSizeTable.Print.Letter.Total'
#Toner Level
tag2_stn2 = 'SupplyGauge0'
#Maintenance Kit Level
tag3_stn2 = 'SupplyGauge1'

#First URL
response1 = requests.get(url1_stn2)
soup1 = BeautifulSoup(response1.text, 'html.parser')
data1 = soup1.find('td', {'id': tag1_stn2}).text.replace(',', '')

#Second URL
response2 = requests.get(url2_stn2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
data2 = soup2.find('span', {'id': tag2_stn2}).text.replace(',', '')

#Third URL
response3 = requests.get(url2_stn2)
soup3 = BeautifulSoup(response3.text, 'html.parser')
data3 = soup3.find('span', {'id': tag3_stn2}).text.replace(',', '')

#LTL1
Printer2 = "LTL1"
url1_ltl1 = 'http://10.10.113.212/hp/device/InternalPages/Index?id=UsagePage'
url2_ltl1 = 'http://10.10.113.212/hp/device/DeviceStatus/Index'
url3_ltl1 = 'http://10.10.113.212/hp/device/DeviceStatus/Index'

tag1_ltl1 = 'UsagePage.ImpressionsByMediaSizeTable.Print.Letter.Total'
tag2_ltl1 = 'SupplyGauge0'
tag3_ltl1 = 'SupplyGauge1'

#First URL

response4 = requests.get(url1_ltl1)
soup4 = BeautifulSoup(response4.text, 'html.parser')
data4 = soup4.find('td', {'id': tag1_ltl1}).text.replace(',', '')

#Second URL

response5 = requests.get(url2_ltl1)
soup5 = BeautifulSoup(response5.text, 'html.parser')
data5 = soup5.find('span', {'id': tag2_ltl1}).text.replace(',', '')

#Third URL

response6 = requests.get(url3_ltl1)
soup6 = BeautifulSoup(response6.text, 'html.parser')
data6 = soup6.find('span', {'id': tag3_ltl1}).text.replace(',', '')


#CLB1

Printer3 = "CLB1"
url1_clb1 = 'http://10.10.113.180/hp/device/InternalPages/Index?id=UsagePage'
url2_clb1 = 'http://10.10.113.180/hp/device/DeviceStatus/Index'
url3_clb1 = 'http://10.10.113.180/hp/device/DeviceStatus/Index'

tag1_clb1 = 'UsagePage.ImpressionsByMediaSizeTable.Print.Letter.Total'
tag2_clb1 = 'SupplyGauge0'
tag3_clb1 = 'SupplyGauge1'

#First URL

response7 = requests.get(url1_clb1)
soup7 = BeautifulSoup(response7.text, 'html.parser')
data7 = soup7.find('td', {'id': tag1_clb1}).text.replace(',', '')

#Second URL 

response8 = requests.get(url2_clb1)
soup8 = BeautifulSoup(response8.text, 'html.parser')
data8 = soup8.find('span', {'id': tag2_clb1}).text.replace(',', '')

#Third URL

response9 = requests.get(url3_clb1)
soup9 = BeautifulSoup(response9.text, 'html.parser')
data9 = soup9.find('span', {'id': tag3_clb1}).text.replace(',', '')

## SPS2 ##

printer4 = "SPS2"

url1_sps2 = 'http://10.10.113.215/hp/device/InternalPages/Index?id=UsagePage'
url2_sps2 = 'http://10.10.113.215/hp/device/DeviceStatus/Index'
url3_sps2 = 'http://10.10.113.215/hp/device/DeviceStatus/Index'

tag1_sps2 = 'UsagePage.ImpressionsByMediaSizeTable.Print.Letter.Total'
tag2_sps2 = 'SupplyGauge0'
tag3_sps2 = 'SupplyGauge1'

#First URL 
response10 = requests.get(url1_sps2)
soup10 = BeautifulSoup(response10.text, 'html.parser')
data10 = soup10.find('td', {'id':tag1_sps2}).text.replace(',', '')

#Second URL
response11 = requests.get(url2_sps2)
soup11 = BeautifulSoup(response11.text, 'html.parser')
data11 = soup11.find('span', {'id': tag2_sps2}).text.replace(',', '')

#Third URL
response12 = requests.get(url3_sps2)
soup12 = BeautifulSoup(response12.text, 'html.parser')
data12 = soup12.find('span', {'id': tag3_sps2}).text.replace(',', '')


## STN1 ##

Printer5 = "STN1"

url1_stn1 = 'http://10.10.113.213/hp/device/InternalPages/Index?id=UsagePage'
url2_stn1 = 'http://10.10.113.213/hp/device/DeviceStatus/Index'
url3_stn1 = 'http://10.10.113.213/hp/device/DeviceStatus/Index'

tag1_stn1 = 'UsagePage.ImpressionsByMediaSizeTable.Print.Letter.Total'
tag2_stn1 = 'SupplyGauge0'
tag3_stn1 = 'SupplyGauge1'

#First URL
response13 = requests.get(url1_stn1)
soup13 = BeautifulSoup(response13.text, 'html.parser')
data13 = soup13.find('td', {'id': tag1_stn1}).text.replace(",", '')

#Second URL
response14 = requests.get(url2_stn1)
soup14 = BeautifulSoup(response14.text, 'html.parser')
data14 = soup14.find('span', {'id': tag2_stn1}).text.replace(',', '')

#Third URL
response15 = requests.get(url3_stn1)
soup15 = BeautifulSoup(response15.text, 'html.parser')
data15 = soup15.find('span', {'id': tag3_stn1}).text.replace(',', '')


#SPS1

Printer6 = "SPS1"

url1_sps1 = 'http://10.10.113.214/hp/device/InternalPages/Index?id=UsagePage'
url2_sps1 = 'http://10.10.113.214/hp/device/DeviceStatus/Index'
url3_sps1 = 'http://10.10.113.214/hp/device/DeviceStatus/Index'

tag1_sps1 = 'UsagePage.ImpressionsByMediaSizeTable.Print.Letter.Total'
tag2_sps1 = 'SupplyGauge0'
tag3_sps1 = 'SupplyGauge1'


#First URL
response16 = requests.get(url1_sps1)
soup16 = BeautifulSoup(response16.text, 'html.parser')
data16 = soup16.find('td', {'id': tag1_sps1}).text.replace(',', '')

#Second URL
response17 = requests.get(url2_sps1)
soup17 = BeautifulSoup(response17.text, 'html.parser')
data17 = soup17.find('span', {'id': tag2_sps1}).text.replace(',', '')

#Third URL
response18 = requests.get(url3_sps1)
soup18 = BeautifulSoup(response18.text, 'html.parser')
data18 = soup18.find('span', {'id': tag3_sps1}).text.replace(',', '')



#Get the current date 
now = datetime.now()
date_string = now.strftime("%m-%d-%Y")

df = pd.DataFrame({
    'Date' : [date_string]*6,
    'Printer': ['STN2', 'LTL1', 'CLB1', 'SPS2', 'STN1', 'SPS1'],
    'Page Count': [data1, data4, data7, data10, data13, data16],
    'Toner Level': [data2, data5, data8, data11, data14, data17],
    'Maintenance Level': [data3, data6, data9, data12, data15, data18]
    
})



#Load Previous Data from Excel

try:
    prev_df =pd.read_excel('AllPrinters.xlsx')
except FileNotFoundError:
    prev_df =pd.DataFrame()

#Append new data to the previous data
df = pd.concat([prev_df, df], ignore_index=True)

#Write to Excel 
df.to_excel('AllPrinters.xlsx', index=False)



