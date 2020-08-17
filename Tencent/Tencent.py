import re
import requests
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
    f_vae = open('Tencent.txt', 'a', encoding='UTF-8')
    base_url = "http://t.qq.com/vaemusic"
    next_url = "http://t.qq.com/vaemusic?pref=qqcom.dp.followalltx1"
    # next_url = "http://t.qq.com/vaemusic?mode=0&id=23066122259515&pi=15&time=1301028830"
    cnt = 1
    pattern = re.compile("下一页")
    while True:
        r = requests.get(next_url)
        soup = BeautifulSoup(r.text, 'lxml')  # lxml为解析器
        href = soup.find_all('a', attrs={'class': 'pageBtn'}, text=pattern)
        soup = soup.find('ul', attrs={'id': 'talkList'})
        texts = soup.find_all('div', attrs={'class': 'msgCnt'})
        times = soup.find_all('a', attrs={'class': 'time'})
        for (i, value) in enumerate(texts):
            tencent = {}
            tencent['text'] = texts[i].text
            tencent['time'] = times[i].text
            tencent['from'] = '腾讯微博'
            f_vae.write(str(tencent) + '\n')
        print(next_url)
        # if href[0].text == "上一页":
        if cnt >= 15:
            break
        #     next_url = base_url + href[1]['href']
        # else:
        for url in href:
            next_url = base_url + url['href']
        cnt += 1
        time.sleep(20)



    # fs = open('vae.txt', 'w', encoding='UTF-8')
# print(soup)
# print("------------")

