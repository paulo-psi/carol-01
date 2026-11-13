import os
import threading
import http.server
import socketserver
from playwright.sync_api import sync_playwright

SITE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class CustomHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)
    def log_message(self, *args): pass

with socketserver.TCPServer(("127.0.0.1", 0), CustomHTTPHandler) as httpd:
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # 1. Desktop 1440
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(f"http://127.0.0.1:{port}/index.html", wait_until="networkidle")
        page.screenshot(path=os.path.join(SITE_DIR, "assets", "screenshots", "desktop_1440.png"), full_page=True)
        # 2. Tablet 768
        page = browser.new_page(viewport={"width": 768, "height": 1024})
        page.goto(f"http://127.0.0.1:{port}/index.html", wait_until="networkidle")
        page.screenshot(path=os.path.join(SITE_DIR, "assets", "screenshots", "tablet_768.png"), full_page=True)
        # 3. Mobile 390
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(f"http://127.0.0.1:{port}/index.html", wait_until="networkidle")
        page.screenshot(path=os.path.join(SITE_DIR, "assets", "screenshots", "mobile_390.png"), full_page=True)
        browser.close()
    httpd.shutdown()
print("Screenshots atualizadas com sucesso!")
