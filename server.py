from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def guess_type(self, path):
        if path.endswith('.js'):
            return 'application/javascript'
        return super().guess_type(path)

server_address = ('', 8000)
httpd = HTTPServer(server_address, CustomHandler)
httpd.serve_forever()
