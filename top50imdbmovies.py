import requests
import csv
import pprint
import os
from bs4 import BeautifulSoup
import pprint
titlelist=[]
connect=requests.get(""" https://www.imdb.com/chart/top/?ref_=nv_mv_250 """)
soup=BeautifulSoup(connect.text,'html.parser')
elements_title=soup.find_all('td',attrs='titleColumn')
elements_rating=soup.find_all('td',class_='ratingColumn imdbRating')
Movies={}
# print(elements_title[0])
# print(elements_rating[0])

for i in range(len(elements_title)):
    title=elements_title[i].find('a').text
    rating=elements_rating[i].find('strong').text
    Movies[title]=Movies.get(title,rating)
# create_newfile
os.chdir('c:\\Users\\nishi\\Desktop')
with open ('Top_250_Movies_IMDB.csv','w') as newfile:
    Writer=csv.writer(newfile)
    for Movie,Ratings in Movies.items():
        Writer.writerow([Movie,Ratings])
    newfile.close()