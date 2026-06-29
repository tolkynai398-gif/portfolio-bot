from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8941340340:AAF0YC5vsrreUT5qrJdnzgkUaYr7qK2N97Q"

keyboard = [
    ["👤 Мен туралы", "🎯 Менің мақсатым"],
    ["🚀 CAP Education", "👨‍🏫 Менторым"],
    ["🛠️ Жобаларым", "🎮 Хобби"],
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Сәлем! Мен Ерназардың портфолио ботымын.",
        reply_markup=reply_markup
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "👤 Мен туралы":
        await update.message.reply_text(
            "Менің атым Ерназар. Мен 13 жастамын, Қарағанды қаласында тұрамын және Дарын СШЛИ-де оқимын."
        )

    elif text == "🎯 Менің мақсатым":
        await update.message.reply_text(
            "Мақсатым — кәсіби бағдарламашы болып, ойындар, сайттар және пайдалы бағдарламалар жасау."
        )

    elif text == "🚀 CAP Education":
        await update.message.reply_text(
            "Мен CAP Education бағдарламасында веб-әзірлеу мен бағдарламалауды үйреніп жүрмін."
        )

    elif text == "👨‍🏫 Менторым":
        await update.message.reply_text(
            "Менторым Әілмансұр маған бағдарламалау мен жобалар жасауға көмектеседі."
        )

    elif text == "🛠️ Жобаларым":
        await update.message.reply_text(
            "Жобаларым:\n• Portfolio сайты\n• Telegram бот\n• Python ойындары"
        )

    elif text == "🎮 Хобби":
        await update.message.reply_text(
            "Хоббиім: бағдарламалау, сурет салу , кітап оқу , сайт жасау және жаңа технологияларды үйрену."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

print("Бот іске қосылды!")
app.run_polling()