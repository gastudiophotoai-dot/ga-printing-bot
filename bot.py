from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

# Main menu buttons
menu = [
    ["📸 Photo Editing", "🪪 ID Photo"],
    ["🎓 Graduation Design", "🖨 Printing"],
    ["📦 Order Status", "📞 Contact Us"],
]

keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to GA Printing & Digital Studio 🇪🇹\nPlease choose a service:",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📸 Photo Editing":
        await update.message.reply_text("Send your photo for editing 📸")
    elif text == "🪪 ID Photo":
        await update.message.reply_text("Send your ID photo request 🪪")
    elif text == "🎓 Graduation Design":
        await update.message.reply_text("Send details for graduation design 🎓")
    elif text == "🖨 Printing":
        await update.message.reply_text("Send your printing file 🖨")
    elif text == "📦 Order Status":
        await update.message.reply_text("Enter your order ID 📦")
    elif text == "📞 Contact Us":
        await update.message.reply_text(
            "GA Printing & Digital Studio\n📍 Konso - Karat\n📞 +251912702062 / +251916357344 / +251970057813"
        )
    else:
        await update.message.reply_text("Please choose from menu.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
