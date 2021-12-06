from config import TOKEN
import keyboard as kb
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType, ParseMode
from aiogram.utils.markdown import text, bold, italic
import json

students = {}

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global students
    user_id = message.from_user.id
    if user_id not in students:
        students[user_id] = {
            'user_id': user_id,
            'flag_add_name': True
        }
    await bot.send_message(user_id, 'Приветствую в чат-боте "Провинциального колледжа"! Как Вас зовут?')

@dp.message_handler()
async def name_message(message: types.Message):
    global students
    user_id = message.from_user.id
    student = students[user_id]
    if student['flag_add_name']:
        student['flag_add_name'] = False
        student['name'] = message.text.capitalize()
        await bot.send_message(user_id, 'Рад познакомиться, ' + student['name'] + '! 😊 \nИз какого Вы класса?', reply_markup=kb.klassi)
        print(student)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('intex'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Что бы Вы хотели посмотреть?',  reply_markup=kb.intex)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('ek'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('en'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('gum'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('socgum'))
async def process_way_command(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "🔒 К сожалению, данный класс ещё находится в разработке ☹")

@dp.message_handler(lambda message: message.text == "Вернуться к выбору класса")
async def process_class_command_3(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери, пожалуйста, свой класс:", reply_markup=kb.klassi)

#РАСПИСАНИЕ_ИНТЕХ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iRaspis'))
async def process_week(callback_query: types.CallbackQuery):
    with open('kalendar_21-22.pdf', 'rb') as cz:
        txt = 'P.S. Если не помните какая сейчас неделя, то посмотрите тут!'
        await bot.send_message(callback_query.from_user.id, "Выберите день недели👇", reply_markup=kb.week)
        await bot.send_document(callback_query.from_user.id, cz, caption=txt)


#ДНИНЕДЕЛИ_ИНТЕХ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iMon'))
async def process_iMon(callback_query: types.CallbackQuery):
    mon = open("table/mon.png", 'rb')
    txt = 'Расписание на понедельник:'
    await bot.send_photo(callback_query.from_user.id, mon, caption=txt)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iTue'))
async def process_iTue(callback_query: types.CallbackQuery):
    tue = open("table/tue.png", 'rb')
    txt = 'Расписание на вторник:'
    await bot.send_photo(callback_query.from_user.id, tue, caption=txt)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iWed'))
async def process_iWed(callback_query: types.CallbackQuery):
    tue = open("table/wed.png", 'rb')
    txt = 'Расписание на среду:'
    await bot.send_photo(callback_query.from_user.id, tue, caption=txt)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iThu'))
async def process_iThu(callback_query: types.CallbackQuery):
    tue = open("table/thu.png", 'rb')
    txt = 'Расписание на чеверг:'
    await bot.send_photo(callback_query.from_user.id, tue, caption=txt)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iFri'))
async def process_iFri(callback_query: types.CallbackQuery):
    tue = open("table/fri.png", 'rb')
    txt = 'Расписание на пятницу:'
    await bot.send_photo(callback_query.from_user.id, tue, caption=txt)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iSat'))
async def process_iSat(callback_query: types.CallbackQuery):
    tue = open("table/sat.png", 'rb')
    txt = 'Расписание на субботу:'
    await bot.send_photo(callback_query.from_user.id, tue, caption=txt)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iEvents'))
async def process_iEvents(callback_query: types.CallbackQuery):
    message_text = text(bold('МЕРОПРИЯТИЯ 📌'),
                        '\n\n1. Очный этап олимпиады "Криста"', italic('\nКогда: в январе'))
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iBack'))
async def process_iBack(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Что бы ты хотел(-а) узнать?", reply_markup=kb.intex)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iRaspis'))
async def process_iRaspis(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Выбери день недели", reply_markup=kb.week)

#ПОЛЕЗНЫЕРЕСУРСЫ_ИНТЕХ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iResources'))
async def process_iResources(callback_query: types.CallbackQuery):
    message_text = text(bold('ПОЛЕЗНЫЕ РЕСУРСЫ 💡'),
                        '\n\nИНТЕРНЕТ-РЕСУРСЫ:',
                        '\nwelcome.stepik.org - онлайн-курсы от ведущих вузов и компаний страны',
                        '\nkpolyakov.spb.ru - сайт Полякова по информатике',
                        '\ncodeforces.com - соревнования и олимпиады по информатике',
                        '\nvsenauka.ru - бесплатная научная литература'
                        '\nsilvertests.ru - портал обучения информатике'
                        '\nege.sdamgia.ru - образовательный портал для подготовки к экзаменам'
                        '\nolimpiada.ru - всё об олимпиадах для школьников'
                        '\npostypashki.ru - лучшая подготовка к олимпиадам, ЕГЭ и ДВИ'
                        '\nmathus.ru - материалы по математике: подготовка к олимпиадам и ЕГЭ'
                        '\n\nЧАТ-БОТЫ:'
                        '\n@mybookbot - поиск книг по всему интернету на всех языках'
                        '\n@ias16bot - бот-учитель со множеством различных функций'
                        '\n@Wikipedia_voice_bot - бот с функцией голосового поиска по «Википедии»'
                        '\n@AndyRobot - чат-бот, который поможет выучить английский язык')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.intexBack)

#ЕГЭ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iEGE'))
async def process_iEGE(callback_query: types.CallbackQuery):
    message_text = text(bold('ПОЛЕЗНЫЕ РЕСУРСЫ ДЛЯ ПОДГОТОВКИ К ЕГЭ 💡'),
                        '\n\nege.sdamgia.ru - образовательный портал для подготовки к экзаменам'
                        '\nkpolyakov.spb.ru - сайт Полякова по информатике'
                        '\nfipi.ru - методическая копилка заданий ЕГЭ'
                        '\nmathege.ru - открытый банк математических задач ЕГЭ'
                        '\nneznaika.info - позволяет подготовиться к ЕГЭ и ОГЭ'
                        '\nfoxford.ru - онлайн-школа'
                        '\nshkolkovo.net - образовательный портал для подготовки к ЕГЭ, ОГЭ, и олимпиадам'
                        '\n4ege.ru - всё самое важное о ЕГЭ'
                        '\nmathus.ru - материалы по математике: подготовка к олимпиадам и ЕГЭ'
                        '\nhttps://drive.google.com/drive/folders/1SltV0hiMSA4yZsh-HLiv_7bBjMzGIiyZ - приложения для подготовки к ЕГЭ по русскому языку'
                        '\n\nТакже есть много каналов на YouTube. Например: '
                        '\nпо математике - Борис Трушин, Пифагор, Математик МГУ, Школково и др.'
                        '\nпо информатике - Информатик БУ, Школково и др.'
                        '\nпо физике - ЕГЭ/ОГЭ Физика, Павел ВИКТОР, Школково и др.'
                        '\n\nТакже Вы можете посмотреть демоверсии ЕГЭ 2022:')
    await bot.send_message(callback_query.from_user.id, message_text, reply_markup=kb.egeintex)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoMath'))
async def process_iDemoMath(callback_query: types.CallbackQuery):
    with open('ege/math-demo2022-pro.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoInf'))
async def process_iDemoInf(callback_query: types.CallbackQuery):
    with open('ege/inf-demo2022pdf.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoPh'))
async def process_iDemoPh(callback_query: types.CallbackQuery):
    with open('ege/fiz-demo2022.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iDemoRus'))
async def process_iDemoRus(callback_query: types.CallbackQuery):
    with open('ege/rus-demo2022.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document)

#ОЛИМПИАДЫ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iOlimp'))
async def process_iOlimp(callback_query: types.CallbackQuery):
    message_text = text('Что бы Вы хотели узнать об олимпиадах?')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.olimp)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('pololimp'))
async def process_pololimp(callback_query: types.CallbackQuery):
    message_text =text('❗Участие в олимпиадах даёт право поступления в ВУЗ без вступительных испытаний или школьник получает 100 баллов по профильному предмету олимпиады.',
                        bold('\n\nПОЛЕЗНЫЕ РЕСУРСЫ ДЛЯ ПОДГОТОВКИ К ОЛИМПИАДАМ 💡'),
                        '\nolimpiada.ru - всё об олимпиадах для школьников'
                        '\npostypashki.ru - подготовка к олимпиадам, ЕГЭ и ДВИ'
                        '\nfoxford.ru - онлайн-школа'
                        '\nshkolkovo.net - образовательный портал для подготовки к ЕГЭ, ОГЭ, и олимпиадам'
                        '\nmathus.ru - материалы по математике: подготовка к олимпиадам и ЕГЭ')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.intexBack)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('soonolimp'))
async def process_pololimp(callback_query: types.CallbackQuery):
    with open('olimp.png', 'rb') as ol:
        txt = 'Ближайшие олимпиады'
        await bot.send_document(callback_query.from_user.id, ol, caption=txt)

#ПОСТУПАШКИ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iPostup'))
async def process_iPostup(callback_query: types.CallbackQuery):
    message_text = text(bold('РЕСУРСЫ ДЛЯ ВЫБОРЫ ВУЗА'),
                         '\n\npostupi.online, \nucheba.ru, \nvuzopedia.ru, \ntabiturient.ru',
                         bold('\n\nТОП ТЕХНИЧЕСКИХ ВУЗОВ'), '\nМГУ им. Ломоносова - msu.ru', '\nСПБГУ - spbu.ru'
                                                                            '\nМФТИ - mipt.ru'
                                                                            '\nИТМО - itmo.ru'
                                                                            '\nМАИ - mai.ru'
                                                                            '\nМГТУ им. Баумана -bmstu.ru '
                                                                            '\nНИЯУ МИФИ - mephi.ru'
                                                                            '\nНИТУ МИСиС - misis.ru')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.intexBack)

#НОВОСТИ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('News'))
async def News(callback_query: types.CallbackQuery):
    with open('news.json') as f:
        n = json.load(f)
        await bot.send_message(callback_query.from_user.id, '\n'.join(n["news"]))

#
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('iOtkr'))
async def News(callback_query: types.CallbackQuery):
    with open('otkr.jpeg', 'rb') as otkr:
        txt = 'Расписание "Открытия" на 2021-2022 г.'
        await bot.send_photo(callback_query.from_user.id, otkr, caption=txt)

#О ШКОЛЕ
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('school'))
async def process_school(callback_query: types.CallbackQuery):
    message_text = text(bold('ИНФОРМАЦИЯ О ШКОЛЕ'),
                        '\n\nПолное название: \nГосударственное общеобразовательное учреждение Ярославской области «Средняя школа «Провинциальный колледж» (сокращенно - ГОУ ЯО СШ «Провинциальный колледж»)'
                        '\n\nАдрес: Большая Октябрьская ул., 79, Ярославль'
                        '\n\nКонтакты: \n(4852) 30-33-38 (приемная, директор)'
                        '\n20-12-42 (Центр дополнительного образования детей "Открытие")'
                        '\n48-60-54 (учительская)'
                        '\n21-23-85 (зам.директора по учебной работе)'
                        '\nФакс: (4852) 30-33-38'
                        '\n\nПочта: yarprovcol@yandex.ru'
                        '\n\nСайт: pcollege.edu.yar.ru'
                        '\n\nТакже Вы можете узнать контакты учителей:')
    await bot.send_message(callback_query.from_user.id, message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=kb.kontaktuch_school)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('kontuch'))
async def process_kontuch(callback_query: types.CallbackQuery):
    with open('kontakti_uchiteley.pdf', 'rb') as document:
        await bot.send_document(callback_query.from_user.id, document, parse_mode=ParseMode.MARKDOWN)

#НЕИЗВЕСТНАЯ КОМАНДА
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text('Я не знаю, что это значит 🤨'
                        '\nДля того, чтобы узнать, что я могу, выбери класс 👉 /grade')
    await msg.reply(message_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)