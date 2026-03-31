from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv
import os
from random_number import get_random_number
from db_conn import DB_conn

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
        
        lucky_number = random_number()

        content = content.replace("{{NUMBER}}", str(lucky_number))

        db = DB_conn()

        last_numbers = db.get_last_10()
        numbers_html = "".join(f"<li>{num}</li>" for num in last_numbers)

        content = content.replace("{{LAST_NUMBERS}}", numbers_html)
       
        db.insert_lucky_number(number=lucky_number)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(content.encode())

    # def do_GET(self):
    #     self.send_response(200)
    #     self.send_header("Content-type", "text/html")
    #     self.end_headers()

    #     with open(HTML_FILE, "r") as f:
    #         content = f.read()
    #     self.wfile.write(content.encode())




if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Request_Handler)
    print(f"Server is running on {HOST}:{PORT}")
    server.serve_forever()