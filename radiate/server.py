import tornado.ioloop
import tornado.web
from tornado import websocket
import tornadio

CHANNELS={}

def normalize_channel(channel):
    # kill double slashes
    return channel.replace('//', '/')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Radiate Server 0.1-alpha")

class SocketIOConnection(tornadio.SocketConnection):
    def on_open(self, *args, **kwargs):
        channel = normalize_channel(kwargs.get('extra'))
        self._channel = channel
        CHANNELS.setdefault(channel, [])
        CHANNELS[channel].append(self)
        print "WebSocket opened on channel %s" % channel

    def on_close(self):
        CHANNELS[self._channel].remove(self)
        print "WebSocket closed on channel %s" % self._channel


class Announcer(tornado.web.RequestHandler):
    def get(self, channel):
        channel = normalize_channel(channel)
        data = self.get_argument('data', '')
        CHANNELS.setdefault(channel, [])
        for socket in CHANNELS[channel]:
            socket.send(data)
        self.write('Posted to %s subscribers' % len(CHANNELS[channel]))

class Stats(tornado.web.RequestHandler):
    def get(self, channel):
        channel = normalize_channel(channel)
        self.write('''
<html>
    <head>
    </head>
    <body>
        <b>Channel:</b> %(channel)s <br/>
        <b>Subscribers:</b> %(count)s <br/>
    </body>
</html>
        ''' % dict(channel=channel, count=len(CHANNELS.get(channel, [])))
        )

SocketIORoute = tornadio.get_router(
    SocketIOConnection, 
    resource='',
    extra_re=r'.+'
).route()
