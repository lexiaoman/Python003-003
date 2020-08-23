# https://maoyan.com/films?showType=3

import requests
from bs4 import BeautifulSoup
from scrapy import Selector
import csv

csv_headers = ['name','time','type']
def get_data():

    cookies = {
        'uuid_n_v': 'v1',
        'uuid': 'D38561B0E53611EA98CDEF49A2769730BBBFB73312C444A3A3B7911B98B36390',
        '_csrf': '46a89a38ec6aadb3a012b964ea436ec6d414dde137f977f8b4a42463488ceafd',
        'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1598183427',
        'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1598183427',
        '_lxsdk_cuid': '1741b27ca6ec8-0e2e0db6b3e5f7-1333062-384000-1741b27ca6e24',
        '_lxsdk': 'D38561B0E53611EA98CDEF49A2769730BBBFB73312C444A3A3B7911B98B36390',
        'mojo-uuid': '47759c916b4b4256108fd902f7964afb',
        'mojo-session-id': '^{^\\^id^\\^:^\\^2fb100458b3d119d94cb3572672775dc^\\^,^\\^time^\\^:1598183426710^}',
        '__mta': '45905563.1598183426736.1598183426736.1598183426736.1',
        'mojo-trace-id': '3',
        '_lxsdk_s': '1741b27ca70-de3-9f0-693^%^7C^%^7C2',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('showType', '3'),
    )

    response = requests.get('https://maoyan.com/films', headers=headers, params=params, cookies=cookies)
    return response.text
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://maoyan.com/films?showType=3', headers=headers, cookies=cookies)


def params_data(html):
    data = Selector(text=html)
    content = data.xpath("//div[@class='movie-item film-channel']")

    base_list = []
    for num,i in enumerate(content[:10]):

        title = i.xpath('.//span[@class="name "]/text()').extract_first()
        p_time = i.xpath('.//div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1].strip()
        p_type = i.xpath('.//div[@class="movie-hover-title"]/text()').extract()[4].strip()
        print(title)
        print(p_time)
        print(p_type)
        base_list.append([title,p_time,p_type])
    to_csv(base_list)

def to_csv(data_list):
    with open('maoyan.csv', 'w',encoding='utf8')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(csv_headers)
        f_csv.writerows(data_list)



if __name__ == '__main__':
    with open(r"C:\Users\Administrator\Desktop\Maoyan\maoyan.html","r",encoding='utf8') as f:
        data = f.read()
        params_data(data)
