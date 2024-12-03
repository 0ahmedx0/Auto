import os
from bot import Bot
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# تحديد المنفذ
os.environ["PORT"] = "8080"  # تحديد المنفذ إلى 8080

# محاكاة خادم HTTP بسيط لإيهام Render بوجود خادم
def run_http_server():
    port = int(os.environ.get("PORT", 8080))  # استخدام المنفذ 8080
    with TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

# بدء البوت في خيط منفصل
def start_bot():
    bot = Bot()
    bot.run()

# تشغيل خادم HTTP في خيط منفصل
http_server_thread = Thread(target=run_http_server)
http_server_thread.daemon = True
http_server_thread.start()

# تشغيل البوت في الخيط الرئيسي
start_bot()
