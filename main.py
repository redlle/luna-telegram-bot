# pip install pyTelegramBotAPI

import telebot
import config
import random  # randomfromlist

from telebot import types  # for keyboard
bot = telebot.TeleBot(config.TOKEN)  # def bot token
print("Start")


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Luna v1/static/welcome.webp', 'rb')  # open sticker
    bot.send_sticker(message.chat.id, sti)  # send sticker

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔮 Magic Ball")
    item2 = types.KeyboardButton("🤑Flip a coin")
    item3 = types.KeyboardButton("😄Tell a joke")

    # add items in keyboard
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Hi {0.first_name}!\nI'm <b>{1.first_name}</b>! I will be your experimental <em>patronus</em>.".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)  # send message


@bot.message_handler(content_types=['text'])
def mes(message):
    if message.chat.type == 'private':  # maybe about group
        if message.text in ('🔮 Magic Ball', 'ball', 'Ball', "Magic Ball", "magic ball", "Magic ball"):
            answer = ["It is certain!", "It is decidedly so!", "Without doubt!", "Yes - definitely!",
                      "You may rely on it!", "As I see it, yes", "Most likely", "Outlook good", "Yes!", "Signs point to yes",
                      "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                      "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
            bot.send_message(message.chat.id, str(
                random.choice(answer)))  # magicball
        # flip a coin
        elif message.text in ("🤑Flip a coin", "Flip", "flip", "coin", "Coin", "flip a coin", "Flip a coin"):
            flip = random.choice(["Heads", "Tails",
                                  "Toss A Coin To Your Witcher!! Oh, sorry, the song..."])  # random
            bot.send_message(message.chat.id, str(flip))
            if flip == "Toss A Coin To Your Witcher!! Oh, sorry, the song...":
                sti = open('Luna v1/static/coin.webp', 'rb')  # open sticker
                bot.send_sticker(message.chat.id, sti)  # send sticker

        elif message.text in ("How are you?", "Howdy", "😋Howdy?", "How're you?", "howdy"):  # newbutton
            # creating inline keyboard for howdy asking
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(
                "Famously", callback_data="good")
            item2 = types.InlineKeyboardButton(
                "Like a sad muggle", callback_data='bad')
            # answering
            markup.add(item1, item2)
            howareyou = ["Perfectly well! How about you?", "Great, thank you. How are you?",
                         "Good, thanks, and you?", "I need some more coffee. How are you?"]
            bot.send_message(message.chat.id, str(random.choice(howareyou)))

        elif message.text in ("Hi", "hi", "Hi!", "hi!", "Hello", "hello", "hello!", "Hello!", "salut", "salut"):  # greetings
            hello = random.choice(
                ["Heya!😇", "Just going to say hi!", "Hey there!☺️", "Long time no see😜", "Hey!"])
            bot.send_message(message.chat.id, str(hello))
            if hello == "Hey!":
                sti = open('Luna v1/static/hello.webp', 'rb')  # open sticker
                bot.send_sticker(message.chat.id, sti)
        elif message.text in ("😄Tell a joke", "joke", "Joke", 'Jokes', "jokes"):
            from jokes import Jokes
            bot.send_message(message.chat.id, str(
                random.choice(Jokes)))
            if random.randrange(1, 6) == 1:
                sti = open('Luna v1/static/witcher.webp', 'rb')
                bot.send_sticker(message.chat.id, sti)
        elif int(message.text) in range(10001):
            bot.send_message(message.chat.id, str(
                random.randrange(1, int(message.text) + 1)))

        # unknown
        else:
            bot.send_message(message.chat.id, "I don't know such a spell!!😔")

# saved callback


@ bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "good":
                bot.send_message(call.message.chat.id, "That's great!! 😊")
                sti = open('Luna v1/static/albus.webp', 'rb')  # open sticker
                bot.send_sticker(call.message.chat.id, sti)  # send sticker
            elif call.data == "bad":
                bot.send_message(
                    call.message.chat.id, "Who offend you? Tell who and I'll turn him into a frog 🐸")

            # to make question to dissapiar and also markup
            """bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id, text="How are you?", reply_markup=None)"""
            # vanishing spell
            """bot.answer_callback_query(
                callback_query_id=call.id, show_alert=False, text="Vanishing Spell✨")"""

            # hz
    except Exception as e:
        print(repr(e))


# run(none_stop)
bot.polling(none_stop=True)
