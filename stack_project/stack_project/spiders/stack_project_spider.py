from scrapy import Spider

class StackProject(Spider):
    name = "stack_project"
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]