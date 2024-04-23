from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path.startswith('/welcome'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            query_components = parse_qs(urlparse(self.path).query)
            name = query_components['name'][0] if 'name' in query_components else 'Guest'
            with open('welcome.html', 'r') as f:
                content = f.read()
                content = content.replace('<span id="name"></span>', name)
                self.wfile.write(content.encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/submit 'or self.path == '/submits':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            name = parse_qs(post_data)['name'][0]
            self.send_response(302)
            self.send_header('Location', '/welcome?name=' + name)
            self.end_headers()
        if self.path == '/submits':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            name = parse_qs(post_data)['name'][0]
            self.send_response(302)
            self.send_header('Location', '/welcome?name=' + name)
            self.end_headers()
        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Server running at localhost:' + str(port))
    httpd.serve_forever()

if __name__ == '__main__':
    run()
