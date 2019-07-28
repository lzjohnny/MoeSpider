from spider.Config import FILE_DL_SLEEP
import threading
import time
import urllib.request
import os


class MultiThreadFileDownloader(threading.Thread):
    def __init__(self, taskManager, threadName):

        threading.Thread.__init__(self)
        self.taskManager = taskManager
        self.threadName = threadName
        self.dirname = 'downloads'
        self.createdir()

    def createdir(self):
        if not os.path.exists(self.dirname):
            os.mkdir(self.dirname)

    def run(self):
        self.download()
        print(str(self.threadName) + '线程停止')

    def download(self):
        # Python不支持 while (item = self.taskManager.getFileItem()) != None 语法
        # Python赋值语句无返回值（Java中赋值语句返回所赋的值）
        item = self.taskManager.getFileItem()
        while item != None:
            print(str(self.threadName) + '线程当前item：' + str(item))
            url = item.url
            name = item.name

            print(str(self.threadName) + '线程当前下载图片：' + name)
            filePath = self.dirname + os.sep + name + '.jpg'
            urllib.request.urlretrieve(url, filePath)

            item = self.taskManager.getFileItem()

            time.sleep(FILE_DL_SLEEP)