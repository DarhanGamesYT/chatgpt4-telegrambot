import requests
import telebot

url = "https://chatgpt-4-bing-ai-chat-api.p.rapidapi.com/chatgpt-4-bing-ai-chat-api/0.1/send-message/"

@bot.message_handler(commands=['chat'])
def handle_chat(message):
    global reqwest
    reqwest = message.text[6:].replace(' ', '%20').replace('?', '%3F')
    chat_id = message.chat.id
    bot.send_chat_action(chat_id, '⌛')
    payload = "bing_u_cookie=%3CREQUIRED%3E&question={reqwest}"
    headers = {
      "content-type": "application/x-www-form-urlencoded",
      "X-RapidAPI-Key": "7b71078c26mshb289dd9d0777c30p1861ddjsn110e7b907b12",
      "X-RapidAPI-Host": "chatgpt-4-bing-ai-chat-api.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    bot.delete_message(chat_id, message_id)
    bot.reply_to(message, response.text)

bot.polling()
