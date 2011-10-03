Deploying
===========

Radiate comes with a buildout configuration which allow you to deploy this
quickly::

  git clone https://kagesenshi@github.com/kagesenshi/radiate.git radiate
  cd radiate
  python bootstrap.py
  ./bin/buildout

The command above will pull the dependencies needed by radiate and install it
in a contained environment.

To start the server, execute::

  ./bin/radiate-admin fg 


Subscribing to channel
=======================

A channel can be any path in the URL. Eg: http://localhost:8888/this/is/a/channel
You can subscribe to a channel using the socketIO library::

    <!DOCTYPE html>
    <html>
    <head>
        <script 
            src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js">
        </script>
        <script type="text/javascript"
            src="http://cdn.socket.io/stable/socket.io.js"></script>
        <script>
            WEB_SOCKET_SWF_LOCATION = 'http://cdn.socket.io/stable/WebSocketMain.swf'

            $(document).ready(function () {
                ws = new io.Socket('localhost', {
                      port: '8888',
                      resource: 'this/is/a/channel',
                      transports:['websocket', 'flashsocket','xhr-multipart',
                                  'xhr-polling']
                })
                
                ws.on('message', function(message) {
                    // Do something after receiving a message from server
                });
            
                ws.connect();
            });
            
        </script>
    </head>
    <body>
    </body>
    </html>

Sending to a channel
=====================

You can use POST or GET to send data to the channel. Currently radiate is 
using 'data' request variable, in the future I'll be making its possible to
post JSON instead.

To send data to a channel using GET, you can just load this:

    http://localhost:8888/this/is/a/channel/push?data=putyourdatahere


