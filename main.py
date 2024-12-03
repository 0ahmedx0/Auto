from bot import Bot
from flask import Flask
import threading

# إنشاء تطبيق Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# تشغيل Flask في خيط منفصل
def run_flask():
    app.run(host='0.0.0.0', port=8080)

# إنشاء وتشغيل البوت
bot = Bot()

def run_bot():
    bot.run()

if __name__ == "__main__":
    # تشغيل Flask في خيط منفصل
    threading.Thread(target=run_flask).start()
    
    # تشغيل البوت
    run_bot()
