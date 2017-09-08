#!/usr/bin/env python3

"""
A simple web server made using Tornado.
It serves the basic webpage located in this file's folder.

For reading on the structure of a Tornado web application read:
    http://www.tornadoweb.org/en/stable/guide/structure.html

It works sort of like this:
    The Application object is what manages routing the routing table and global config.
    It maps requests such as / to certain handlers
"""

import os                   # Used to get proper paths to static/template folders
import tornado.httpserver   # Default http server
import tornado.ioloop       # Not sure
import tornado.options      # Used for settings
import tornado.web          # Contains Application / RequestHandler classes

# Tell template renderer where html, css, and js are located
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH   = os.path.join(os.path.dirname(__file__), "static")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler)
        ]

        settings = dict(
            template_path = TEMPLATE_PATH,
            static_path = STATIC_PATH
        )
        # **settings is called keyword argument unpacking.
        # f(**settings) -> f(template_path=blah, static_path=bleh)
        tornado.web.Application.__init__(self, handlers, **settings)

# A basic hander for requests to "/".
# This renders index.html. Render looks by default inside the "templates"
# folder, which was specified in the settings in Application.
# Because it is templated for the css and js, they are "rendered" as well
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


# Make an http server that serves our application to the provided port.
def main():
    httpServer = tornado.httpserver.HTTPServer(Application())
    httpServer.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
