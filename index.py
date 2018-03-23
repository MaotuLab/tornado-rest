import tornado.ioloop
import pyrestful.rest

from pyrestful import mediatypes
from pyrestful.rest import get


class App(pyrestful.rest.RestHandler):

    @get(_path="/{name}", _produces=mediatypes.APPLICATION_JSON)
    def say_name(self, name):
        print("name")
        # todo log中间件
        return {"Hello": name}

    @get(_path="/", _produces=mediatypes.APPLICATION_JSON)
    def index(self):
        print("index")
        return {"message": 'index'}


if __name__ == '__main__':
    try:
        print("Start the echo service")
        app = pyrestful.rest.RestService([App])
        app.listen(8080)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\nStop the echo service")
