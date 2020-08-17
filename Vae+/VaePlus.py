import re
import requests
from bs4 import BeautifulSoup
import time

if __name__ == '__main__':
    base_url = "https://m-xusong.taihe.com/posts/"
    time_start = time.time()
    for i in range(100):
        url = base_url+str(i)
        r = requests.get(url)
        print(r)

    time_end = time.time()
    print('totally cost', time_end - time_start)
