import requests
import csv
import os
from bs4 import BeautifulSoup



def Tvseries(filename,path):

    os.chdir(path)
    connect=requests.get("""https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv""")
    soup=BeautifulSoup(connect.text,'html.parser')
    elements_title=soup.find_all('td',attrs='titleColumn')
    elements_rating=soup.find_all('td',class_='ratingColumn imdbRating')
    Tv_Series={}


    for i in range(len(elements_title)):
        title=elements_title[i].find('a').text
        try:
            rating=elements_rating[i].find('strong').text
        except:
            rating="None"
        Tv_Series[title]=Tv_Series.get(title,rating)
    

    with open (filename,'w') as newfile:
        Writer=csv.writer(newfile)
        for Movie,Ratings in Tv_Series.items():
            Writer.writerow([Movie,Ratings])
        newfile.close()


if __name__ == "__main__":

    try:
        filename=input("Please enter a name for the file to be stored:\n")+".csv"
        path=input('Enter the path you want to store the file:\n')
        Tvseries(filename,path)
        print("Done")

    except:
        filename='Trending_Tv_Series_IMDB.csv'
        path=os.path.join(os.environ["HOMEPATH"], "Desktop")
        Tvseries(filename,path)
        print("Done!")
