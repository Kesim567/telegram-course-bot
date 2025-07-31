from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Sample course content
courses = {
    "Ace Course": ["Ace Part 1", "Ace Part 2", "Ace Part 3"],
    "Hit FX": ["Hit Part 1", "Hit Part 2", "Hit Part 3"]
}

user_progress = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(course, callback_data=course)]
        for course in courses
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select a course:", reply_markup=reply_markup)

async def course_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    course = query.data
    user_id = query.from_user.id
    user_progress[user_id] = {"course": course, "part": 0}
    part = courses[course][0]
    keyboard = [[InlineKeyboardButton("Next", callback_data="next")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=part, reply_markup=reply_markup)

async def next_part(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    progress = user_progress.get(user_id)

    if not progress:
        await query.edit_message_text("Start with /start")
        return

    course = progress["course"]
    part_index = progress["part"] + 1

    if part_index < len(courses[course]):
        user_progress[user_id]["part"] = part_index
        part = courses[course][part_index]
        keyboard = [[InlineKeyboardButton("Next", callback_data="next")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=part, reply_markup=reply_markup)
    else:
        await query.edit_message_text("Course finished 🎉")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(course_handler, pattern="^(Ace Course|Hit FX)$"))
app.add_handler(CallbackQueryHandler(next_part, pattern="^next$"))

app.run_polling()
