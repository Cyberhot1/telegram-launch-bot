import logging

from telegram import ParseMode
from telegram.ext import Updater, Filters, CommandHandler
from database import DBHelper

logging.basicConfig(
	format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO
)
logger = logging.getLogger(__name__)
db = DBHelper()

BOT_TOKEN = 'put your bot token here'
ADMIN_APPROVED = ['@isaiahttc']
CHAT_APPROVED = [-1001501246286]

EXISTS_TEXT = '''
<b>You already have data inside databases.</b> <i>If you want 
to add new data, delete the previous data using</i> /delete
'''

ALERT_TEXT = '''
<i>Hei please give me specification of what data you want to save while replying to the message!</i>

<b>Example:</b>
<code>/save today</code> - to save today data
<code>/save tomorrow</code> - to save tomorrow data
<code>/save legit</code> - to save legit project
<code>/save verified</code> - to save verified project
'''

DELETE_ALERT = '''
<i>Hei please give me specification of what data you want to delete!</i>

<b>Example:</b>
<code>/delete today</code> - to delete today data
<code>/delete tomorrow</code> - to delete tomorrow data
<code>/delete legit</code> - to delete legit project
<code>/delete verified</code> - to delete verified project
<code>/delete all</code> - to delete all data
'''

def data_sorting(data):
	results = None
	if data.video:
		if data.caption:
			results = {
				'type': 'video',
				'file_id': data.video.file_id,
				'caption': data.caption_html_urled
			}
		else:
			results = {
				'type': 'video',
				'file_id': data.video.file_id,
				'caption': None
			}
	elif data.text:
		results = {
			'type': 'text',
			'file_id': None,
			'caption': data.text_html_urled
		}
	return results

def save_command(update, context):
	msg = update.message
	query = context.args
	if msg.reply_to_message:
		reply = msg.reply_to_message
		if not query or query[0] not in ['today', 'tomorrow', 'legit', 'verified']:
			context.bot.send_message (
				chat_id = msg.chat_id,
				text = ALERT_TEXT,
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
			return
		elif query[0] == 'today':
			check = db.check_data(100)
			if check:
				msg.reply_text(
					EXISTS_TEXT,
					parse_mode = ParseMode.HTML
				)
			else:
				data = data_sorting(reply)
				if data is not None:
					db.add_data(100, data['type'], data['file_id'], data['caption'])
					msg.reply_text(
						'<b>Success</b>, <i>data is saved inside database</i>',
						parse_mode = ParseMode.HTML
					)
				else:
					msg.reply_text(
						'<b>Failed</b>, <i>media that supported by me just a video and text!</i>',
						parse_mode = ParseMode.HTML
					)
		elif query[0] == 'tomorrow':
			check = db.check_data(200)
			if check:
				msg.reply_text(
					EXISTS_TEXT,
					parse_mode = ParseMode.HTML
				)
			else:
				data = data_sorting(reply)
				if data is not None:
					db.add_data(200, data['type'], data['file_id'], data['caption'])
					msg.reply_text(
						'<b>Success</b>, <i>data is saved inside database</i>',
						parse_mode = ParseMode.HTML
					)
				else:
					msg.reply_text(
						'<b>Failed</b>, <i>media that supported by me just a video and text!</i>',
						parse_mode = ParseMode.HTML
					)
		elif query[0] == 'legit':
			check = db.check_data(300)
			if check:
				msg.reply_text (
					EXISTS_TEXT,
					parse_mode = ParseMode.HTML
				)
			else:
				data = data_sorting(reply)
				if data is not None:
					db.add_data(300, data['type'], data['file_id'], data['caption'])
					msg.reply_text(
						'<b>Success</b>, <i>data is saved inside database</i>',
						parse_mode = ParseMode.HTML
					)
				else:
					msg.reply_text(
						'<b>Failed</b>, <i>media that supported by me just a video and text!</i>',
						parse_mode = ParseMode.HTML
					)
		elif query[0] == 'verified':
			check = db.check_data(400)
			if check:
				msg.reply_text (
					EXISTS_TEXT,
					parse_mode = ParseMode.HTML
				)
			else:
				data = data_sorting(reply)
				if data is not None:
					db.add_data(400, data['type'], data['file_id'], data['caption'])
					msg.reply_text(
						'<b>Success</b>, <i>data is saved inside database</i>',
						parse_mode = ParseMode.HTML
					)
				else:
					msg.reply_text(
						'<b>Failed</b>, <i>media that supported by me just a video and text!</i>',
						parse_mode = ParseMode.HTML
					)
	else:
		context.bot.send_message (
			chat_id = msg.chat.id,
			text = '<i>Reply the</i> <b>message</b> <i>you want to save.</i>',
			parse_mode = ParseMode.HTML,
			reply_to_message_id = msg.message_id
		)

def delete_command(update, context):
	msg = update.message
	query = context.args
	if not query or query[0] not in ['today', 'tomorrow', 'legit', 'verified', 'all']:
		context.bot.send_message (
			chat_id = msg.chat_id,
			text = DELETE_ALERT,
			parse_mode = ParseMode.HTML,
			reply_to_message_id = msg.message_id
		)
	elif query[0] == 'today':
		check = db.check_data(100)
		if check:
			db.del_data(100)
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Success,</b> <i>data is deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Failed,</b> <i>data is already deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
	elif query[0] == 'tomorrow':
		check = db.check_data(200)
		if check:
			db.del_data(200)
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Success,</b> <i>data is deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Failed,</b> <i>data is already deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
	elif query[0] == 'legit':
		check = db.check_data(300)
		if check:
			db.del_data(300)
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Success,</b> <i>data is deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Failed,</b> <i>data is already deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
	elif query[0] == 'verified':
		check = db.check_data(400)
		if check:
			db.del_data(400)
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Success,</b> <i>data is deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Failed,</b> <i>data is already deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
	elif query[0] == 'all':
		check = db.check_all()
		if check:
			db.del_all_data()
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Success,</b> <i>all data is deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat.id,
				text = '<b>Failed,</b> <i>data is already deleted.</i>',
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)

def today_command(update, context):
	msg = update.message
	data = db.get_data(100)
	print(data)
	if not data:
		context.bot.send_message (
			chat_id = msg.chat.id,
			text = '<b>Sorry</b>, <i>currently there is no data available yet</i>',
			parse_mode = ParseMode.HTML,
			reply_to_message_id = msg.message_id
		)
	else:
		if data[0][0] == 'video':
			context.bot.send_video (
				chat_id = msg.chat_id,
				video = data[0][1],
				caption = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat_id,
				text = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)

def tomorrow_command(update, context):
	msg = update.message
	data = db.get_data(200)
	if not data:
		context.bot.send_message (
			chat_id = msg.chat.id,
			text = '<b>Sorry</b>, <i>currently there is no data available yet</i>',
			parse_mode = ParseMode.HTML,
			reply_to_message_id = msg.message_id
		)
	else:
		if data[0][0] == 'video':
			context.bot.send_video (
				chat_id = msg.chat_id,
				video = data[0][1],
				caption = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat_id,
				text = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)

def legit_command(update, context):
	msg = update.message
	data = db.get_data(300)
	if not data:
		context.bot.send_message (
			chat_id = msg.chat.id,
			text = '<b>Sorry</b>, <i>currently there is no data available yet</i>',
			parse_mode = ParseMode.HTML,
			reply_to_message_id = msg.message_id
		)
	else:
		if data[0][0] == 'video':
			context.bot.send_video (
				chat_id = msg.chat_id,
				video = data[0][1],
				caption = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat_id,
				text = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)

def verified_command(update, context):
	msg = update.message
	data = db.get_data(400)
	if not data:
		context.bot.send_message (
			chat_id = msg.chat.id,
			text = '<b>Sorry</b>, <i>currently there is no data available yet</i>',
			parse_mode = ParseMode.HTML,
			reply_to_message_id = msg.message_id
		)
	else:
		if data[0][0] == 'video':
			context.bot.send_video (
				chat_id = msg.chat_id,
				video = data[0][1],
				caption = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)
		else:
			context.bot.send_message (
				chat_id = msg.chat_id,
				text = data[0][2],
				parse_mode = ParseMode.HTML,
				reply_to_message_id = msg.message_id
			)

def main():
	db.setup()
	updater = Updater(BOT_TOKEN, use_context = True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler('save', save_command, filters = Filters.user(username = ADMIN_APPROVED)))
	dp.add_handler(CommandHandler('delete', delete_command, filters = Filters.user(username = ADMIN_APPROVED)))
	dp.add_handler(CommandHandler('today', today_command, filters = Filters.chat(chat_id = CHAT_APPROVED)))
	dp.add_handler(CommandHandler('tomorrow', tomorrow_command, filters = Filters.chat(chat_id = CHAT_APPROVED)))
	dp.add_handler(CommandHandler('legit', legit_command, filters = Filters.chat(chat_id = CHAT_APPROVED)))
	dp.add_handler(CommandHandler('verified', verified_command, filters = Filters.chat(chat_id = CHAT_APPROVED)))

	updater.start_polling(drop_pending_updates = True)
	updater.idle()
if __name__ == '__main__':
	main()
