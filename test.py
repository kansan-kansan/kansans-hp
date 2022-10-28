#https://kajiblo.com/python-file-write/#:~:text=1%20%E6%96%B0%E8%A6%8F%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%81%BF%E6%99%82%E3%81%AFwith%20open%20%28%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%90%8D%2C%20mode%20%3D%20%22w%22%29%20as,%22a%22%29%20as%20f%3A%203%20with%E3%80%80open%E3%82%92%E4%BD%BF%E3%81%86%E3%81%A8%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%AF%E3%83%AD%E3%83%BC%E3%82%BA%E5%BF%98%E3%82%8C%E3%81%8C%E3%81%AA%E3%81%8F%E3%82%BD%E3%83%BC%E3%82%B9%E3%82%82%E8%A6%8B%E3%82%84%E3%81%99%E3%81%8F%E3%81%AA%E3%82%8B%E3%80%82%204%20open%E3%81%AE%E3%83%A2%E3%83%BC%E3%83%89%E2%80%9Dw%E2%80%9D%E3%81%AF%E5%B8%B8%E3%81%AB%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E6%96%B0%E8%A6%8F%E4%BD%9C%E6%88%90%E3%81%97%E3%81%A6%E6%9B%B8%E3%81%8D%E8%BE%BC%E3%82%80%E3%80%82%20%E3%81%9D%E3%81%AE%E4%BB%96%E3%81%AE%E3%82%A2%E3%82%A4%E3%83%86%E3%83%A0
#https://atmarkit.itmedia.co.jp/ait/articles/2111/02/news019.html
import time

now = time.ctime()
cnvtime = time.strptime(now)


while True:
    nyuurtyoku = str(input(">>"))
    if nyuurtyoku == "a":
        with open("./sample.txt", "a",encoding='utf-8') as txt:
            now = time.ctime()
            cnvtime = time.strptime(now)
            txt.write("\n\n入力:a")
            txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))


    elif nyuurtyoku == "b":
        with open("./sample.txt", "a",encoding='utf-8') as txt:
            now = time.ctime()
            cnvtime = time.strptime(now)
            txt.write("\n\n入力:b\n")
            txt.write(time.strftime("%Y/%m/%d %H:%M:%S", cnvtime))
    elif nyuurtyoku == "q":
        break
