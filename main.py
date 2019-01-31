from scrapy.cmdline import execute

spider_cmd = 'scrapy crawl dytt8_spider -o movies.csv'

execute(spider_cmd.split(' '))