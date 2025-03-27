# Replit
# Taobao Telegram Bot (Replit versiyasi)

Bu loyiha Taobao sahifasini avtomatik ochadigan va Telegram orqali sizga xabar yuboradigan Python botdir.  
Bot `playwright` va `python-telegram-bot` asosida yozilgan, va **Replit** platformasida ishlashga moslashtirilgan.

---

## Funksiyasi

- Taobao sahifasini ochadi
- Screenshot oladi (`screenshot.png`)
- Telegram bot orqali sizga xabar yuboradi

---

## O‘rnatish (Replit uchun)

1. Replit’da yangi Python loyihasi yarating
2. Quyidagi fayllarni yuklang:
   - `bot.py`
   - `requirements.txt`
   - `build.sh`
   - `.replit`
   - `.env` (yoki Secrets bo‘limida kiritiladi)

---

## Replit Secrets sozlovi

Secrets (yashirin o‘zgaruvchilar) bo‘limiga quyidagilarni qo‘shing:

| Nomi       | Qiymat                              |
|------------|--------------------------------------|
| `BOT_TOKEN`| `123456789:AAABBBCCCDDDEEE...`       |
| `CHAT_ID`  | `123456789` (foydalanuvchi yoki guruh ID)

---

## Ishga tushirish

1. Terminalda quyidagilarni yozing:
