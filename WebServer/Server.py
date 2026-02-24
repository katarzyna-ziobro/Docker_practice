from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
import os

HTML_FILE = os.path.join(os.path.dirname(__file__), "Website", "index.html")

load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))


class Request_Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        with open(HTML_FILE, "rb") as f:
            content = f.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content)



server = HTTPServer((HOST, PORT), Request_Handler)
print(f"server is now running on port: {PORT}")
server.serve_forever()
        
