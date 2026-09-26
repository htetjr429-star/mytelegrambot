import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.request import HTTPXRequest

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"မင်္ဂလာပါ {user_name} ရှင့် 🌸\n\n"
        f"ကျွန်မကတော့ ထက် ရဲ့ Personal Assistant Bot လေးပါ၊ ဘာများ ကူညီပေးရမလဲရှင့်။\n"
        f"ပြောချင်တာတွေ၊ စာတွေကို ဒီအတိုင်း ပို့ထားခဲ့လို့ ရပါတယ်နော်။ လိုင်းတက်တာနဲ့ ပြန်ပြောပေးပါမယ်။"
    )
    await update.message.reply_text(welcome_text)

# စာမေးတာတွေပေါ် မူတည်ပြီး အဖြေအမျိုးမျိုး ပြန်ပေးမယ့် Function
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if "နေကောင်းလား" in user_text:
        reply_text = "နေကောင်းပါတယ်ရှင့် 🌸"
    elif "နာမည်ဘယ်လိုခေါ်လဲ" in user_text:
        reply_text = "ကျွန်မကတော့ ထက် ရဲ့ Assistant Bot လေးပါနော် 💖"
    else:
        # မေးခွန်းတွေထဲ မပါရင် အလိုအလျောက် ပြန်ပေးမယ့် စာ
        reply_text = f"ကျေးဇူးပါနော်! သင့်ဆီက မက်ဆေ့ဂျ် '{user_text}' ကို လက်ခံရရှိပါတယ်။ ထက် လိုင်းတက်လာရင် ပြန်ပြောပေးပါမယ်။"

    await update.message.reply_text(reply_text)

if __name__ == '__main__':
    TOKEN = "8624661477:AAGG1kmcFQvfZ_BGBDhuszupFtMfv94tRAQ"

    request = HTTPXRequest(connect_timeout=60.0, read_timeout=60.0)
    app = ApplicationBuilder().token(TOKEN).request(request).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot စတင် လည်ပတ်နေပါပြီ...")
    app.run_polling()
