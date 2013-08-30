'''
Created on Aug 29, 2013

@author: Bakkes
'''

from SteamMarketAPI import MarketItem

csgo_id = 730
items = ["CS:GO Case Key", "eSports 2013 Key", "CS:GO Weapon Case", "eSports 2013 Case"]
for item in items:
    marketitem = MarketItem(csgo_id, item)
    print "{item_name}. Units sold: {units}".format(item_name=item, units=marketitem.get_sell_count())