from django.core.management.base import BaseCommand
from rozetka_items_crape.spiders import HrefsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(HrefsSpider)
        process.start()
