import urllib.request
import re
import codecs
import time
import gzip
import random
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def process_code(byte_str):
    temp_str = ""
    i = 0
    j = len(byte_str) - 1
    while i < j:
        s = ""
        try:
                s = str(byte_str[i:i + 1], encoding="gbk")
                i = i + 1
        except:
            s = ""
            i = i + 1
        temp_str = temp_str + s
    return temp_str

def filter_page(driver, url):
    next_page = ""
    title = ""
    txt = ""
    while 1:
        time.sleep(random.randint(2,3))
        try:
            driver.get(url)
            temp_str = driver.find_element_by_tag_name("body").get_attribute('innerHTML')
            #print(temp_str)
            next_page = temp_str.split("class=\"page_chapter\"")[1]
            next_page = next_page.split("href=\"")[3]
            next_page = next_page.split("\"")[0]

            next_page = "https://www.biqiuge.com%s" % next_page

            temp_str = temp_str.split("<h1>")[1]
            title = temp_str.split("</h1>")[0]

            temp_str = temp_str.split("<div id=\"content\" class=\"showtxt\">")[1]
            txt = temp_str.split("<script>")[0]
            break
        except Exception as e:
            print(str(e))
            continue
    return next_page, title, txt

begin = "https://www.biqiuge.com/book/10563/7527843.html"
end = "https://www.biqiuge.com/book/10563/"

if __name__ == "__main__":
    chromedriver = "C:\\Users\\Administrator\\PycharmProjects\\downloader\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chromedriver， chrome_options=chrome_options)

    current = begin
    i = 1
    while 1:
        print(i)
        current,title,txt = filter_page(driver, current)

        with codecs.open("./西出玉门.txt", "a+", encoding="utf-8") as F:
            F.write("\n\n\t\t\t\t%s\n" % title)
            F.write(txt.replace('&nbsp;', ' ').replace('<br>', '\n'))
        if current == end:
            break
        i = i + 1
