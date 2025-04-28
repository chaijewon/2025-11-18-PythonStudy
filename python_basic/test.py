import requests
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

def genieMusic():
    url = f"https://www.10000recipe.com/recipe/list.html?order=reco&page=1"
    response = requests.get(url)
    html = BeautifulSoup(response.content.decode('utf-8','replace'),'html.parser')
    print(html)
    # 제목 추출
    title = html.find("ul", class_="common_sp_list_ul").find_all('div', class_='common_sp_caption_tit')
    image = html.select('ul.common_sp_list_ul img[src*="/recipe/"]')
    print(title)
    print(image)

    total_str = ''
    for i in title:
        #print(i.text)
        total_str+=i.text+" "
    print(total_str)
genieMusic()
