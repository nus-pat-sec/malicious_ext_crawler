import scrapy

#Class for defining how your spider is gonna work~!
class ExtensionsSpider(scrapy.Spider):
    name = 'extensions'
    start_urls = [
        'https://chrome.google.com/webstore/search/ledger?hl=en&_category=extensions'
        # 'https://chrome.google.com/webstore/search/trezor?hl=en&_category=extensions'
    ]

    # Loop through the urls to retrieve the expected data
    # for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # parsing the data from pages from the list of url
    def parse(self, response):
        # name_extension = response.css('')
        page = response.css('.a-na-d-w').extract()
        yield {'body': page}

        # filename = 'test-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)