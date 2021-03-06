# MoeSpider
Python 轻量级多线程爬虫实现，抓取页面需要编写HtmlParser的解析逻辑

## Python版本：
 - Python 3

## 项目结构：
 - CoreSpider：控制爬虫的整体逻辑，负责调用其他模块
 - HtmlParser：使用BeautifulSoup解析HTML页面，通过对HTML标签及其属性的选择，获取所有目标的名称和链接
 - Item：每一个目标是一个Item对象，包含有url和name属性
 - TaskManager：使用一个线程安全的队列保存任务
 - MultiThreadFileDownloader：从任务队列中不断取出Item对象，下载并命名、保存到指定位置，下载支持多线程

![项目结构](./document/crawler-infrastructure.png)

## 用到的模块
 - 第三方模块 BeautifulSoup
 - 内置模块 urllib.request（在Python2.X版本为urllib2）、queue等

## 多线程支持
TaskManager维护两个线程安全队列：待下载网页任务、待下载文件任务
放入速度 > 取出速度 可以缓冲，放入速度 < 取出速度 执行取出行为线程阻塞，无阻塞超时
MultiThreadHtmlPageDownloader、HtmlParser从TaskManager取出待下载网页任务，下载解析出新链接添加到TaskManager指定的队列中
下载网页和下载文件都是多线程执行