from bot import Bot
import os
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# محاكاة خادم HTTP بسيط لإيهام Render بوجود خادم
def run_http_server():
    port = int(os.environ.get("PORT", 8080))  # استخدام المنفذ 8080
    with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

# بدء البوت
bot = Bot()
bot.run()

# بدء خادم HTTP في الخلفية (لن يؤثر على عمل البوت)
run_http_server()
