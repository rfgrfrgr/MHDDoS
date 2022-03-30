import telegram.ext
import os

with open('token.txt', 'r') as f:
 TOKEN = f.read()

def start(update, context):
    update.message.reply_text("hello! swagat hai")
    
def a1(update, context):
        url = context.args[0]
        update.message.reply_text(f"started")
        url=
        os.system('python start.py ovh {url} 1 250 socks5.txt 100 172800')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"A1 is free now")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("a1", a1))

updater.start_polling()
updater.idle()
