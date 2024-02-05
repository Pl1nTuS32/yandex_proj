import telebot
from Bot_quest_info import *
import random

bot = telebot.TeleBot('6920047978:AAETbuynidglPFNaq5F4xvk6o8VlEl0siMI')

@bot.message_handler(commands=['start'])
def bot_start(message):
    bot.send_message(message.chat.id, text=start_message)

@bot.message_handler(commands=['help'])
def bot_help(message):
    bot.send_message(message.chat.id, text=help_message)

@bot.message_handler(commands=['fait'])
def bot_quest(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text=quest_message)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Дааааа")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Хотите подолжить?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Дааааа")
def bot_mushroom_castle(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='3..2..1')
    photo = open('msg1100036345-200348.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text=mushroom_castle_message)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Ути-пути-катана")
    item2 = telebot.types.KeyboardButton("Армянский коньяк")
    item3 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2, item3)
    bot.send_message(user_id, "Выберите одно из двух оружий:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Нееет, хочу домой")
def bot_mushroom_castle2(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Хехе, вы проиграли не начав играть, начните прохождение заново!')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("/fait")
    item2 = telebot.types.KeyboardButton("/fait")
    markup.add(item1, item2)
    bot.send_message(user_id, "ДА или ДА?", reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == "Ути-пути-катана")
def bot_utikatana(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Ути-пути-катана - это стандартная катана самурая из страны тростника.')
    bot.send_message(user_id, text='О нет, Гриб Ужастного Знамения приближается, сражайся или беги!')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Я готов!!!")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Готов ли ты сражаться?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Я готов!!!")
def bot_mushroom_castle(message):
    user_id = message.from_user.id
    photo = open('msg1100036345-199344.jpg', 'rb')
    bot.send_photo(user_id, photo)
    user_id = message.from_user.id
    boss_health = 100
    user_health = 100
    while boss_health > 0 and user_health > 0:
        boss_damage = random.randint(15, 25)
        user_damage = random.randint(15, 25)
        boss_health -= user_damage
        user_health -= boss_damage
    if boss_health <= 0:
        bot.send_message(user_id, text='Поздравляю вас, дорогая погасшая душа, у вас получилось победить Гриба Ужастного Знамения!!!!')
        bot.send_message(user_id, text='Вы прошли первый уровень, сейчас я вас перемещу на второй уровень, в локацию Вершина Хулиганов')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Конечно")
        item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
        markup.add(item1, item2)
        bot.send_message(user_id, "Продолжим?", reply_markup=markup)
    else:
        bot.send_message(user_id, text='К сожалению у вас не получилось победить Гриба ужастного Знамения и он вас разрубил две половинки, попробуйте сначала!')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("/fait")
        item2 = telebot.types.KeyboardButton("/fait")
        markup.add(item1, item2)
        bot.send_message(user_id, "ДА или ДА?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Армянский коньяк")
def bot_armeyski_dvuruchnik(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Армянский коньяк - это стандартное оружие армян.')
    photo = open('msg1100036345-199344.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text='О нет, Гриб ужастного Знамения приближается, у вас есть 50% шанс, что получится его споить, в противном случае вы умрете.')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Да, он опьянеет за одну рюмку!!!")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Готов ли ты сражаться?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Да, он опьянеет за одну рюмку!!!")
def bot_mushroom_castle(message):
    user_id = message.from_user.id
    a = random.randint(0, 10)
    if a % 2 == 0:
        bot.send_message(user_id, text='Поздравляю вас, дорогая погасшая душа, у вас получилось споить Гриба Ужастного Знамения!!!!')
        bot.send_message(user_id, text='Вы прошли первый уровень, сейчас я вас перемещу на второй уровень, в локацию Вершина Хулиганов')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Конечно")
        item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
        markup.add(item1, item2)
        bot.send_message(user_id, "Продолжим?", reply_markup=markup)
    else:
        bot.send_message(user_id, text='К сожалению у вас не получилось споить Гриба ужастного Знамения и он вас разрубил две половинки.')
        bot.send_message(user_id, text='Вы проиграли, нажмите /fait, чтобы начать игру заново')



@bot.message_handler(func=lambda message: message.text == "Конечно")
def bot_huligan_mountain1(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='3..2..1')
    photo = open('msg1100036345-200347.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text=huligan_mountain_message)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Плака от швабры")
    item2 = telebot.types.KeyboardButton("Палец Сукуны")
    item3 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2, item3)
    bot.send_message(user_id, "Выберите одно из двух оружий:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Плака от швабры")
def bot_huligan_mountain2(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Плака от швабры - это стандартное оружие рыцаря страны Темного чулана.')
    bot.send_message(user_id, text='О нет, Огненый Хулиган Сава тебя заметил и начинет идти в твою сторону, сражайся или беги!')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Я пройду маинкрафт с модами быстрее него!!!")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Готов ли ты сражаться?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Я пройду маинкрафт с модами быстрее него!!!")
def bot_huligan_mountain3(message):
    user_id = message.from_user.id
    photo = open('msg1100036345-199345.jpg', 'rb')
    bot.send_photo(user_id, photo)
    user_id = message.from_user.id
    boss_health = 100
    user_health = 100
    while boss_health > 0 and user_health > 0:
        boss_damage = random.randint(15, 25)
        user_damage = random.randint(15, 25)
        boss_health -= user_damage
        user_health -= boss_damage
    if boss_health <= 0:
        bot.send_message(user_id, text='Поздравляю вас, дорогая погасшая душа, у вас получилось победить Огненого Хулигана Саву!!!!')
        bot.send_message(user_id, text='Вы прошли первый уровень, сейчас я вас перемещу на третий уровень, в локацию Армянское Семейное Древо')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Поехали!")
        item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
        markup.add(item1, item2)
        bot.send_message(user_id, "Продолжим?", reply_markup=markup)
    else:
        bot.send_message(user_id, text='К сожалению у вас не получилось победить Огненого Хулигана Саву, он вас разрубил две половинки, попробуйте сначала!')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("/fait")
        item2 = telebot.types.KeyboardButton("/fait")
        markup.add(item1, item2)
        bot.send_message(user_id, "ДА или ДА?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Палец Сукуны")
def bot_armeyski_dvuruchnik(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Палец Сукуны - это древний артефакт манического мира, хз как он тут оказался')
    photo = open('msg1100036345-199344.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text='О нет, Огненый Великан Сава приближается, у вас есть 50% шанс, что он съест этот палец и умрет, в противном случае он обратится Сукуной и вам конец!')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Да, у меня получится!!!")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Готов ли ты сражаться?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Да, у меня получится!!!")
def bot_mushroom_castle(message):
    user_id = message.from_user.id
    a = random.randint(0, 10)
    if a % 2 == 0:
        bot.send_message(user_id, text='Поздравляю вас, дорогая погасшая душа, у вас получилось накормить Огненого Хулигана Саву, ваша еда была убойной!')
        bot.send_message(user_id, text='Вы прошли второй уровень, сейчас я вас перемещу на второй уровень, в локацию Армянское Семейное Древо')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("Поехали!")
        item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
        markup.add(item1, item2)
        bot.send_message(user_id, "Продолжим?", reply_markup=markup)
    else:
        bot.send_message(user_id, text='К сожалению вам неповезло и в Огненом Великане Саве пробудился Сукуна и разрубил вас своей техникой')
        bot.send_message(user_id, text='Вы проиграли, нажмите /fait, чтобы начать игру заново')

@bot.message_handler(func=lambda message: message.text == "Поехали!")
def bot_huligan_mountain1(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='3..2..1')
    photo = open('msg1100036345-200346.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text=armyanskoe_drevo_message)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Свадебная вуаль")
    item2 = telebot.types.KeyboardButton("Кольцо всевластия")
    item3 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2, item3)
    bot.send_message(user_id, "Выберите одно из двух оружий:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Кольцо всевластия")
def bot_huligan_mountain2(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Кольцо всевластия - это артифакт который наносит психический урон цели!')
    photo = open('msg1100036345-199343.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text='О нет, Аня-Армянский Зверь тебя заметила и начала ползти в твою сторону, сражайся или беги!')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Я заберу себе трон Армении")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Готов ли ты сражаться?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Я заберу себе трон Армении")
def bot_huligan_mountain3(message):
    user_id = message.from_user.id
    photo = open('msg1100036345-199343.jpg', 'rb')
    bot.send_photo(user_id, photo)
    user_id = message.from_user.id
    boss_health = 100
    user_health = 100
    while boss_health > 0 and user_health > 0:
        boss_damage = random.randint(15, 25)
        user_damage = random.randint(15, 25)
        boss_health -= user_damage
        user_health -= boss_damage
    if boss_health <= 0:
        bot.send_message(user_id, text='Поздравляю вас, дорогая погасшая душа, у вас получилось победить Аню-Армянского Зверя!!!!')
        bot.send_message(user_id, text='Вы прошли этот шедевральный квест на плохую концовку, если хотите пройти квест заново нажмите /fait!')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    else:
        bot.send_message(user_id, text='К сожалению у вас не получилось победить Аню-Армянского Зверя и она вас дизентегрировала!')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("/fait")
        item2 = telebot.types.KeyboardButton("/fait")
        markup.add(item1, item2)
        bot.send_message(user_id, "ДА или ДА?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Свадебная вуаль")
def bot_armeyski_dvuruchnik(message):
    user_id = message.from_user.id
    bot.send_message(user_id, text='Свадебная вуаль - это вещь которая помогает удачно выйти замуж')
    photo = open('msg1100036345-199343.jpg', 'rb')
    bot.send_photo(user_id, photo)
    bot.send_message(user_id, text='О нет, Аня-Армянский Зверь тебя заметила и начала ползти в твою сторону, сражайся или беги!')
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Я съем твой йогурт!!!")
    item2 = telebot.types.KeyboardButton("Нееет, хочу домой")
    markup.add(item1, item2)
    bot.send_message(user_id, "Готов ли ты сражаться?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Я съем твой йогурт!!!")
def bot_mushroom_castle(message):
    user_id = message.from_user.id
    a = random.randint(0, 10)
    if a % 2 == 0:
        bot.send_message(user_id, text='Поздравляю вас, дорогая погасшая душа, у вас получилось жениться на Ане-Армянском Звере! Теперь она будет вам готовить шашлык всю вашу жизнь!')
        bot.send_message(user_id, text='Вы прошли этот шедевральный квест, так еще и на хорошую концовку, ели хотите пройти квест заново нажмите  /fait!')
    else:
        bot.send_message(user_id, text='К сожалению вам неповезло и Аня-Армянский Зверь отвергла вас, а после она вас дизентегрировала!')
        bot.send_message(user_id, text='Вы проиграли')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("/fait")
        item2 = telebot.types.KeyboardButton("/fait")
        markup.add(item1, item2)
        bot.send_message(user_id, "Начнете занаво?", reply_markup=markup)

grib = ["Да, он опьянеет за одну рюмку!!!", "Конечно", "Армянский коньяк", "Я готов!!!", "Ути-пути-катана", "Нееет, хочу домой", "Дааааа", "Да, у меня получится!!!",
        "Палец Сукуны", "Я готов!!!", "Плака от швабры", "Поехали!", "Я съем твой йогурт!!!", "Свадебная вуаль", "Я заберу себе трон Армении", "Кольцо всевластия"]

for i in grib:
    @bot.message_handler(func=lambda message: message.text != i)
    def bebe(message):
        user_id = message.from_user.id
        bot.send_message(user_id, text='Не балуйся, будешь баловаться, будешь проиграешь. Начинай занаво!!!!!!!')
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        item1 = telebot.types.KeyboardButton("/fait")
        item2 = telebot.types.KeyboardButton("/fait")
        markup.add(item1, item2)
        bot.send_message(user_id, "ДА или ДА?", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)