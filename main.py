import telebot
#Telebot is a bot framework for Telegram Bot API.
import pyqrcode
#module used to convert url to qrcode
import time
#maintains execution time
import png
#helps in png

token = " YOUR BOT TOKEN "
bot=telebot.TeleBot(token ,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome Sir/Madam To @urltoqrbot!")
 
@bot.message_handler(commands=['abuse'])
def send_welcome(message):
	bot.reply_to(message, "vela vetti illama vandhutan paaru")
 
@bot.message_handler(commands=['abuse_hard'])
def send_welcome(message):
	bot.reply_to(message, "nee lam uyirodavae iruka koodathu sethudu poi")
 
@bot.message_handler(commands=['donate'])
def send_donate(message):
	bot.reply_to(message, "BOT IS FREE TO USE , WE WILL ACCEPT DONATIONS IN OUR FUTURE PROJECTS")
 
@bot.message_handler(commands=['creator'])
def send_creator(message):
	bot.reply_to(message, "created by @im_raveen")
 
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, "Any Doubts? pm @im_raveen")
 
@bot.message_handler(commands=['repo'])
def send_repo(message):
	bot.reply_to(message, "Repo : https://github.com/raveen-2003/url-to-qrcode-bot")

@bot.message_handler(commands=['get_qrcode'])
def qr_code_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_message(message.chat.id, "Send Any Valid url")
    bot.register_next_step_handler(sent, qr_code)

@bot.message_handler(commands=['qr_code'])
def qr_code(message):
    url=pyqrcode.create(message.text)
    url.png('qrcode.png',scale=10)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open('qrcode.png','rb' ))
    
time.sleep(2)
bot.polling()
