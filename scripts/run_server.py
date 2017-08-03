import threading
import webbrowser

from http.server import HTTPServer, SimpleHTTPRequestHandler


def run_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def run_browser(browser=''):
    browser = webbrowser.get(browser if browser else None)
    browser.open('http://localhost:8000/', new=2)


def run_site():
    threading.Thread(target=run_server).start()
    threading.Thread(target=run_browser).start()


if __name__ == '__main__':
    run_site()
