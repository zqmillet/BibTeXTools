import HTMLParsers

url = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7086418&tag=1'

HTMLParser = HTMLParsers.IEEEXplorePDFPage()
HTMLParser.Parse(url)

if HTMLParser.ExistFullPaper:
    print(HTMLParser.FullPaperPath)



# print("downloading with requests")
# url = 'http://ieeexplore.ieee.org/ielx7/5/7086369/07086418.pdf?tp=&arnumber=7086418&isnumber=7086369'
# r = requests.get(url)
# with open("Qiqi.pdf", "wb") as code:
#     code.write(r.content)

# ref: http://python.usyiyi.cn/python_278/library/argparse.html