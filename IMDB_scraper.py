from __future__ import annotations
import bs4
import requests
import csv
import os


def IMDB_scraper(url):

    soup = bs4.BeautifulSoup(requests.get(url).text,"lxml")
    titles = soup.find_all("td",class_="titleColumn")
    ratings = soup.find_all("td",class_="ratingColumn imdbRating")
    dic = {}
    for title,rating in zip(titles,ratings):
        try:
            dic[title.a.text.strip()] = float(rating.strong.text.strip())
        except:
            dic[title.a.text.strip()] = "None" 
    return dic


def writer(urls):
    path = os.getcwd()
    for url in urls:
        table = IMDB_scraper(urls[url])
        fname = url
        with open(os.path.join(path,fname+'.csv'),'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Title","Rating"])
            for title,rating in table.items():
                writer.writerow([title,rating])
        print(f"{fname} has been made")


if __name__ == "__main__":
    urls = {"trending_movies":"""https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm""",
        "trending_series":"""https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv""",
        "top_100_movies":"""https://www.imdb.com/chart/top/?ref_=nv_mv_250""",
        "top_100_series":"""https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"""}
    writer(urls)
