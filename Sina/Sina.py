from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient
import time

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/1251000504',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 67.0.3396.87 Safari / 537.36',
}

# 这里需要提前创建好‘weibo’数据库
# 并在‘weibo’数据库中创建一个‘weibo’集合
# 我是用mongodb可视化工具Robo 3t手动创建的
client = MongoClient()
db = client['weibo']
collection = db['weibo']


def get_page(page):
    # 这个params参数可以直接从浏览器中复制过来
    # 记得添加一个page参数
    params = {
        'uid': '1251000504',
        'luicode': '10000011',
        'lfid': '100103type=1&q=许嵩',
        'featurecode': '20000320',
        'type': 'uid',
        'value': '1251000504',
        'containerid': '1076031251000504',
        'page': page
    }
    # 动态构造URL
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
    time.sleep(10)  # 休息一下，防止封ip


def parse_page(json):
    items = json.get('data').get('cards')
    for index, item in enumerate(items):
        if page == 1 and index == 1:
            continue
        else:
            item = item.get('mblog')
            weibo = {}
            # weibo['id'] = item.get('id')
            weibo["text"] = pq(item.get('text')).text()
            # weibo['attitudes'] = item.get('attitudes_count')
            # weibo['comments'] = item.get('comments_count')
            # weibo['reposts'] = item.get('reposts_count')
            weibo["time"] = item.get('created_at')
            weibo["from"] = "新浪微博"
            print(weibo)
            f_vae.write(str(weibo) + '\n')


if __name__ == '__main__':
    # 这个42是我算出来的
    # 一共408条微博，每页10条，从1开始计数
    f_vae = open("Sina.txt", 'w', encoding='UTF-8')
    for page in range(1, 42):
        json = get_page(page)
        parse_page(json)
        # print(json)
        # for result in results:
            # print(result)
            # 将结果插入数据库
            # collection.insert(result)