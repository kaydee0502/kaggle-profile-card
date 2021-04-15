import scrapy
import json

class KaggleStripper(scrapy.Spider):
    name = 'sasori'
    def __init__(self,response):
        html = response.text

        selector = scrapy.Selector(text = html)


        self.selector = selector


    def start_requests(self):
        
        main_section = self.selector.css(".kaggle-component").extract()[1]
        print("lol")
        o = c = 0
        third = 0
        for i in range(len(main_section)):
            if main_section[i] == "{":
                o = i
                third+=1
                if third == 2:
                    break
        
        for i in range(len(main_section)):
            if main_section[i] == "}":
                c = i
                

        #print(main_section[o:c+1])
        return main_section[o:c+1]



    def parse(self, response):
        
        item = {}
        title = response.css('title::text').get()
        item['title'] = title
        yield item
