#!usr/bin/python
# -*- coding:utf-8 -*-
"""
爬取这个网站的视频
"""
import requests
import logging
import re
from requests.exceptions import RequestException
from lxml import etree
logger = logging.INFO


url = u"http://www.01kmm.com:8888/video/2018-10/38183.html"
# url = u"https://www.baidu.com/"
# <source class="src" src="https://201806.53didi.com/20181017/1/1/xml/91_6cae9b82808945fe9badbb6c94f08ab0.mp4" type="video/mp4; codecs=&quot;avc1.42E01E, mp4a.40.2&quot;">
video_url = u"https://201806.53didi.com/20181017/1/1/xml/91_6cae9b82808945fe9badbb6c94f08ab0.mp4"
root_url = u"http://www.12kmm.com:8888/diao/se57.html"
one_url = u"http://www.12kmm.com:8888"

# <object id="videoPlayer" width="100%" height="100%" align="middle" data="http://resources.baomihua.com/swf/bd_video_player.swf?flvid=36856408&amp;qudao=baiduVideo" type="application/x-shockwave-flash" style="opacity: 1;"> <param name="wmode" value="direct"> <param name="allowscriptaccess" value="always"> <param name="allowfullscreen" value="true"><div class="no-flash-tips">您的flash可能被禁用或版本过低,为了能够正常观看视频，请您<a href="http://get.adobe.com/cn/flashplayer/?no_redirect" target="_blank" class="a-flash-link">点这里启用Flash</a></div></object>
def get_main_page_response():
    try:
        response = requests.get(url=root_url)
        if response.status_code == 200:
            doc_tree = response.text
            return doc_tree
    except RequestException:
        print(u"get page fail!!!!!!!!!!!!!!!!!!")

def parser_response(page):
    container = {}
    page_source = etree.HTML(page)
    #//*[@id="container"]/div[1]
    # for ele in page_source.xpath('//div[@class="videos"]'):
    #     print(ele.xpath('//a/@href'))
    print(page_source.xpath('//div[@class="videos"]//a/@href'))
    urls = page_source.xpath('//div[@class="videos"]//a/@href')
    return urls

def parser_video_response(urls):
    for url in urls:
        url = one_url+url
        response_text = requests.get(url).text
        page_source = etree.HTML(response_text)
        final_url = page_source.xpath('//video//a/@href')
        print(final_url)



def write_into_file():
    pass


def main():
    urls = parser_response(get_main_page_response())
    parser_video_response(urls)



if __name__ == '__main__':
    main()
