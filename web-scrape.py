import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlalchemy 

url = 'https://www.skyscrapercenter.com/buildings'

response = requests.get(url)

print(response)

#  create a soup object - we want to store all of the html elements 
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup) 

#  start point
#  we search the entire table where the value we are looking for "shanghai" is stored
#  "table" is <table>, id =id and the id name is buildingsTable
#  in the table body - tbody, we want to find all the table rows - tr
results = soup.find('table', {'id' : 'buildingsTable'}).find('tbody').find_all('tr')
len(results)


# name
print(results[0].find_all('td')[1].get_text().strip())
print(results[0].find_all('td')[2].get_text().strip())
print(results[0].find_all('td')[3].get_text().strip())
print(results[0].find_all('td')[4].get_text().strip())
print(results[0].find_all('td')[5].find_all('p')[0].get_text()) # grabs the height in metres and not feet [1]
print(results[0].find_all('td')[6].get_text().strip())
print(results[0].find_all('td')[7].get_text().strip())
print(results[0].find_all('td')[8].get_text().strip())