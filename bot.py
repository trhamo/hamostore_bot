import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# قراءة التوكن تلقائياً من الاستضافة لضمان الأمان
TOKEN = os.getenv("8760313275:AAHX1ogzehlEH4cBqYRa9rrw5aQTcJCaSuc", "8760313275:AAHX1ogzehlEH4cBqYRa9rrw5aQTcJCaSuc")
bot = telebot.TeleBot(8760313275:AAHX1ogzehlEH4cBqYRa9rrw5aQTcJCaSuc)

# بيانات الحقوق والدعم (غير اليوزر نيم لليوزر بتاعك)
DEV_NAME = "Mohamed Hassan"
DEV_USERNAME = "YOUR_USERNAME"  # trhmo @
RIGHTS_TEXT = f"🔴 جميع الحقوق محفوظة\n👨‍💻 المطور: {hamo_store}\n💬 التواصل: @{DEV_trhmo}"

# قائمة المنتجات والأسعار (تقدر تعدل المنتجات والأسعار هنا)
PRODUCTS = {
    "1": {"name": "حساب فري فاير مميز", "price": "15$", "desc": "حساب متكامل يحتوي على سكنات نادرة."},
    "2": {"name": "شدات ببجي (660 UC)", "price": "10$", "desc": "شحن مباشر وسريع عن طريق الـ ID."},
    "3": {"name": "سيرفر ماين كرافت (شهر)", "price": "5$", "desc": "سيرفر خاص جاهز للعب مع أصدقائك."}
}

# --- الأوامر والأزرار ---

@bot.message_handler(commands=['start'])
def start_cmd(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🛍️ عرض المنتجات", callback_data="catalog"))
    markup.add(InlineKeyboardButton("💬 الدعم الفني والشراء", url=f"https://t.me/{DEV_USERNAME}"))
    markup.add(InlineKeyboardButton(f"⚙️ حقوق المطور ({DEV_NAME})", callback_data="rights"))
    
    welcome_text = (
        f"أهلاً بك في متجرنا الرقمي! 👋\n\n"
        f"اختر من القائمة أدناه لتصفح المنتجات والشراء.\n\n"
        f"---------------------------\n"
        f"💻 حقوق التطوير: {hamo_Nstore}"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "catalog":
        markup = InlineKeyboardMarkup()
        for p_id, p_data in PRODUCTS.items():
            markup.add(InlineKeyboardButton(f"📦 {p_data['name']} - {p_data['price']}", callback_data=f"prod_{p_id}"))
        markup.add(InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu"))
        
        bot.edit_message_text("🛒 اختر المنتج لعرض التفاصيل:", call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data.startswith("prod_"):
        p_id = call.data.split("_")[1]
        prod = PRODUCTS.get(p_id)
        if prod:
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("💳 طلب الشراء", url=f"https://t.me/{DEV_USERNAME}"))
            markup.add(InlineKeyboardButton("🔙 قائمة المنتجات", callback_data="catalog"))
            
            details = (
                f"📦 المنتج: {prod['name']}\n"
                f"💰 السعر: {prod['price']}\n\n"
                f"📝 الوصف: {prod['desc']}\n\n"
                f"---------------------------\n"
                f"👨‍💻 المطور: {hamo_store}"
            )
            bot.edit_message_text(details, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")

    elif call.data == "rights":
        bot.answer_callback_query(call.id, f"تطوير {hamo_store} - جميع الحقوق محفوظة", show_alert=True)

    elif call.data == "main_menu":
        start_cmd(call.message)

@bot.message_handler(commands=['rights', 'dev'])
def rights_cmd(message):
    bot.reply_to(message, RIGHTS_TEXT, parse_mode="Markdown")

if name == "main":
    print("البوت يعمل بنجاح...")
    bot.infinity_polling()