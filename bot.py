import os
from telegram import Bot
from telegram.error import InvalidToken

# Token va chat ID ni olish
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print(f"BOT_TOKEN: {TOKEN}")
print(f"CHAT_ID: {CHAT_ID}")

if not TOKEN:
    print("❌ BOT_TOKEN topilmadi. Replit Secret'da uni qo‘shganingizga ishonch hosil qiling.")
    exit()

if not CHAT_ID:
    print("❌ CHAT_ID topilmadi. Replit Secret'da uni ham yozing.")
    exit()

try:
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text="✅ Shohanshohning boti muvaffaqiyatli ishladi!")
    print("✅ Telegramga xabar yuborildi.")
except InvalidToken:
    print("❌ Noto‘g‘ri BOT_TOKEN! Iltimos, uni BotFather’dan to‘g‘ri nusxalang.")
except Exception as e:
    print(f"❌ Noma’lum xatolik: {e}")
