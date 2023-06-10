import scrapy
from scrapy.http import Request, FormRequest
import weakref
import os
import weakref
import webbrowser
import tempfile
from twisted.web import http
from w3lib import html
from scrapy.utils.response import open_in_browser


class MoodleSpider(scrapy.Spider):
    name = 'moodle'
    start_urls = {
            "https://moodle.cu.edu.ng/login/index.php/"
    }

    # def parse(self, response, **kwargs):
    #     login = response.css("span.login a::attr(href)").get()
    #     yield response.follow(login, callback=self.log_in)
    def start_requests(self):
        login_url = "https://moodle.cu.edu.ng/login/index.php/"
        yield scrapy.Request(login_url, callback=self.login)

    def login(self, response):
        yield FormRequest.from_response(response, formdata={
                     'username': '19cg026486',
                     'password': 'demi1234',
                     'credentialId': ''
                 }, callback=self.start_scraping)

    # def parse(self, response, **kwargs):
    #     return FormRequest.from_response(response, formdata={
    #         'username': '19cg026486',
    #         'password': 'demi1234',
    #         'credentialId': ''
    #     }, callback=self.start_scraping)

    def start_scraping(self, response):
        print(response.css('title::text').extract_first())