# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter
# csv_headers = ['name','time','type']
# with open('maoyan.csv', 'w', encoding='utf8')as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(csv_headers)


class MaoyanPipeline:
    def open_spider(self, spider):
        self.f = open('maoyan.csv', 'w+', encoding='utf8')


    def process_item(self, item, spider):

        f_csv = csv.writer(self.f)
        print(item)
        f_csv.writerows([item["title"],item["p_type"],item["p_time"]])

        return item

    def close_spider(self, spider):
        self.f.close()