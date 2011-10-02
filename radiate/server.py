import tornado.ioloop
import tornado.web
from tornado import websocket
import tornadio

CHANNELS={}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This Works!")

class SocketIOConnection(tornadio.SocketConnection):
    def on_open(self, *args, **kwargs):
        channel = kwargs.get('extra')
        self._channel = channel
        CHANNELS.setdefault(channel, [])
        CHANNELS[channel].append(self)
        print "WebSocket opened on channel %s" % channel

    def on_close(self):
        CHANNELS[self._channel].remove(self)
        print "WebSocket closed on channel %s" % self._channel


class Announcer(tornado.web.RequestHandler):
    def get(self, channel):
        data = self.get_argument('data', '')
        CHANNELS.setdefault(channel, [])
        for socket in CHANNELS[channel]:
            socket.send(data)
        self.write('Posted to %s subscribers' % len(CHANNELS[channel]))

SocketIORoute = tornadio.get_router(
    SocketIOConnection, 
    resource='',
    extra_re=r'.*'
).route()

def main(port=8888):
    application = tornado.web.Application([
        (r"/", MainHandler),
        SocketIORoute,
        (r"/(.*)/push", Announcer),
    ])
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
