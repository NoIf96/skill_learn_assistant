# -*- coding:utf-8 -*-
import time
import pymongo
import requests
from bs4 import BeautifulSoup
from utils.data.manager.mongo.manager import Manager
from utils.worm import logger


def update_introduction(tab_name):
    manager = Manager(db_name="item_datas", tab_name=tab_name)
    tab = manager.tab
    items = list(tab.find())
    count = 0
    fail_list = []
    for item in items:
        try:
            if item["introduction"] == "" or item["introduction"] == "-":
                introduction = get_one_introduction(item["name"])
                item["introduction"] = introduction
                tab.update_one({"name": item["name"]}, {"$set": item})
                count += 1
                time.sleep(3)
        except Exception as e:
            fail_list.append(item["name"])
            logger.exception(e)
            continue
    return count, fail_list


def get_one_introduction(name, url=""):
    try:
        introduction = get_one_data(name, url)
        return introduction
    except Exception as e:
        logger.exception(e)
        return "-"


def get_one_data(name, url=""):
    url = f"https://baike.baidu.com/item/{name}" if url == "" else url
    response = get_response(url)
    soup = BeautifulSoup(response, "lxml")
    items = soup.select(
        "body > div.body-wrapper > div.content-wrapper > div > div.main-content > div.lemma-summary"
    )
    content = items[0].get_text()
    # 移除首行换行
    content = content.replace("\n", "", 1)
    # 移除引用记号
    content = (
        content.replace("[1]", "")
        .replace("[2]", "")
        .replace("[3]", "")
        .replace("[4]", "")
    )
    # 拼接百度链接
    content = content + "\n百度百科：" + url
    return content


def get_response(url):
    headers = {
        "Cookie": "BIDUPSID=A2DE86B015ABE0B56ECCD3918BD9C23F; PSTM=1512189939; __cfduid=d915169593110ec91971072d8378fe51c1527000517; BAIDUID=67974100468048242665A6E8F22D0E76:FG=1; MCITY=-340%3A; BDUSS=zNZc2VnZUNrREREdUE5elRJZjVwcUZlM0l-djllbUo4YTRldVpSUEdRaGl6R0pjQVFBQUFBJCQAAAAAAAAAAAEAAAA3L28boey346HsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGI~O1xiPztcY; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1462_28940_21104_28775_28720_28963_28834_28585_26350_20718; delPer=0; PSINO=6; locale=zh; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1556892572; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1556892572; pgv_pvi=7320494080; pgv_si=s6264338432; BK_SEARCHLOG=%7B%22key%22%3A%5B%22mongodb%22%5D%7D",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Host": "baike.baidu.com",
    }
    return requests.get(url, headers=headers).content
