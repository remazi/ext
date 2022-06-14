import telebot,os,requests
from telebot import TeleBot,types
import time
token = '5566091482:AAHv7SSjBWohEQubkUEilOgjmeVyuIm9R5A'
bot = TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text="Welcome please send only IG posts link 🗿❤️\nby : @G_D_I")
    time.sleep(2)
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text="  ⩫ post link? : ")
@bot.message_handler(content_types = ['text'])
def basha(m):
	ba = m.text	
	target = ba.split('?')[0]
	post = f'{target}?__a=1'
	head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
	x = requests.get(post,headers=head).json()
	post_id =x['graphql']['shortcode_media']['id']
	bot.send_message(m.chat.id,text=post_id)
bot.polling()
