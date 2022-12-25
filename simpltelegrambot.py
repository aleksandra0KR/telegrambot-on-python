import telebot
from telebot import types

bot = telebot.TeleBot('your key')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)

    but1 = types.KeyboardButton('Профильная Математика')
    but2 = types.KeyboardButton('Русский')
    but3 = types.KeyboardButton('Информатика')
    but4 = types.KeyboardButton('Итоговое Сочинение')
    markup.add(but1, but2, but3, but4)
    send_mess = f"<b> Привет, {message.from_user.first_name}{message.from_user.last_name}</b>!\nЯ - Фалуфа, ваш ассистент в мире ЕГЭ.\nХочу показать вам полезные ресурсы для подготовки к экзамену. \nРекомендации основаны на собственном опыте, опыте выпускников и учащихся 10-11 классов,а также на информации из статей  \nС помощью этих ресурсов у вас все обязательно получится!\nКакой предмет вас интересует?"
    bot.send_message(message.chat.id,send_mess,parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def messa(messagee):


    get_message_bot = messagee.text.lower()

    if get_message_bot =='информатика' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        but1 = types.KeyboardButton('БесплатныеИнф')
        but2 = types.KeyboardButton('ПлатныеИнф')
        but3 = types.KeyboardButton('Меню')
        markup.add(but1, but2,but3)
        final_messagee = "Отличия платных и бесплтных источников: \n➡Объем информации в ПЛАТНЫХ ресурсах больше, есть задания для закрепления пройденного, а также присутствуют удобные конспекты. \n➡В БЕСПЛАТНЫХ редко есть домашка, но информация преподносится не хуже чем в платных"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='платныеинф' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("сайт Умскул", url="https://umschool.net/profile/"))
        markup.add(types.InlineKeyboardButton("сайт Фоксфорд", url="https://foxford.ru/courses/3841/lessons/83821/"))
        final_messagee = "В <a href='https://umschool.net/profile/'>Умскул</a> вам будут предоставлены:\n  - лекции с разборами заданий, где вы сможете задать вопросы\n  - конспекты\n  - пробники раз в месяц\n  - группа в ВК\n  - домашние задания с проверкой\nВ <a href='https://foxford.ru/courses/3841/lessons/83821/'>Фоксфорде</a> вас также ждут:\n - лекции\n - пробники\n - домашние задания\n - группа в ВК\n - но конспектов не будет"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='бесплатныеинф' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Информатик БУ", url="https://www.youtube.com/c/%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%91%D0%A3"))
        markup.add(types.InlineKeyboardButton("Code-Enjoy", url="https://www.youtube.com/channel/UCGBaXVk4CKyCOuoj49IxK5w"))
        markup.add(types.InlineKeyboardButton("Информатик Родя", url="https://www.youtube.com/c/RodKub27"))
        markup.add(types.InlineKeyboardButton("Сайт Константина Полякова", url="https://kpolyakov.spb.ru/school/ege.htm"))
        markup.add(types.InlineKeyboardButton("Программирование на Python", url="https://stepik.org/course/67/syllabus"))
        markup.add(types.InlineKeyboardButton("Информатика ЕГЭ Умскул", url="https://www.youtube.com/channel/UCqZvYprH2ornRwwMYbPoDYA"))
        final_messagee = "Видео каналы с самыми понятными разборами заданий:\n  ➡️ Информатик БУ\n  ➡️ Информатика ЕГЭ Умскул\n  ➡️️ Информатик Родя\n  ➡️ Code-Enjoy\nСайт Константина Полякова. На нем вы найдете разборы заданий, ответы на частозадоваемые вопросы, тренажеры, видеоматералы и еще много всего."
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)


    elif get_message_bot =='меню' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=7)
        but1 = types.KeyboardButton('Профильная Математика')
        but2 = types.KeyboardButton('Русский')
        but3 = types.KeyboardButton('Информатика')
        but4 = types.KeyboardButton('Итоговое Сочинение')
        markup.add(but1, but2, but3, but4)
        final_messagee = 'Готова подсказать и с другими предметами. \nЧто вас еще интересует?'
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)


    elif get_message_bot =='русский' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        but1 = types.KeyboardButton('БесплатныеРус')
        but2 = types.KeyboardButton('ПлатныеРус')
        but3 = types.KeyboardButton('Меню')
        markup.add(but1, but2,but3)
        final_messagee = "Отличия платных и бесплтных источников: \n➡Объем информации в ПЛАТНЫХ ресурсах больше, есть задания для закрепления пройденного, а также присутствуют удобные конспекты. \n➡В БЕСПЛАТНЫХ редко есть домашка, но информация преподносится не хуже чем в платных"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='платныерус' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("сайт Школково", url="https://shkolkovo.online/"))
        markup.add(types.InlineKeyboardButton("сайт Фоксфорда", url="https://foxford.ru/courses/3829/lessons/83385"))

        final_messagee = "В <a href='https://shkolkovo.online/'>Школково</a> вам будут предоставлены:\n  - лекции с разборами заданий, где вы сможете задать вопросы\n  - конспекты\n  - пробные сочинения и тесты раз в неделю\n  - группа в ВК\n  - домашние задания\n  - Кураторы \nВ <a href='https://foxford.ru/courses/3841/lessons/83821/'>Фоксфорде</a> вас также ждут лекции, пробники и домашние задания, но конспектов не будет"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='бесплатныерус' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("курс на stepik", url="https://stepik.org/lesson/82825/step/12?thread=solutions&unit=59484"))
        markup.add(types.InlineKeyboardButton("Соточка по русскому", url="https://www.youtube.com/channel/UCXzJhu8qo7n2h7xG8k12J3g"))
        markup.add(types.InlineKeyboardButton("РУССКИЙ ЯЗЫК ЕГЭ 2022 СОТКА", url="https://www.youtube.com/c/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD%D1%88%D0%BA%D0%BE%D0%BB%D0%B0%D0%A1%D0%9E%D0%A2%D0%9A%D0%90/videos"))
        final_messagee = "На канале <a href='https://www.youtube.com/channel/UCXzJhu8qo7n2h7xG8k12J3g'>Соточка по русскому</a> вас ждут замечательные разборы каждого задания, а также автор этого канала сделал бесплатный <a href='https://stepik.org/lesson/82825/step/12?thread=solutions&unit=59484'>курс на stepik</a>, в котором вы можете не только посмотреть теорию, но и порешать задания\nА также есть канал <a href='https://www.youtube.com/c/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD%D1%88%D0%BA%D0%BE%D0%BB%D0%B0%D0%A1%D0%9E%D0%A2%D0%9A%D0%90/videos'>РУССКИЙ ЯЗЫК ЕГЭ 2022 СОТКА</a>"

        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)


    elif get_message_bot =='профильная математика' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        but1 = types.KeyboardButton('БесплатныеПр')
        but2 = types.KeyboardButton('ПлатныеПр')
        but3 = types.KeyboardButton('Меню')
        markup.add(but1, but2,but3)
        final_messagee = "Отличия платных и бесплтных источников: \n➡Объем информации в ПЛАТНЫХ ресурсах больше, есть задания для закрепления пройденного, а также присутствуют удобные конспекты. \n➡В БЕСПЛАТНЫХ редко есть домашка, но информация преподносится не хуже чем в платных"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='платныепр' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("сайт Школково", url="https://shkolkovo.online/"))
        final_messagee = "<a href='https://shkolkovo.online/'>ШКОЛКОВО</a> - самая лучшая онлайн школа для подготовки к математике. Более понятных и увлекательных обьяснений вы больше ни где не найдете. Там есть:\n  - стримы с теорией и практикой\n  - домашние задания с экспертной проверкой\n   - пробники\n   - чаты с кураторами, которые овечают 24/7"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='бесплатныепр' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Школково", url="https://www.youtube.com/channel/UCxWeAHyOBQWsw8jZhxWz5iw"))
        markup.add(types.InlineKeyboardButton("Трушин", url="https://www.youtube.com/c/trushinbv"))
        markup.add(types.InlineKeyboardButton("100 бальный репетитор", url="https://www.youtube.com/c/100%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%D1%80%D0%B5%D0%BF%D0%B5%D1%82%D0%B8%D1%82%D0%BE%D1%80"))
        markup.add(types.InlineKeyboardButton("Математик МГУ", url="https://www.youtube.com/channel/UCSdmht0kbvfnItRMNcr4qZA"))
        markup.add(types.InlineKeyboardButton("Школа Пифагора ЕГЭ по математике", url="https://www.youtube.com/c/pifagor1"))

        final_messagee = "Каналы с разборами заданий, а также полезной теорией и стримами:\n   - Школково\n   - 100балльный репетитор\n   - Математик МГУ\n   - Трушин\n   - Школа Пифагора"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)


    elif get_message_bot =='итоговое сочинение' :
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        but1 = types.KeyboardButton('БесплатныеИС')
        but2 = types.KeyboardButton('ПлатныеИС')
        but3 = types.KeyboardButton('Меню')
        markup.add(but1,but2,but3)
        final_messagee = "Отличия платных и бесплтных источников: \n➡Объем информации в ПЛАТНЫХ ресурсах больше, есть задания для закрепления пройденного, а также присутствуют удобные конспекты. \n➡В БЕСПЛАТНЫХ редко есть домашка, но информация преподносится не хуже чем в платных"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='платныеис' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Сайт Фоксфорда", url="https://foxford.ru/courses/3963"))
        final_messagee = "<a href='https://foxford.ru/courses/3963'>Фоксфорд</a>, в которой есть курс по итоговому сочинению. Там есть проверка ваших сочинений"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)
    elif get_message_bot =='бесплатныеис' :
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Соточка по русскому", url="https://www.youtube.com/channel/UCXzJhu8qo7n2h7xG8k12J3g"))
        markup.add(types.InlineKeyboardButton("Школково", url="https://2.shkolkovo.online/courses/2/413"))
        markup.add(types.InlineKeyboardButton("Итоговое сочинение группа ВК", url="https://vk.com/ege100ballov"))
        final_messagee = "<a href='https://2.shkolkovo.online/courses/2/413'>Школково</a> сделали курс, в котором каждую неделю разбирают тексты и произведения для аргументации, также у них есть конспекты, по которым потом можно легко все вспомнить.\n<a href='https://vk.com/ege100ballov'>Итоговое сочинение группа ВК</a>. Здесь вы сможете сдать бесплатно свое сочинение на проверку, также там публикуют аргументы и хорошие сочинения\n<a href='https://www.youtube.com/channel/UCXzJhu8qo7n2h7xG8k12J3g'>Соточка по русскому</a> - канал со стримами про ИС, на которых разбираются произведения и пишутся сочинения"
        bot.send_message(messagee.chat.id, final_messagee, parse_mode='html', reply_markup=markup)



bot.polling(none_stop=True)
