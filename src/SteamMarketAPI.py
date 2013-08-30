'''
Created on Aug 29, 2013

@author: Bakkes
'''

import requests
import re
    
class MarketItem:
    
    def __init__(self, appid, item_name):
        self.appid = appid
        self.item_name = item_name
      
    def get_sell_count(self):
        return MarketItem._get_key_count(self.appid, self.item_name)
      
    #Using some ugly regex to parse javascript. Yeah...
    @staticmethod
    def _get_key_count(appid, item_name):
        data = requests.get("http://steamcommunity.com/market/listings/{appid}/{item_name}".format(appid=appid, item_name=item_name))
        match = re.search(r'var line1=\[(.*?)\];', data.text.encode('utf8'))
        allmatches = re.findall("\[\"(.*?)\",(.*?),\"([0-9]*) sold\"\]", match.group(1))
        return sum([int(key[2]) for key in allmatches])
    