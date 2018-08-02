# coding=utf-8

from bs4 import BeautifulSoup
import requests
from test import db, Weather


def get_list_by_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    weathers = soup.select("#tool_site")
    title = weathers[1].select("h3")[0].text  # 每个月份天气的标题
    weather_infors = weathers[1].select("ul")[1:]  # 去掉表头
    for weatherInfor in weather_infors:
        li_list = list()
        for li in weatherInfor.select('li'):
            li_list.append(li.text)

        weather = Weather()
        weather.title = title
        weather.date = li_list[0]
        weather.highest_temperature = li_list[1]
        weather.lowest_temperature = li_list[2]
        weather.weather = li_list[3]
        weather.wind_vane = li_list[4]
        weather.wind_power = li_list[5]
        db.session.add(weather)
        db.session.commit()


def getListByAddress(addressUrl):
    url = addressUrl
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    dates = soup.select(".tqtongji1 ul li a")
    url_list = set()
    for d in dates:
        url_list.add(d['href'])
    return url_list


def get_url_list():
    addresses = BeautifulSoup(requests.get('http://lishi.tianqi.com/').text, "html.parser")
    queryAddress = addresses.find_all('a', text="昆明")
    url_list = set()
    for q in queryAddress:
        url_list = url_list | getListByAddress(q['href'])  # 取并集
    return url_list
