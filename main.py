from bot import Bot
import os

# تعيين متغير بيئة لإيهام Render أن الخدمة تحتوي على خادم
os.environ["PORT"] = "8080"  # تعيين المنفذ الذي يتوقعه Render

# تشغيل البوت
bot = Bot()
bot.run()
