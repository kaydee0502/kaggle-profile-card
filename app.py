import flask 
from flask import request, jsonify, render_template, Markup, make_response
import requests
import json
import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from scrapy.crawler import CrawlerRunner
from spider import KaggleStripper
from styles import tier_colour
from html_local import KaggleStyles


app = flask.Flask(__name__)



@app.route("/")
def index():
    return "Heya"



    
@app.route("/api",methods=["GET"])
def api():
    if "user" in request.args:
        complete_url = "https://kaggle.com/"+request.args["user"]
        response = requests.get(complete_url)
        kstyle = KaggleStyles()
        if response.status_code == 200:
            crawler = KaggleStripper(response)
            data = crawler.start_requests()
            sdata = ''.join(list(data))

            print(sdata)
            sdata = sdata.replace("\\","")
            obj = json.loads(sdata)
            for i,j in obj.items():
                print("{} : {}".format(i,j))
            
            response = make_response(kstyle.present(obj), 200)
            response.mimetype = "image/svg+xml"
            return response
        return "kaggle profile does not exist"
    return "No user!"


@app.route("/selection",methods=["GET"])
def selection():
    response = HtmlResponse(url = 'http://kaggle.com') 
    f = Selector(response = response).xpath('//span/text()').extract()
    return f



if __name__ == "__main__":
    
    app.run(debug=True)
