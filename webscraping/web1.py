import re
import sys 
import os.path
import tornado.httpserver
import webbrowser
import csv
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
define("port", default=8882	, help="run on the given port", type=int)
class IndexHandler(tornado.web.RequestHandler):
	def get(self): #pass a get request
		self.render('index1.html')
class OutputHandler(tornado.web.RequestHandler):
	def post(self):
		datafile = self.get_argument('cars.csv',None)
		with open('cars.csv') as f:
                    reader=csv.reader(f)
                    for row in reader:
                        self.write(row[0])
		self.render('output.csv')
if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler), (r'/hello', OutputHandler)],
		template_path=os.path.join(os.path.dirname(__file__), "templates"))
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()