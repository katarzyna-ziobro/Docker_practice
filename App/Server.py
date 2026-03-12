from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
import os
from random_number import get_random_number

HTML_FILE = os.path.join(os.path.dirname(__file__), "Website", "index.html")

load_dotenv()
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))


def random_number():
    number = get_random_number(1, 1000)
    return number


class Request_Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        with open(HTML_FILE, "r") as f:
            content = f.read()
        
        content = content.replace("{{NUMBER}}", str(random_number()))
       

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode())


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Request_Handler)
    print(f"Server is running on {HOST}:{PORT}")
    server.serve_forever()
        
