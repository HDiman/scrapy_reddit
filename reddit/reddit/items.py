# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditItem(scrapy.Item):
    # define the fields for your item here like:
    titles = scrapy.Field()
    hrefs = scrapy.Field()
    scores = scrapy.Field()
