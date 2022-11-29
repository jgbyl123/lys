from urllib.request import urlopen
import os

encoding="utf-8"

url = input("请输入要抓取的URL：")

a = urlopen(url)
print(a.read())

resp = urlopen(url)
with open("./URL-html/myurl.htm",mode="w") as f:
    f.write(resp.read().decode("utf-8"))

print("over!")
