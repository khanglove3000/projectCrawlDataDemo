from . import routes

import os, sys, json
from src.services.crawlService import CrawlService

from flask import Flask
from flask import request, jsonify

# Bắt đầu reactor để khởi động spider
@routes.route('/crawl/start',methods=['POST'])
def start():
	service = CrawlService()
	service.start_reactor()
	return 'Started Successful', 200

# dừng reactor service để dừng spider
@routes.route('/crawl/stop', methods=['POST'])
def stop():
	service = CrawlService()
	service.stop_reactor()
	return 'Stop Successful', 200

## bắt đầu crawl website với các thành phần spider
@routes.route('/crawl/<siteuuid>', methods=['POST'], default={'crawluuid':''})
@routes.route('/crawl/<siteuuid>/<crawluuid>', methods=['POST'])
def crawl(siteuuid, crawluuid):
	if request.is_json:
		service = CrawlService()
		website = request.get_json()
		website['UUID'] = siteuuid
		service.crawl(website, crawluuid) # sẽ không trả về bất kỳ kết quả nào vì nó được thực thi bởi CrawlerRunner
		return 'Excuting crawling', 200

	return 'Bad request', 500


## bắt đầu crawl website với crawl process
@routes.route('/crawlp/<siteuuid>', methods=['POST'], default={'crawluuid':''})
@routes.route('/crawlp/<siteuuid>/<crawluuid>', methods=['POST'])
def crawl_by_process(siteuuid, crawluuid):
	if request.is_json:
		service = CrawlService()
		website = request.get_json()
		website['UUID'] = siteuuid
		result = service.crawl_by_process(website, crawluuid) # sẽ không trả về bất kỳ kết quả nào vì nó được thực thi bởi CrawlerRunner
		return jsonify(result), 200

	return 'Bad request', 500






