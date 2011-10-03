import tornado.web
import tornado.ioloop
from radiate.server import SocketIORoute, Announcer, Stats, MainHandler
import argh

def start(port=8888):
    application = tornado.web.Application([
        (r"/", MainHandler),
        SocketIORoute,
        (r"/(.+)/push", Announcer),
        (r"/(.+)/push/", Announcer),
        (r'/(.+)/', Stats),
        (r'/(.+)', Stats),
    ])
    application.listen(port)
    print "Listening at %s" % port
    tornado.ioloop.IOLoop.instance().start()
    print "Terminated"


@argh.command
def fg():
    start()

def main():
    parser = argh.ArghParser()
    parser.add_commands([fg])
    parser.dispatch()    
