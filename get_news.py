# from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET
import requests as req 
from url.can_use_rss import rss_list as rss

def jeju_news():
    
    crad_lsit = []
    
    a = rss.jeju

    xl = req.get(a)
    content = xl.content

    root = ET.fromstring(content)
    
    for item in root.findall('./channel/item')[:5]:
        title = item.find('title').text
        where = '제주일보'
        link = item.find('link').text
        
        crad = {
            "title" : title,
            'where' : where,
            'link' : link
        }
        
        crad_lsit.append(crad)
        
    return crad_lsit
    
def jemin_news():
    crad_lsit = []
    
    a = rss.jemin

    xl = req.get(a)
    content = xl.content

    root = ET.fromstring(content)
    
    for item in root.findall('./channel/item')[:5]:
        title = item.find('title').text
        where = '제민일보'
        link = item.find('link').text
        
        crad = {
            "title" : title,
            'where' : where,
            'link' : link
        }
        
        crad_lsit.append(crad)
        
    return crad_lsit
    
def omai_news():
    
    crad_list = []
    
    a =rss.omai
    
    xl = req.get(a)
    content = xl.content

    root = ET.fromstring(content)
    for item in root.findall('./channel/item')[:5]:
        title = item.find('title').text.replace("<br>","").replace("<BR>","")
        where = '오마이'
        link = item.find('link').text
        
        crad = {
            "title" : title,
            'where' : where,
            'link' : link
        }
        
        crad_list.append(crad)
    return crad_list
    
    
print(omai_news())