# -*- coding: utf-8 -*-

# import scrapy  # 可以写这句注释下面两句，不过下面要更好
from scrapy.spiders import Spider
from scrapy.selector import Selector
from video_hunt.items import VideoItem  # 此处如果报错是pyCharm的原因
from scrapy import Request

class VideoSpider(Spider):
    name = "video"
    allowed_domains = ["byzfwl.zdqbrya.9izhuiju.com"]  # 允许爬取的域名，非此域名的网页不会爬取
    home = "http://byzfwl.zdqbrya.9izhuiju.com"

    start_urls = [
        "http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/detail/id/53349.html"  # 起始url，此例只爬这个页面
    ]

    # 用来保持登录状态，可把chrome上拷贝下来的字符串形式cookie转化成字典形式，粘贴到此处
    cookies = {}

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        # 'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    def parse(self, response):
        selector = Selector(response)  # 创建选择器
        table = selector.xpath('/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/ul[2]//li')  # 取出所有的楼层
        if not table:
            # 无法访问该链接
            self.badUrl(response)
            return
        for each in table:  # 对于每一个楼层执行下列操作
            item = VideoItem()  # 实例化一个Item对象
            item['title'] = each.xpath('a/text()').extract()[0]
            item['url'] = self.home + str(each.xpath('a/@href').extract()[0])
            yield item  # 将创建并赋值好的Item对象传递到PipeLine当中进行处理




    '''
    description: 返回下次迭代的url
    :param oldUrl: 上一个爬去过的url
    :return: 下次要爬取的url
    '''
    def get_next_url(self, oldUrl):
        # 传入的url格式：http://www.heartsong.top/forum.php?mod=viewthread&tid=34
        l = oldUrl.split('=')  #用等号分割字符串
        oldID = int(l[2])
        newID = oldID - 1
        if newID == 0:  # 如果tid迭代到0了，说明网站爬完，爬虫可以结束了
            return
        newUrl = l[0] + "=" + l[1] + "=" + str(newID)  #构造出新的url
        return str(newUrl)  # 返回新的url

    """
    这是一个重载函数，它的作用是发出第一个Request请求
    :return:
    """
    def start_requests(self):
        # 带着headers、cookies去请求self.start_urls[0],返回的response会被送到
        # 回调函数parse中
        yield Request(self.start_urls[0],
                             callback=self.parse, headers=self.headers,
                             cookies=self.cookies, meta=self.meta)

    # 遇到无法访问的链接
    def badUrl(self, response):
        # 这个链接内没有一个楼层，说明此主题贴可能被删了，
        # 把这类url保存到一个文件里，以便审查原因
        print("bad url!")
        f = open('badurl.txt', 'a')
        f.write(response.url)
        f.write('\n')
        f.close()

    """
    用以处理主题贴的首页
    :param response:
    :return:
    """

    """
    def parse(self, response):
        selector = Selector(response)  # 创建选择器

        table = selector.xpath('//*[starts-with(@id, "pid")]')  # 取出所有的楼层
        if not table:
            # 无法访问该链接
            self.badUrl(response)
            # 发起下一个主题贴的请求
            next_url = self.get_next_url(response.url)  # response.url就是原请求的url
            if next_url != None:  # 如果返回了新的url
                yield Request(next_url, callback=self.parse, headers=self.headers,
                                cookies=self.cookies, meta=self.meta)
            return
        for each in table:
            item = VideoItem()  # 实例化一个item
            # 因为后来我在论坛里删除了大量的机器回帖，所以有的楼层里没有作者信息
            try:
                # 通过XPath匹配信息，注意extract（）方法返回的是一个list
                item['author'] = each.xpath('tr[1]/td[@class="pls"]/div[@class="pls favatar"]/div[@class="pi"]/div[@class="authi"]/a/text()').extract()[0]
                item['post_time'] = each.xpath('tr[1]/td[@class="plc"]/div[@class="pi"]').re(r'[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+:[0-9]+')[0]
            except:
                continue
            # XPath的string(.)用法，解决标签套标签的情况，具体解释请自行找XPath教程
            content_list = each.xpath('.//td[@class="t_f"]').xpath('string(.)').extract()
            content = "".join(content_list)  # 将list转化为string
            item['url'] = response.url  # 用这种方式获取网页的url
            # 把内容中的换行符，空格等去掉
            item['content'] = content.replace('\r\n', '').replace(' ', '').replace('\n', '')
            yield item  # 将创建并赋值好的Item对象传递到PipeLine当中进行处理

        pages = selector.xpath('//*[@id="pgt"]/div/div/label/span')
        if pages:  # 如果pages不是空列表，说明该主题帖分页
            pages = pages[0].re(r'[0-9]+')[0]  # 正则匹配出总页数
            print("This post has", pages, "pages")
            # response.url格式： http://www.heartsong.top/forum.php?mod=viewthread&tid=34
            # 子utl格式： http://www.heartsong.top/forum.php?mod=viewthread&tid=34&page=1
            tmp = response.url.split('=')  # 以=分割url
            # 循环生成所有子页面的请求
            for page_num in range(2, int(pages) + 1):
                # 构造新的url
                sub_url = tmp[0] + '=' + tmp[1] + '=' + tmp[2] + 'page=' + str(page_num)
                # 注意此处的回调函数是self.sub_parse,就是说这个请求的response会传到
                # self.sub_parse里去处理
                yield Request(sub_url,callback=self.sub_parse, headers=self.headers,
                                cookies=self.cookies, meta=self.meta)

        # 发起下一个主题贴的请求
        next_url = self.get_next_url(response.url)  # response.url就是原请求的url
        if next_url != None:  # 如果返回了新的url
            yield Request(next_url,callback=self.parse, headers=self.headers,
                        cookies=self.cookies, meta=self.meta)
                        
    """

    """
    用以爬取主题贴除首页外的其他子页
    :param response:
    :return:
    """
    def sub_parse(self, response):
        selector = Selector(response)
        table = selector.xpath('//*[starts-with(@id, "pid")]')  # 取出所有的楼层
        for each in table:
            item = VideoItem()  # 实例化一个item
            try:
                # 通过XPath匹配信息，注意extract（）方法返回的是一个list
                item['author'] = each.xpath('tr[1]/td[@class="pls"]/div[@class="pls favatar"]/div[@class="pi"]/div[@class="authi"]/a/text()').extract()[0]
                item['post_time'] = each.xpath('tr[1]/td[@class="plc"]/div[@class="pi"]').re(r'[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+:[0-9]+')[0]
            except:
                continue
            content_list = each.xpath('.//td[@class="t_f"]').xpath('string(.)').extract()
            content = "".join(content_list)  # 将list转化为string
            item['url'] = response.url  # 用这种方式获取网页的url
            # 把内容中的换行符，空格等去掉
            item['content'] = content.replace('\r\n', '').replace(' ', '').replace('\n', '')
            yield item  # 将创建并赋值好的Item对象传递到PipeLine当中进行处理



