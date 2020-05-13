import scrapy

from rozetka_items_crape.items import CategoryItem, ProductItem


class HrefsSpider(scrapy.Spider):

    name = 'rozetka_hrefs'
    start_urls = [
        'https://rozetka.com.ua/promo/laughday/',
    ]
    number_of_pages = 0

    # parse promo page and save all categories and link to them
    def parse(self, response):
        global file
        file = open('text.txt', 'w')
        categories = []
        for div in response.css("div.preloader-trigger"):

            name = div.css("span::text").getall()[2].strip()
            href_to_new_catalog = div.css("a::attr(href)").get()
            file.write(name + ' --- ' + href_to_new_catalog + "\n")

            iCategory = CategoryItem()
            iCategory['name'] = name
            iCategory['link'] = href_to_new_catalog


            categories.append(iCategory)

            # for each category parse count of products pages
            for category in categories:
                href_to_new_catalog = category['link']
                yield scrapy.Request(href_to_new_catalog, meta={'category_item': category},
                                     callback=self.parse_count_of_pase_for_category)

    def parse_count_of_pase_for_category(self, response):
        item = response.meta['category_item']
        count_pages = int(response.css("ul.paginator-catalog li span::text").getall()[-1])
        item['count_of_pages'] = count_pages
        page = 0
        links = []

        # for each category create list links that will parse to search products
        while count_pages != 0:
            count_pages -= 1
            page += 1
            href_to_new_catalog_page = item['link'] + "&p={number_of_page}".format(number_of_page=page)
            links.append(href_to_new_catalog_page)

        # loop for category` links
        for link in links:
            href_to_new_catalog_page = link
            yield scrapy.Request(href_to_new_catalog_page, self.parse_items_on_new_page)

    def parse_items_on_new_page(self, response):

        for item in response.css("div.g-i-tile-catalog"):

            name = item.css('a.novisited::text').get().strip().split("(")[0]
            href_to_file = item.css('a.novisited::attr(href)').get()

            if name != "" and href_to_file != "#":
                file.write(name + " " + href_to_file + "\n")

            iProduct = ProductItem()
            iProduct['name'] = name
            iProduct['link'] = href_to_file

            yield iProduct