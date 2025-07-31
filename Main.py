from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"  # THIS WILL BE REPLACED BY RAILWAY'S ENVIRONMENT VARIABLE

# List of course video links
videos =1/ https://t.me/squad_4xx/6
2/https://t.me/squad_4xx/7
3/https://t.me/squad_4xx/8
4/https://t.me/squad_4xx/9
5/https://t.me/squad_4xx/10
6/https://t.me/squad_4xx/11
7/https://t.me/squad_4xx/13
8/https://t.me/squad_4xx/14
9/https://t.me/squad_4xx/15
10/https://t.me/squad_4xx/16
11/https://t.me/squad_4xx/17
12/https://t.me/squad_4xx/18
13/https://t.me/squad_4xx/19
14/https://t.me/squad_4xx/20
welcome to level 2🚀 are you ready for next level 2📊
15/https://t.me/squad_4xx/21
16/https://t.me/squad_4xx/22
17/https://t.me/squad_4xx/23
18/https://t.me/squad_4xx/24
19/https://t.me/squad_4xx/25
20/ https://t.me/squad_4xx/26
Welcome to level 3 are you ready for next level 3 course 📊

21/https://t.me/squad_4xx/27
22/https://t.me/squad_4xx/28
23/https://t.me/squad_4xx/29
24/https://t.me/squad_4xx/30
25/https://t.me/squad_4xx/31
26/https://t.me/squad_4xx/32
27/https://t.me/squad_4xx/33
28/https://t.me/squad_4xx/34
29/https://t.me/squad_4xx/35
30/https://t.me/squad_4xx/36
31/https://t.me/squad_4xx/37
32/https://t.me/squad_4xx/38
33/https://t.me/squad_4xx/39
34/https://t.me/squad_4xx/40
35/https://t.me/squad_4xx/41
36/https://t.me/squad_4xx/42
37/https://t.me/squad_4xx/43
38/https://t.me/squad_4xx/44
39/https://t.me/squad_4xx/45
40/https://t.me/squad_4xx/46

Welcome to level 4 🥳🥳
41/https://t.me/squad_4xx/48
42/https://t.me/squad_4xx/49
43/https://t.me/squad_4xx/50
44/https://t.me/squad_4xx/52
45/https://t.me/squad_4xx/53
46/https://t.me/squad_4xx/54
47/https://t.me/squad_4xx/55
48/https://t.me/squad_4xx/56
49/https://t.me/squad_4xx/57
50/https://t.me/squad_4xx/58
welcome to final level 5 😍😍🥳🥳

59 /https://t.me/squad_4xx/62
60/https://t.me/squad_4xx/73
61/https://t.me/squad_4xx/83
62/https://t.me/squad_4xx/104
63/https://t.me/squad_4xx/201
64/https://t.me/squad_4xx/244
65/https://t.me/squad_4xx/245
66/https://t.me/squad_4xx/247
67/https://t.me/squad_4xx/248
68/https://t.me/squad_4xx/249
69/https://t.me/squad_4xx/253
70/https://t.me/squad_4xx/274
71/https://t.me/squad_4xx/275
72/https://t.me/squad_4xx/295
73/https://t.me/squad_4xx/342
  
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_part(update, context, 0)

async def send_part(update, context, index):
    if index >= len(videos):
        await update.message.reply_text("🎉 ኮርሱ ተጠናቀቀ!")
        return

    keyboard = [
        [InlineKeyboardButton("⏭ Next", callback_data=str(index + 1))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(videos[index], reply_markup=reply_markup)
    else:
        await update.callback_query.message.edit_text(videos[index], reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    index = int(query.data)
    await send_part(update, context, index)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
