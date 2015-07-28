# Simple HTTP Server

This is an ultra simple HTTPS server as a wrapper for the SimpleHTTPServer module Python ships with.

## Usage

Clone the repo

    $ git clone git@github.com:crgwbr/https-server.git
    $ cd https-server

In order for the server to work, you'll need to generate an SSL certificate. This won't be trusted by anything since it's self-signed, but it's good enough for development.

    $ openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem

Alias it (you should probably add something like this to your `~/.bashrc` file)

    $ alias serve-https="python `pwd`/server.py"

Run the server

    $ cd ~/some/directory
    $ serve-https
