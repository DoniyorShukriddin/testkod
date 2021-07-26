import telebot
from telebot import types
import time

#biznig kanalimiz @PHP_PYTHON_COD Dasturchi @DoniyorSoft manbaga tegingan 3 ta xarif


bot = telebot.TeleBot("1727308709:AAG8h3UAiq933AGEAePEKkZt2AZsPzGi31E") #botingiz tokeni yozasiz 

@bot.message_handler(func=lambda message: True)
def main(message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	
	text = str(message.text)
	if text == '/start':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		markup.row('🕋Allohning go‘zal ismlari🤲')
		markup.row('📚Arab Alifbosi📖', '💥Kanalimiz⭐️')
		markup.row('👨‍💻 Dasturchi🧑‍💻')
		bot.send_photo(chat_id, "https://t.me/Loading_Online/13", "<b>Assalomu Alaykum Va Rahmatullahi Barakotuh.Sizni Botimizda Ko‘rishimizdan Hursandmiz.😊Marhamat Kerakli  Bo‘limni Tanlang.</b>", parse_mode="HTML", reply_markup=markup)

		
		
		
	
		
	if text == '🕋Allohning go‘zal ismlari🤲':
		Svam = types.ReplyKeyboardMarkup(resize_keyboard=True)
		Svam.row('🎵 Audio 🎧', '🎞️ Video 🎬')
		Svam.row('🚫ᴏʀᴛɢᴀ🚫')
		bot.send_photo(chat_id, "https://t.me/Loading_Online/9", "<b>Siz Allohning Go‘zal Ismlari bo‘limidasiz.O‘zingizga kerakli bo‘limni tanlang...!</b>", parse_mode="HTML", reply_markup=Svam)
	if text == '👨‍💻 Dasturchi🧑‍💻':
		bot.send_message(chat_id, "Admin @DoniyorSoft biznig kanalimiz @PHP_PYTHON_COD")	
	if text == '💥Kanalimiz⭐️':
		bot.send_message(chat_id, "Biznig kanalimiz @PHP_PYTHON_COD")
	 
			
	if text == '🚫ᴏʀᴛɢᴀ🚫':
		up = types.ReplyKeyboardMarkup(resize_keyboard=True)
		up.row('🕋Allohning go‘zal ismlari🤲')
		up.row('📚Arab Alifbosi📖', '💥Kanalimiz⭐️')
		up.row('👨‍💻 Dasturchi🧑‍💻')
	
		bot.send_message(chat_id, "<b>Bosh meynuga muvafaqiyatli qaytdingiz✔.😊Marhamat kerakli  bo‘limni tanlang.</b>", parse_mode="HTML", reply_markup=up)
		
		#@DoniyorSoft 
		
	if text == '📚Arab Alifbosi📖':
		up = types.ReplyKeyboardMarkup(resize_keyboard=True)
		up.row('1-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('2-D͜͡A͜͡R͜͡S͜͡ ✍️', '3-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('4-D͜͡A͜͡R͜͡S͜͡ ✍️', '5-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('6-D͜͡A͜͡R͜͡S͜͡ ✍️', '7-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('8-D͜͡A͜͡R͜͡S͜͡ ✍️', '9-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('10-D͜͡A͜͡R͜͡S͜͡ ✍️', '11-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('12-D͜͡A͜͡R͜͡S͜͡ ✍️', '13-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('14-D͜͡A͜͡R͜͡S͜͡ ✍️', '15-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('16-D͜͡A͜͡R͜͡S͜͡ ✍️', '17-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('18-D͜͡A͜͡R͜͡S͜͡ ✍️', '19-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('20-D͜͡A͜͡R͜͡S͜͡ ✍️', '21-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('22-D͜͡A͜͡R͜͡S͜͡ ✍️', '23-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('24-D͜͡A͜͡R͜͡S͜͡ ✍️', '35-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('26-D͜͡A͜͡R͜͡S͜͡ ✍️', '27-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('28-D͜͡A͜͡R͜͡S͜͡ ✍️', '29-D͜͡A͜͡R͜͡S͜͡ ✍️')
		up.row('🚫ᴏʀᴛɢᴀ🚫')
		bot.send_photo(chat_id, "https://t.me/Loading_Online/11", "<b>《Arab Alifbosi》 Arab Tilini O'rganish!</b>", parse_mode="HTML", reply_markup=up)
		
	
		
		
	if text == '1-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_photo(chat_id, "https://t.me/Namoz_Organish_Kanali/263:", "1-дарс.  أ    ب    ت  Араб алифбосининг исмлари #Шайх_Алижон_қори @UnversalUzRoBot")
		
		
	if text == '1-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_document(chat_id, "https://t.me/Namoz_Organish_Kanali/264:", "")

	if text == '2-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_photo(chat_id, "https://t.me/Namoz_Organish_Kanali/265:", "2-дарс.  أ    ب    ت Ҳарфлар махражи #Шайх_Алижон_қори @UnversalUzRoBot")
		
		
	if text == '2-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_document(chat_id, "https://t.me/Namoz_Organish_Kanali/266:")
		
		
	if text == '3-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_photo(chat_id, "https://t.me/Namoz_Organish_Kanali/267:", "3-дарс.   اَ    اِ     اُ Ҳарфлар махражи Шайх_Алижон_қори        @UnversalUzRoBot")
		
		
	if text == '3-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_document(chat_id, "https://t.me/Namoz_Organish_Kanali/268:")
		
	
	if text == '4-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/269", caption="4-дарс. زَ     زِ     زُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
		
		
	
	if text == '5-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/270", caption="5-дарс. مَ     مِ     مُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
		
	if text == '6-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/271", caption="6-дарс.تَ     تِ     تُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '7-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/272", caption="7-дарс.نَ     نِ     نُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '8-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/273", caption="8-дарс.يَ      يِ      يُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '9-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/274", caption="9-дарс.بَ    بِ    بُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '10-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/275", caption="10-дарс كَ      كِ      كُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")	
	if text == '11-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/276", caption="11-дарс لَ      لِ      لُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	
	if text == '12-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/277", caption="12-дарс وَ      وِ      وُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")	
	if text == '13-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/278", caption="13-дарс هَ       هِ       هُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")	
	if text == '14-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/280", caption="14-дарс فَ   فِ     فُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '15-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/279", caption="15-дарс قَ    قِ      قُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '16-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/281", caption="16-дарс شَ    شِ     شُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '17-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/282", caption="17-дарс سَ     سِ     سُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '18-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/283", caption="18-дарс ثَ     ثِ     ثُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '19-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/284", caption="19-дарс صَ    صِ    صُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '20-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/285", caption="20-дарс طَ     طِ     طُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '21-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/286", caption="21-дарс جَ      جِ      جُҲарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '22-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/287", caption="22-дарс خَ      خِ      خُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '23-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/288", caption="23-дарс حَ      حِ      حُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '24-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/289", caption="24-дарс غَ      غِ      غُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '25-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/290", caption="25-дарс عَ      عِ      عُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '26-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/291", caption="26-дарс دَ       دِ      دُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '27-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/292", caption="27-дарс ضَ     ضِ    ضُ Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '28-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/293", caption="28-дарс ذَ      ذِ      ذُ  Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '29-D͜͡A͜͡R͜͡S͜͡ ✍️':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/294", caption="29-дарс ظَ      ظِ      ظُ  Ҳарфлар махражи Шайх_Алижон_қори🌙 @UnversalUzRoBot ✅")
	if text == '🎵 Audio 🎧':
		bot.send_audio(chat_id, "https://t.me/Namoz_Organish_Kanali/230")
	if text == '🎞️ Video 🎬':
		bot.send_video(chat_id, "https://t.me/Namoz_Organish_Kanali/231", caption="🕋 Allohning 99 go‘zal ismlari.🕌@UnversalUzRoBot")
   
bot.polling(none_stop=True)

#biznig kanalimiz @PHP_PYTHON_COD manbaga tegingan 3 ta xarif