import urllib.request
import re
import codecs
import time
import gzip
import random

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

def filter_page(url):
    next_page = ""
    title = ""
    txt = ""
    while 1:
        time.sleep(random.randint(2,3))
        try:
            data = urllib.request.urlopen(url, timeout=10)
            byte_str = data.read()
            try:
                temp_str = str(gzip.decompress(byte_str), encoding="utf8")
            except:
                temp_str = str(byte_str, encoding="utf8")
            next_page = temp_str.split("class=\"next\"")[1]
            next_page = next_page.split("href=\"")[-1]
            next_page = next_page.split("\"")[0]

            next_page = "https://www.hytd.com%s" % next_page

            temp_str = temp_str.split("<h1>")[1]
            title = temp_str.split("</h1>")[0]

            temp_str = temp_str.split("<div id=\"content\" deep=\"3\">")[1]
            txt = temp_str.split("<div align")[0]
            break
        except Exception as e:
            print(str(e))
            continue
    return next_page, title, txt

begin = "https://www.hytd.com/12/12440/9133253.html"
end = "https://www.hytd.com/12/12440/"

if __name__ == "__main__":
    current = begin
    i = 1
    while 1:
        print(i)
        current,title,txt = filter_page(current)
        print(current)
        #print(title)
        #print(txt)
        #break
        with codecs.open("./怨气撞铃.txt", "a+", encoding="utf-8") as F:
            F.write("\n\n\t\t\t\t%s\n" % title)
            F.write(txt.replace('&nbsp;', ' ').replace('<br/>', '\n').replace('<p>', '\n').replace('</p>', '\n'))
        if current == end:
            break
        i = i + 1
