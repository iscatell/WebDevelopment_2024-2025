import http.server
import socketserver

PORT = 9090

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"  
        return super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    httpd.serve_forever()