import telebot, time, threading, random
from telebot import types

admin_id = '6309252183'
token = "7511845554:AAGa7IrfV0DQQQMM99NNcs7Z16SyzDSFxBM"
bot = telebot.TeleBot(token, parse_mode="HTML")

stop_processes = {}

video_urls = [
    "https://t.me/O_An6/106",
    "https://t.me/O_An6/110",
    # Add the remaining video URLs here...
]

def process(message):
    video_url = random.choice(video_urls)
    process_id = hash(message)
    stop_processes[process_id] = False
    dd = 0
    live = 0
    risko = 0
    send = bot.send_video(message.chat.id, video_url, caption="𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐂𝐚𝐫𝐝𝐬...⌛", parse_mode='Markdown', reply_to_message_id=message.message_id)

    # You can replace this with the logic you want to process during the /yo command
    lino = ["dummy_card_1", "dummy_card_2"]  # Placeholder for cards
    total = len(lino)

    for card in lino:
        start_time = time.time()
        # Replace info(card) and chk(card) with your own logic
        brand, type, level, bank, country_name, country_flag = "Visa", "Credit", "Gold", "Dummy Bank", "Dummy Country", "🌍"
        try:
            result = "Dummy result"  # Replace this with actual result
        except Exception as e:
            bot.send_message(admin_id, f"An error occurred: {e}")
            result = "ERROR"
        elapsed_time = round(time.time() - start_time, 2)
        print(result)
                
        if 'success' in result.lower():
            live += 1
            bot.reply_to(message, f'𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n𝐂𝐚𝐫𝐝: <code>{card}</code>\n𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Auth 🔥\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: {result}\n\n𝗜𝗻𝗳𝗼: {brand} - {type} - {level}\n𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country_name} {country_flag}\n\n𝐓𝐢𝐦𝐞: {elapsed_time} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬\n𝐁𝐲: <a href="tg://openmessage?user_id=6309252183">JOO</a>', parse_mode='HTML')
        elif 'risk' in result.lower():
            risko += 1
        else:
            dd += 1

        buttons = types.InlineKeyboardMarkup(row_width=1)
        buttons.add(
            types.InlineKeyboardButton(f"{card}", callback_data='1', align_center=True),
            types.InlineKeyboardButton(f"{result}", callback_data='2'),
            types.InlineKeyboardButton(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅ : {live}", callback_data='3'),
            types.InlineKeyboardButton(f"𝐑𝐢𝐬𝐤 ❌️ : {risko}", callback_data='4'),
            types.InlineKeyboardButton(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌ : {dd}", callback_data='5'),
            types.InlineKeyboardButton(f"𝐓𝐨𝐭𝐚𝐥 🍬 : {total}", callback_data='6'),
            types.InlineKeyboardButton("𝐒𝐭𝐨𝐩", callback_data=f'stop_process_{process_id}')
        )
            
        bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=send.message_id, reply_markup=buttons)

        for _ in range(21):
            if stop_processes.get(process_id):
                bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐒𝐭𝐨𝐩𝐩𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
                return
            time.sleep(1)

    bot.edit_message_caption(chat_id=message.chat.id, message_id=send.message_id, caption="𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")

@bot.callback_query_handler(func=lambda call: call.data.startswith('stop_process'))
def stop_process_callback(call):
    process_id = call.data.split('_')[-1]
    stop_processes[int(process_id)] = True
    bot.answer_callback_query(call.id, "Process will be stopped.")
    
@bot.message_handler(commands=['yo'])
def yo_command(message):
    threading.Thread(target=process, args=[message]).start()

@bot.message_handler(commands=['start'])
def start_command(message):
    video_url = random.choice(video_urls)
    bot.send_video(message.chat.id, video_url, caption="𝐉𝐮𝐬𝐭 𝐬𝐞𝐧𝐝 𝐲𝐨𝐮𝐫 𝐜𝐨𝐦𝐛𝐨", parse_mode='Markdown', reply_to_message_id=message.message_id)

bot.infinity_polling()
