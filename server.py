from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import app


http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(9000)
http_server.bind(80, "0.0.0.0")
http_server.start(1)
IOLoop.instance().start()