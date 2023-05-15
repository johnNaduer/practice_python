from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def main():
    PORT = 8080
    server = HTTPServer(('', PORT), MyHandler)
    print(f"Server running on port {PORT}")
    server.serve_forever()

if __name__ == '__main__':
    main()

