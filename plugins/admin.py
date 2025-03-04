import keralabot

import logging

from config import *

@bot.message_handler(commands=['ban'])
def ban(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    members = bot.get_chat_member(chat_id, user_id)
    
    if message.chat.type == "private":
        bot.reply_to(message, "Este comando deve ser usado em grupos")
        return
    if message.reply_to_message == None and members.status == "administrator" or members.status == "creator":
        ban_user = message.text[5:]
        if ban_user == None:
            bot.reply_to(message, "Responda a uma mensagem ou envie-me o ID do usuário")
        else:
            bot.kick_chat_member(message.chat.id, ban_user)
            bot.send_sticker(message.chat.id, "CAADBAADJQEAAu0egAUl-J3zbwtTgBYE")
            bot.reply_to(message, "{} banned {}".format(message.from_user.first_name, members.first_name))
            bot.delete_message(message.chat.id, message.from_user.message_id)      #Added delete some command for misuse of that
    if message.reply_to_message != None and members.status == "administrator" or members.status == "creator":
        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.send_sticker(message.chat.id, "CAADBAADJQEAAu0egAUl-J3zbwtTgBYE")
        bot.reply_to(message, "{} banned {}".format(message.from_user.first_name, message.reply_to_message.from_user.first_name))
        bot.delete_message(message.chat.id, message.message_id)      #Added delete some command for misuse of that
        return

@bot.message_handler(commands=['unban'])
def unban(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    members = bot.get_chat_member(chat_id, user_id)
    if message.chat.type == "private":
        bot.reply_to(message, "Este comando deve ser usado em grupos")
        return
    
    if message.reply_to_message == None and members.status == "administrator" or members.status == "creator":
        unban_user = message.text[7:]
        if unban_user == None:
            bot.reply_to(message, "Responda a uma mensagem ou envie-me o ID do usuário")
        else:
            bot.unban_chat_member(message.chat.id, unban_user)
            bot.reply_to(message, "Agora esse usuário pode entrar neste chat")
            bot.delete_message(message.chat.id, message.message_id)      #Added delete some command for misuse of that
    if message.reply_to_message != None and members.status == "administrator" or members.status == "creator":
        bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.reply_to(message, "Agora esse usuário pode entrar neste chat")
        bot.delete_message(message.chat.id, message.message_id)      #Added delete some command for misuse of that
        return
