from bs4 import BeautifulSoup
from bs4 import element
import Item

# 对于指定的HTML页面进行解析，抽取出要抓取图片的url和name
# 保存在Item对象中，Item对象保存在一个“线程安全”队列中
# 生产者-消费者模型

class HtmlParser(object):

    '''
    每一个HtmlParser对象中保存了要解析的HTML页面
    parser = HtmlParser(html)
    parser.parse()
    '''
    def __init__(self, html, taskManager):
        # super().__init__()
        self.html = html
        self.taskManager = taskManager

    def parse(self):
        # soup = BeautifulSoup(open('D:/kancolle.html', encoding='utf-8'), 'html.parser')
        soup = BeautifulSoup(self.html, 'html.parser')
        # print(soup.prettify())
        trTag = soup.find_all('tr', valign='bottom')
        for tr in trTag:  # tr是bs4.element.Tag类型
            for td in tr.children:
                if isinstance(td, element.NavigableString):
                    continue
                if td.__len__() == 1:
                    continue
                # print(td.contents[1].contents[0]) # 第一个<a>节点，含有src链接
                # name = td.contents[2].contents[0].string  # 第二个<a>节点，内容为文件名称，No.001 长门
                name = td.contents[3].string
                srcset = (td.contents[1].contents[0])['srcset'] # srcset属性
                url = srcset.split(' ', 1)[0]

                item = Item.Item(url, name)
                self.taskManager.add(item)

                # print(name)
                # print(url)
        return None