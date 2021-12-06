from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


#ВЫБОР_КЛАССА
intex = InlineKeyboardButton('11И', callback_data='intex')
ek = InlineKeyboardButton('11Э', callback_data='ek')
en = InlineKeyboardButton('11ЕН', callback_data='en')
gum = InlineKeyboardButton('11Г', callback_data='gum')
socgum = InlineKeyboardButton('11СГ', callback_data='socgum')

#ВОЗМОЖНОСТИ_ИНТЕХ
iRaspis= InlineKeyboardButton('Расписание ⏰', callback_data='iRaspis')
News = InlineKeyboardButton('Новости 📰', callback_data='News')
iResources = InlineKeyboardButton('Полезные ресурсы', callback_data='iResources')
iEGE = InlineKeyboardButton('ЕГЭ ✏', callback_data='iEGE')

olimppol = InlineKeyboardButton('Полезные материалы', callback_data='pololimp')
olimpsoon = InlineKeyboardButton('Ближайшие олимпиады', callback_data='soonolimp')
olimp = InlineKeyboardMarkup(row_width=1).add(olimppol, olimpsoon)
iOlimp = InlineKeyboardButton('Олимпиады 🥇', callback_data='iOlimp')

iPostup = InlineKeyboardButton('Поступашки 🐦', callback_data='iPostup')
iOtkr = InlineKeyboardButton('Открытие ', callback_data='iOtkr')

#РАСПИСАНИЕ_ИНТЕХ
iMon = InlineKeyboardButton('Понедельник', callback_data='iMon')
iTue = InlineKeyboardButton('Вторник', callback_data='iTue')
iWed = InlineKeyboardButton('Среда', callback_data='iWed')
iThu = InlineKeyboardButton('Четверг', callback_data='iThu')
iFri = InlineKeyboardButton('Пятница', callback_data='iFri')
iSat = InlineKeyboardButton('Суббота', callback_data='iSat')
iEvents = InlineKeyboardButton('Мероприятия', callback_data='iEvents')
iBack = InlineKeyboardButton('🔙', callback_data='iBack')

#EGE_ИНТЕХ
iDemoMath = InlineKeyboardButton("МАТЕМАТИКА'22", callback_data='iDemoMath')
iDemoInf = InlineKeyboardButton("ИНФОРМАТИКА'22", callback_data='iDemoInf')
iDemoPh = InlineKeyboardButton("ФИЗИКА'22", callback_data='iDemoPh')
iDemoRus = InlineKeyboardButton("РУССКИЙ ЯЗЫК'22", callback_data='iDemoRus')
iBackEGE = InlineKeyboardButton('🔙', callback_data='iBackEGE')

school = InlineKeyboardButton('О школе 🏫', callback_data='school')
kontaktuch = InlineKeyboardButton('Контакты учителей 👩‍🏫', callback_data='kontuch')
webschool = InlineKeyboardButton('Перейти на сайт школы 🏫', callback_data='webschool', url = "pcollege.edu.yar.ru")
parol = InlineKeyboardButton('Введите пароль:')

klassi = InlineKeyboardMarkup(row_width=1).add(intex, ek, en, gum, socgum)
intex = InlineKeyboardMarkup(row_width=2).add(iRaspis, News, iResources, iOtkr, iEGE, iOlimp, iPostup, school)
week= InlineKeyboardMarkup(row_width=1).add(iMon, iTue, iWed, iThu, iFri, iSat, iEvents, iBack)
intexBack = InlineKeyboardMarkup(row_width=1).add(iBack)
egeintex = InlineKeyboardMarkup(row_width=2).add(iDemoMath, iDemoInf, iDemoPh, iDemoRus, iBack)
egeintexback = InlineKeyboardMarkup(row_width=1).add(iBackEGE)
kontaktuch_school = InlineKeyboardMarkup(row_width=1).add(kontaktuch, webschool)