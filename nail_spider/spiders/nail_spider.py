import scrapy
from selenium import webdriver
import time
from scrapy.selector import Selector
import urllib
from .crop import crop_img

from scrapy.http.request import Request

class nail_spider(scrapy.Spider):
    name = 'nails'

    start_urls = [
        'https://gelato.im/designs'
    ]

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = webdriver.Chrome(r"C:\Users\saltuscorp\chromedriver.exe")

    def parse(self, response):
        self.browser.get(response.url)
        time.sleep(5)

        match = False
        lenOfPage = 0
        idx = 0
        prev_tag_length = 0
        curr_tag_length = 0
        while (match == False):
            time.sleep(3)
            tag_count = 20
            start_range = idx * tag_count
            end_range = start_range + tag_count

            html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
            selector = Selector(text=html)
            curr_tag_length = len(selector.xpath("//div[@class='_1IL-bGgINLpqKlfQmQsBHM']"))
            print("curr_tag_length:", curr_tag_length, "prev_tag_length", prev_tag_length)
            if(curr_tag_length > prev_tag_length):
                 for i in range(start_range, end_range):

                    src_url = selector.xpath(
                        "//div[@class='RGUjoiOc9VBagw8NkPgAr']/div/div[" + str(i + 1) + "]/a/img/@src").extract_first()
                    tags = selector.xpath(
                        "//div[@class='RGUjoiOc9VBagw8NkPgAr']/div/div[" + str(i + 1) + "]/a/img/@alt").extract_first()
                    design_link = selector.xpath(
                        "//div[@class='RGUjoiOc9VBagw8NkPgAr']/div/div[" + str(i + 1) + "]/a/@href").extract_first()
                    print(src_url)
                    url_split = src_url.split("/")
                    file_name = url_split[len(url_split) - 1]
                    print(file_name)
                    image_folder = "crawled_img2"
                    id = design_link.split('/')[len(design_link.split('/'))-1]

                    urllib.request.urlretrieve(src_url, image_folder + "/" + file_name)
                    crop_img(image_folder, file_name)
                    # print(src_url)
                    yield {
                        # "image_url": src_url,
                        "index": i,
                        "id": id,
                        "file_name": file_name,
                        "tags": tags,
                        "design_link": design_link
                    }

            prev_tag_length = curr_tag_length

            print(idx, "Tag count:", len(selector.xpath("//div[@class='_1IL-bGgINLpqKlfQmQsBHM']")), "start_range", start_range, "end_range", end_range)
            lenOfPage = self.browser.execute_script(
                "window.scrollTo("+str(lenOfPage)+", document.body.scrollHeight);"+
                "var lenOfPage=document.body.scrollHeight;"+
                "return lenOfPage;")
            idx += 1
            if idx == 2000:
                match = True

        # html = self.browser.find_element_by_xpath('//*').get_attribute('outerHTML')
        # selector = Selector(text=html)
        # for nail in selector.xpath("//div[@class='_1IL-bGgINLpqKlfQmQsBHM']"):
        #     src_url = nail.xpath(".//a/img/@src").extract_first()
        #     tags = nail.xpath(".//a/img/@alt").extract_first()
        #     design_link = nail.xpath(".//a/@href").extract_first()
        #
        #     url_split = src_url.split("/")
        #     file_name = url_split[len(url_split) - 1]
        #     print(file_name)
        #     image_folder = "crawled_img"
        #
        #     urllib.request.urlretrieve(src_url, image_folder + "/" + file_name)
        #     crop_img(image_folder, file_name)
        #     # print(src_url)
        #     yield {
        #         #"image_url": src_url,
        #         "file_name": file_name,
        #         "tags": tags,
        #         "design_link": design_link
        #     }
        # for i in range(20):
        #     src_url = selector.xpath(
        #         "//div[@class='RGUjoiOc9VBagw8NkPgAr']/div/div[" + str(i + 1) + "]/a/img/@src").extract_first()
        #     tags = selector.xpath(
        #         "//div[@class='RGUjoiOc9VBagw8NkPgAr']/div/div[" + str(i + 1) + "]/a/img/@alt").extract_first()
        #     design_link = selector.xpath(
        #         "//div[@class='RGUjoiOc9VBagw8NkPgAr']/div/div[" + str(i + 1) + "]/a/@href").extract_first()
        #     url_split = src_url.split("/")
        #     file_name = url_split[len(url_split) - 1]
        #     print(file_name)
        #     image_folder = "crawled_img"
        #
        #     urllib.request.urlretrieve(src_url, image_folder + "/" + file_name)
        #     # crop_img(image_folder, file_name)
        #     # print(src_url)
        #     yield {
        #         # "image_url": src_url,
        #         "file_name": file_name,
        #         "tags": tags,
        #         "design_link": design_link
        #     }