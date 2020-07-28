import re
from urllib import request


class Spider():

    url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1595577438230_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&sid=&word=%E6%8A%BD%E7%83%9F%E5%9B%BE%E7%89%87&f=3&oq=%E6%8A%BD%E7%83%9F&rsp=0"
    root_pattern = '<a href="(.*)" <img class=>'
    # root_pattern2 = 'src=([\s\S]*?)data-default'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding="utf-8")
        # print(htmls)
        # exit()
        # a = 1
        return htmls

    def __analysis(self,htmls):

        root_html=re.findall(Spider.root_pattern,htmls)
        # img=[]
        # for html in root_html:
        #     img_address = re.findall(self.root_pattern2,html)
        #     img.append(img_address)
        print(root_html)

    def go(self):
        htmls=self.__fetch_content()
        self.__analysis(htmls)


if __name__ == '__main__':

    spider = Spider()
    spider.go()