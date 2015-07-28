#!/usr/bin/env python

import BaseHTTPServer, SimpleHTTPServer
import ssl

HOST = ('localhost', 4433)
PRIVATE_KEY = 'key.pem'
CERT_FILE = 'cert.pem'

httpd = BaseHTTPServer.HTTPServer(HOST, SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=PRIVATE_KEY, certfile=CERT_FILE, server_side=True)

print 'Server running at %s:%s' % HOST
httpd.serve_forever()
