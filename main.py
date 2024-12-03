from bot import Bot
import os

# جعل التطبيق يعمل دون تشغيل خادم فعلًا
if __name__ == "__main__":
    # تعيين متغير بيئة لإيهام Render أن الخدمة تحتوي على خادم
    os.environ["PORT"] = "8080"  # تعيين المنفذ الذي يتوقعه Render

    # تشغيل البوت
    bot = Bot()
    bot.run()
