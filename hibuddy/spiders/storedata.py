import scrapy
import pandas as pd

class StoredataSpider(scrapy.Spider):
    name = "storedata"
    df = pd.read_csv('store.csv')
    start_urls= df['url'].to_list()

    def parse(self, response):
        store_name = response.xpath('.//h1/text()').get()
        adress= response.xpath('.//address/text()').get()
        phone_number = response.xpath('.//address/a/text()').get()

        products = response.xpath('.//div[@class="infinite-scroll-component "]/article/section/div[1]')
        for product in products:
            product_name = product.xpath('.//h3/text()').get()
            products_desc = product.xpath('.//h1/text()').get()
            quantity_weight = product.xpath('.//p[1]/text()').get()
            store_price = product.xpath('p[2]/text()').getall()
            store_price = (',').join(store_price).replace('Store Price:','').replace(',','').strip()

            yield{
                'Store Name':store_name,
                'Adress':adress,
                'Phone Number':phone_number,
                'Brand':product_name,
                'Product Name':products_desc,
                'Quantity weight':quantity_weight,
                'Store Price':store_price
            }