#coding = utf-8
import requests
from lxml import etree
import re
from selenium import webdriver

driver = webdriver.PhantomJS()

url = 'http://www.tongqu.me'
driver.get(url)
html = driver.page_source
pattern = re.compile(r'(.*)?(\d){1,3}(.*)?')

selector = etree.HTML(html)
# neirong = selector.xpath('//div[contains(@class,"body")]/tq-one-act/div[contains(@class,"one-home-act ng-isolate-scope")]/div[contains(@class,"bottom")]/div[contains(@class,"name ng-binding")]/text()')
neirong = selector.xpath('//div[contains(@class,"body")]/tq-one-act/div[contains(@class,"one-home-act ng-isolate-scope")]/div[contains(@class,"bottom")]')

for i in range(0,10):
    wenben = neirong[i].xpath('string(.)')
    wenben = wenben.replace('\n','')
    renshu = pattern.match(wenben)
    print wenben
    print renshu.group(2)
