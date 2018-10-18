#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import ImageRecognition


SERVER_ADDRES = '127.0.0.1'
SERVER_PORT = 8081

class ImageRecognitionHTTPServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = open(ImageRecognition.project_path + 'form.html').read()
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        # Upload the temp file and get the path
        uploaded_file = ImageRecognition.upload(form['file'])

        # Run ImageAI lib
        result = ImageRecognition.recognize(uploaded_file)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(result, "utf8"))



def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = (SERVER_ADDRES, SERVER_PORT)
    httpd = HTTPServer(server_address, ImageRecognitionHTTPServer)
    print('running server on http://' + SERVER_ADDRES + ':' + str(SERVER_PORT) + '...')
    httpd.serve_forever()





run()