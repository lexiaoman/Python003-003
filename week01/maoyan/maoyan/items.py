# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    p_type = scrapy.Field()
    p_time = scrapy.Field()

    pass