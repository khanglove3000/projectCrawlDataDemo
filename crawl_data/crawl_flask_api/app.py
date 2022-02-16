import os, sys

# make sure src folder is added into sys path.
from flask import Flask
from flask import request, jsonify
from flask import Blueprint
from celery import Celery
from src.routes import *
from threading import Thread
import time
from urllib import request
from twisted.internet import reactor

import json

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)

	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	app.register_blueprint(routes)

	@app.before_first_request
	def activate_job():
		def run_job():
			time.sleep(0.5)
			try:
				if not reactor.running:
					reactor.run()

			except:
				pass

		thread = Thread(target=run_job)