import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
from tornado.options import define,options
define("port",default=9996, help="run on the given port", type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
       greeting = self.get_argument('greeting','hello!')
       self.write(greeting+',Welcome to Tornado Web Framework')
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    #application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()