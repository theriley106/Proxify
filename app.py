#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, request, render_template, request, url_for, redirect, Markup, Response, send_file, send_from_directory, make_response, jsonify
import requests
import csv
import time
from time import gmtime, strftime

app = Flask(__name__)

SECRET = str(open("../SecretCode.txt").read()).strip()

@app.route('/proxies/<code>', methods=['POST'])
def getProxies(code):
	try:
		if str(code) == str(SECRET):
			proxies = []
			with open('ProxyList.csv', 'rb') as f:
			    reader = csv.reader(f)
			    your_list = list(reader)
			for e in your_list:
				proxies.append(e[0])
			your_list = list(set(proxies))
			return jsonify({"proxies": your_list, "time": strftime("%Y-%m-%d %H:%M:%S", gmtime())})
		else:
			return "Invalid Code"
	except Exception as exp:
		print exp
		return "ERROR"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8888)