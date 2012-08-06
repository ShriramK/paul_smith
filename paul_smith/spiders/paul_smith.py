from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import random

class PaulSmithSpider(BaseSpider):
	name = "paulsmith"
	domain_name = "paulsmith.co.uk"
	start_urls = ["http://www.paulsmith.co.uk/paul-smith-jeans-253/category.html"]
	
	def parse(self, response):
		open('paulsmith.html', 'wb').write(response.body)
		hxs = HtmlXPathSelector(response)
		sites = hxs.select('//div[@id="product-group-1"]')

		random.shuffle(sites)
		handleFile = open('result.html', 'wb')
		site2 = sites.select('//div[@class="grid c160 product clear"]')
		for subsite in site2:
			hlink = subsite.select('a/@href').extract()
			price = subsite.select('p[@class="price price-GBP"]/text()').extract()
			image = subsite.select('a/img[@class="default"]/@src').extract()
			site3 = subsite.select('.//div[@class="details"]')
			title = site3.select('h3[@class="desc"]/text()').extract()

			handleFile.write('<div><div style="width:150px;float:left;text-align:center">\
<img src="%s" alt=""/><br />\
<p><a href="http://www.paulsmith.co.uk/%s">%s</a><br />%s</p>\
</div></div><br/>' % (''.join(image), ''.join(hlink), ''.join(title), ''.join(price)))
			image =""
			hlink =""
			title =""
			price =""
		handleFile.close()

SPIDER = PaulSmithSpider()
