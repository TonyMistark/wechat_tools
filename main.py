import tornado.ioloop
import tornado.web
from app.urls import urls
import os

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "static_url_prefix": "/static/",
}
print("settings: ", settings)


def make_app():
    return tornado.web.Application(urls, **settings)


if __name__ == "__main__":
    port = 8889
    address = "0.0.0.0"
    print("start server %s:%s" % (address, port))
    app = make_app()
    app.listen(port=port, address=address)
    tornado.ioloop.IOLoop.current().start()
