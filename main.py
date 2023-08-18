import requests
from bs4 import BeautifulSoup

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def tettt():
    return {"test": "1111"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def testfunc(a=1, b=2):
    return a - b


# print(testfunc(1, 4))


def func2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }
    for start_aum in range(0, 250, 25):
        response = requests.get(f'https://movie.douban.com/top250?start={start_aum}', headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        all_titles = soup.findAll('span', attrs={'class': 'title'})
        for title in all_titles:
            title_string = title.string
            if '/' not in title_string:
                pass
                # print(title.string)
