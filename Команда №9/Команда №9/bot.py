import telebot
import config
import random
import math
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
		markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
		i1 = types.KeyboardButton("Детский сад")
		i2 = types.KeyboardButton("Школа")
		i3 = types.KeyboardButton("Колледж")
		i4 = types.KeyboardButton("ВУЗ")
		markup1.add(i1,i2,i3,i4)
		bot.send_message(message.chat.id, 'Привет!\n\nЯ создан для помощи в выборе учебного учреждения.\n\nДля продолжения диалога, выбери тип учебного учреждения!\n\n<b><i>Данные актуальны на 2022 год</i></b>'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup1)

#Диалог с пользователем
@bot.message_handler(content_types=['text'])
def dialog(message):
	if message.chat.type == 'private':
			
			#Детский сад

		if message.text == 'Детский сад':
			markup2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			inlinemarkupds0 = types.InlineKeyboardMarkup(row_width=1)
			q0 = types.KeyboardButton("Детские сады в северном округе")
			q1 = types.KeyboardButton("Детские сады в восточном округе")
			q2 = types.KeyboardButton("Детские сады в южном округе")
			q3 = types.KeyboardButton("Детские сады в западном округе")
			q4 = types.KeyboardButton("Детские сады в центральном округе")
			q5 = types.InlineKeyboardButton("⬅️Назад", callback_data='main')
			inlinemarkupds0.add(q5)
			markup2.add(q0, q1, q2, q3, q4)
			bot.send_message(message.chat.id, "Выберите округ", reply_markup=markup2)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupds0)

			#Северный округ

		if message.text == 'Детские сады в северном округе':
			markupds1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupds1 = types.InlineKeyboardMarkup(row_width=1)
			w1 = types.KeyboardButton("Остров сокровищ")
			w2 = types.KeyboardButton("№2185")
			w3 = types.KeyboardButton("№473")
			w5 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			markupds1.add(w1, w2, w3)
			inlinemarkupds1.add(w5)
			bot.send_message(message.chat.id, "Список лучших детских садов по северному округу", reply_markup=markupds1)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupds1)
		if message.text == 'Остров сокровищ':
			inlinemarkupos = types.InlineKeyboardMarkup(row_width=3)
			os1 = types.InlineKeyboardButton("Телефон", callback_data='os1')
			os2 = types.InlineKeyboardButton("Адрес", callback_data='os2')
			os3 = types.InlineKeyboardButton("Сайт", callback_data='os3')
			os4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos.add(os1, os2, os3, os4)
			bot.send_message(message.chat.id, "Частный детский сад «Остров сокровищ» - дошкольная образовательная организация, имеющая лицензию на право ведения образовательной деятельности №037481.\n\n1.Частный детский сад «Остров сокровищ» - дошкольная образовательная организация, имеющая лицензию на право ведения образовательной деятельности №037481.\n\n2.Расположен в Парковой зоне Дубки Тимирязевского района Северного административного округа (САО) города Москвы. Здоровье вашего ребенка здесь не будет подвергаться вредным воздействиям, свойственным мегаполисам.\n\n3.Придерживается индивидуального подхода и авторских методик в образовательном и воспитательном процессах. Наш детский сад в Москве использует современные и проверенные методы развития и обучения, которые приносят исключительную пользу детям. Авторские методики воспитания — это то, что отличает нас от других.\n\n4.У нас работают только квалифицированные и опытные педагоги и воспитатели. Они, как профессионалы своего дела, в то же время являются творческими педагогами. Мы работаем под девизом «Развивая, вдохновляем!» — сочетая творческий аспект воспитания и развития с обучением необходимым практическим навыкам, которые пригодятся в жизни.\n\n5.Оснащен по последнему слову техники и укомплектован новым оборудованием, комфортной мебелью и инвентарем. У нас в помощниках обучающие роботы, сенсорные игровые аппараты, интерактивная доска и много других современных гаджетов.", reply_markup=inlinemarkupos)

		if message.text == '№2185':
			inlinemarkup2185 = types.InlineKeyboardMarkup(row_width=3)
			ds1 = types.InlineKeyboardButton("Телефон", callback_data='ds1')
			ds2 = types.InlineKeyboardButton("Адрес", callback_data='ds2')
			ds3 = types.InlineKeyboardButton("Сайт", callback_data='ds3')
			ds4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup2185.add(ds1, ds2, ds3, ds4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №2185", reply_markup=inlinemarkup2185)

		if message.text == '№473':
			inlinemarkup473 = types.InlineKeyboardMarkup(row_width=3)
			cs1 = types.InlineKeyboardButton("Телефон", callback_data='cs1')
			cs2 = types.InlineKeyboardButton("Адрес", callback_data='cs2')
			cs3 = types.InlineKeyboardButton("Сайт", callback_data='cs3')
			cs4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup473.add(cs1, cs2, cs3, cs4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №473", reply_markup=inlinemarkup473)

			#Восточный округ

		if message.text == 'Детские сады в восточном округе':
			markupds2 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupds2 = types.InlineKeyboardMarkup(row_width=1)
			w6 = types.KeyboardButton("№109")
			w7 = types.KeyboardButton("№1898")
			w8 = types.KeyboardButton("№2407")
			w10 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			markupds2.add(w6, w7, w8)
			inlinemarkupds2.add(w10)
			bot.send_message(message.chat.id, "Список лучших детских садов по восточному округу", reply_markup=markupds2)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupds2)

		if message.text == '№109':
			inlinemarkup109 = types.InlineKeyboardMarkup(row_width=3)
			ds109 = types.InlineKeyboardButton("Телефон", callback_data='ds109')
			ds110 = types.InlineKeyboardButton("Адрес", callback_data='ds110')
			ds111 = types.InlineKeyboardButton("Сайт", callback_data='ds111')
			ds112 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup109.add(ds109, ds110, ds111, ds112)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №109", reply_markup=inlinemarkup109)

		if message.text == '№1898':
			inlinemarkup1898 = types.InlineKeyboardMarkup(row_width=3)
			ot1 = types.InlineKeyboardButton("Телефон", callback_data='ot1')
			ot2 = types.InlineKeyboardButton("Адрес", callback_data='ot2')
			ot3 = types.InlineKeyboardButton("Сайт", callback_data='ot3')
			ot4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup1898.add(ot1, ot2, ot3, ot4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №1898", reply_markup=inlinemarkup1898)

		if message.text == '№2407':
			inlinemarkup2407 = types.InlineKeyboardMarkup(row_width=3)
			at1 = types.InlineKeyboardButton("Телефон", callback_data='at1')
			at2 = types.InlineKeyboardButton("Адрес", callback_data='at2')
			at3 = types.InlineKeyboardButton("Сайт", callback_data='at3')
			at4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup2407.add(at1, at2, at3, at4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №2407", reply_markup=inlinemarkup2407)


			#Южный округ

		if message.text == 'Детские сады в южном округе':
			markupds3 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupds3 = types.InlineKeyboardMarkup(row_width=1)
			w11 = types.KeyboardButton("№1767")
			w12 = types.KeyboardButton("№1856 Карусель")
			w13 = types.KeyboardButton("№1574")
			w15 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			markupds3.add(w11, w12, w13)
			inlinemarkupds3.add(w15)
			bot.send_message(message.chat.id, "Список лучших детских садов по южному округу", reply_markup=markupds3)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupds3)

		if message.text == '№1767':
			inlinemarkup1767 = types.InlineKeyboardMarkup(row_width=3)
			rt1 = types.InlineKeyboardButton("Телефон", callback_data='rt1')
			rt2 = types.InlineKeyboardButton("Адрес", callback_data='rt2')
			rt3 = types.InlineKeyboardButton("Сайт", callback_data='rt3')
			rt4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup1767.add(rt1, rt2, rt3, rt4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №1767", reply_markup=inlinemarkup1767)
		if message.text == '№1856 Карусель':
			inlinemarkup1856 = types.InlineKeyboardMarkup(row_width=3)
			kar1 = types.InlineKeyboardButton("Телефон", callback_data='kar1')
			kar2 = types.InlineKeyboardButton("Адрес", callback_data='kar2')
			kar3 = types.InlineKeyboardButton("Сайт", callback_data='kar3')
			kar4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup1856.add(kar1, kar2, kar3, kar4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №1856 Карусель", reply_markup=inlinemarkup1856)
		if message.text == '№1574':
			inlinemarkup1574 = types.InlineKeyboardMarkup(row_width=3)
			k1 = types.InlineKeyboardButton("Телефон", callback_data='k1')
			k2 = types.InlineKeyboardButton("Адрес", callback_data='k2')
			k3 = types.InlineKeyboardButton("Сайт", callback_data='k3')
			k4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkup1574.add(k1, k2, k3, k4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №1574", reply_markup=inlinemarkup1574)
			#Западный округ

		if message.text == 'Детские сады в западном округе':
			markupds4 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupds4 = types.InlineKeyboardMarkup(row_width=1)
			w16 = types.KeyboardButton("№1 Сказка")
			w17 = types.KeyboardButton("№1 УДП РФ")
			w18 = types.KeyboardButton("№2 УДП РФ")
			w20 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			markupds4.add(w16, w17, w18)
			inlinemarkupds4.add(w20)
			bot.send_message(message.chat.id, "Список лучших детских садов по западному округу", reply_markup=markupds4)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupds4)

		if message.text == '№1 Сказка':
			inlinemarkupsk = types.InlineKeyboardMarkup(row_width=3)
			sk1 = types.InlineKeyboardButton("Телефон", callback_data='sk1')
			sk2 = types.InlineKeyboardButton("Адрес", callback_data='sk2')
			sk3 = types.InlineKeyboardButton("Сайт", callback_data='sk3')
			sk4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupsk.add(sk1, sk2, sk3, sk4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №1 Сказка", reply_markup=inlinemarkupsk)

		if message.text == '№1 УДП РФ':
			inlinemarkupyd = types.InlineKeyboardMarkup(row_width=3)
			yd1 = types.InlineKeyboardButton("Телефон", callback_data='yd1')
			yd2 = types.InlineKeyboardButton("Адрес", callback_data='yd2')
			yd3 = types.InlineKeyboardButton("Сайт", callback_data='yd3')
			yd4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupyd.add(yd1, yd2, yd3, yd4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №1 УДП РФ", reply_markup=inlinemarkupyd)
		if message.text == '№2 УДП РФ':
			inlinemarkupyd2 = types.InlineKeyboardMarkup(row_width=3)
			yd21 = types.InlineKeyboardButton("Телефон", callback_data='yd21')
			yd22 = types.InlineKeyboardButton("Адрес", callback_data='yd22')
			yd23 = types.InlineKeyboardButton("Сайт", callback_data='yd23')
			yd24 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupyd.add(yd21, yd22, yd23, yd24)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду №2 УДП РФ", reply_markup=inlinemarkupyd2)

			#Центральный округ
		
		if message.text == 'Детские сады в центральном округе':
			markupds5 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupds5 = types.InlineKeyboardMarkup(row_width=1)
			w21 = types.KeyboardButton("Волшебный замок")
			w22 = types.KeyboardButton("Детский сад №3")
			w23 = types.KeyboardButton("Детский сад №6")
			w25 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			markupds5.add(w21, w22, w23)
			inlinemarkupds5.add(w25)
			bot.send_message(message.chat.id, "Список лучших детских садов по центральному округу", reply_markup=markupds5)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupds5)
		if message.text == 'Волшебный замок':
			inlinemarkupmz = types.InlineKeyboardMarkup(row_width=3)
			mz1 = types.InlineKeyboardButton("Телефон", callback_data='mz1')
			mz2 = types.InlineKeyboardButton("Адрес", callback_data='mz2')
			mz3 = types.InlineKeyboardButton("Сайт", callback_data='mz3')
			mz4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupmz.add(mz1, mz2, mz3, mz4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду Волшебный замок", reply_markup=inlinemarkupmz)	

		if message.text == 'Детский сад №3':
			inlinemarkupdz3 = types.InlineKeyboardMarkup(row_width=3)
			dz1 = types.InlineKeyboardButton("Телефон", callback_data='dz1')
			dz2 = types.InlineKeyboardButton("Адрес", callback_data='dz2')
			dz3 = types.InlineKeyboardButton("Сайт", callback_data='dz3')
			dz4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupdz3.add(dz1, dz2, dz3, dz4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду Детский сад №3", reply_markup=inlinemarkupdz3)
		if message.text == 'Детский сад №6':
			inlinemarkupdz6 = types.InlineKeyboardMarkup(row_width=3)
			du1 = types.InlineKeyboardButton("Телефон", callback_data='du1')
			du2 = types.InlineKeyboardButton("Адрес", callback_data='du2')
			du3 = types.InlineKeyboardButton("Сайт", callback_data='du3')
			du4 = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupdz6.add(du1, du2, du3, du4)
			bot.send_message(message.chat.id, "Здесь будет информация о детском саду Детский сад №6", reply_markup=inlinemarkupdz6)	


		#Школа

		if message.text == 'Школа':
			markupshk0 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			inlinemarkupshk0 = types.InlineKeyboardMarkup(row_width=1)
			e1 = types.KeyboardButton("Школы в северном округе")
			e2 = types.KeyboardButton("Школы в восточном округе")
			e3 = types.KeyboardButton("Школы в южном округе")
			e4 = types.KeyboardButton("Школы в западном округе")
			e5 = types.KeyboardButton("Школы в центральном округе")
			e0 = types.InlineKeyboardButton("⬅️Назад", callback_data='main')
			markupshk0.add(e1, e2, e3, e4, e5)
			inlinemarkupshk0.add(e0)
			bot.send_message(message.chat.id, "Выберите район", reply_markup=markupshk0)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupshk0)
			#Северный округ

		if message.text == 'Школы в северном округе':
			markupshk1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupshk1 = types.InlineKeyboardMarkup(row_width=1)
			e6 = types.KeyboardButton("№1576")
			e7 = types.KeyboardButton("№1252 им. Сервантеса")
			e8 = types.KeyboardButton("№1474")
			e10 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupshk1.add(e6, e7, e8)
			inlinemarkupshk1.add(e10)
			bot.send_message(message.chat.id, "Список лучших школ по северному округу", reply_markup=markupshk1)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupshk1)

			#Восточный округ

		if message.text == 'Школы в восточном округе':
			markupshk2 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupshk2 = types.InlineKeyboardMarkup(row_width=1)
			e11 = types.KeyboardButton("№1502 при МЭИ")
			e12 = types.KeyboardButton("№1547")
			e13 = types.KeyboardButton('№1357 "На Братиславской"')
			e15 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupshk2.add(e11, e12, e13)
			inlinemarkupshk2.add(e15)
			bot.send_message(message.chat.id, "Список лучших школ по восточному округу", reply_markup=markupshk2)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupshk2)

			#Южный округ

		if message.text == 'Школы в южном округе':
			markupshk3 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupshk3 = types.InlineKeyboardMarkup(row_width=1)
			e16 = types.KeyboardButton('№548 "Царицыно"')
			e17 = types.KeyboardButton("№1523")
			e18 = types.KeyboardButton("№1158")
			e20 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupshk3.add(e16, e17, e18)
			inlinemarkupshk3.add(e20)
			bot.send_message(message.chat.id, "Список лучших школ по южному округу", reply_markup=markupshk3)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupshk3)

			#Западный округ

		if message.text == 'Школы в западном округе':
			markupshk4 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupshk4 = types.InlineKeyboardMarkup(row_width=1)
			e21 = types.KeyboardButton("№1514")
			e22 = types.KeyboardButton("№1329")
			e23 = types.KeyboardButton("№2007")
			e25 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupshk4.add(e21, e22, e23)
			inlinemarkupshk4.add(e25)
			bot.send_message(message.chat.id, "Список лучших школ по западному округу", reply_markup=markupshk4)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupshk4)

			#Центральный округ
		
		if message.text == 'Школы в центральном округе':
			markupshk5 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupshk5 = types.InlineKeyboardMarkup(row_width=1)
			e26 = types.KeyboardButton("№1535")
			e27 = types.KeyboardButton("Лицей НИУ ВШЭ")
			e28 = types.KeyboardButton("№179 МИОО")
			e30 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupshk5.add(w21, w22, w23)
			inlinemarkupshk5.add(w25)
			bot.send_message(message.chat.id, "Список лучших школ по центральному округу", reply_markup=markupshk5)	
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupshk5)
			
			#Kolledji
		if message.text == 'Колледж':
			markupshk0 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			e1 = types.KeyboardButton("Дизайн")
			e2 = types.KeyboardButton("IT")
			e4 = types.KeyboardButton("Медицина")
			e5 = types.KeyboardButton("Машиностроение")
			markupshk0.add(e1, e2, e4, e5)
			bot.send_message(message.chat.id, "Выберите специальность", reply_markup=markupshk0)

			#Дизайн

		if message.text == 'Дизайн':
			markupcol1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupcol1 = types.InlineKeyboardMarkup(row_width=1)
			e6 = types.KeyboardButton("МИПК им. И.Федорова")
			e7 = types.KeyboardButton('ММКЦТ "Академия TOP"')
			e8 = types.KeyboardButton("МКИиК")
			e10 = types.InlineKeyboardButton("⬅️Назад", callback_data='col')
			markupcol1.add(e6, e7, e8)
			inlinemarkupcol1.add(e10)
			bot.send_message(message.chat.id, "Список лучших колледжей дизайну", reply_markup=markupcol1)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupcol1)
			
			#IT

		if message.text == 'IT':
			markupcol2 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupcol2 = types.InlineKeyboardMarkup(row_width=1)
			e11 = types.KeyboardButton("МГКЭиИТ")
			e12 = types.KeyboardButton("МКИТ IThub")
			e13 = types.KeyboardButton("Политехнический Колледж №8")
			e15 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupcol2.add(e11, e12, e13)
			inlinemarkupcol2.add(e15)
			bot.send_message(message.chat.id, "Список лучших колледжей IT", reply_markup=markupcol2)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupcol2)

			#Медицина

		if message.text == 'Медицина':
			markupcol3 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupcol3 = types.InlineKeyboardMarkup(row_width=1)
			e16 = types.KeyboardButton("Мед. колледж №1")
			e17 = types.KeyboardButton("Мед. колледж №2")
			e18 = types.KeyboardButton("Мед. колледж №7")
			e20 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupcol3.add(e16, e17, e18)
			inlinemarkupcol3.add(e20)
			bot.send_message(message.chat.id, "Список лучших колледжей медицины", reply_markup=markupcol3)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupcol3)

			#Машиностроение

		if message.text == 'Машиностроение':
			markupcol4 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
			inlinemarkupcol4 = types.InlineKeyboardMarkup(row_width=1)
			e21 = types.KeyboardButton("Московский тех. колледж")
			e22 = types.KeyboardButton("Колледж ЖДиГТ")
			e23 = types.KeyboardButton("Колледж АТ №9")
			e24 = types.KeyboardButton("Машиностроение")
			e25 = types.InlineKeyboardButton("⬅️Назад", callback_data='shk')
			markupcol4.add(e21, e22, e23, e24)
			inlinemarkupcol4.add(e25)
			bot.send_message(message.chat.id, "Список лучших колледжей машиностроения", reply_markup=markupcol4)
			bot.send_message(message.chat.id, 'Если хотите вернуться, нажмите "⬅️Назад"', reply_markup=inlinemarkupcol4)


























	#callback
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.message:
		if call.data == 'ds':
			markup2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			q0 = types.KeyboardButton("Детские сады в северном округе")
			q1 = types.KeyboardButton("Детские сады в восточном округе")
			q2 = types.KeyboardButton("Детские сады в южном округе")
			q3 = types.KeyboardButton("Детские сады в западном округе")
			q4 = types.KeyboardButton("Детские сады в центральном округе")
			markup2.add(q0, q1, q2, q3, q4)
			bot.send_message(call.message.chat.id, "Выберите округ", reply_markup=markup2)
		if call.data == 'shk':
			markup3 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			q0 = types.KeyboardButton("Школы в северном округе")
			q1 = types.KeyboardButton("Школы в восточном округе")
			q2 = types.KeyboardButton("Школы в южном округе")
			q3 = types.KeyboardButton("Школы в западном округе")
			q4 = types.KeyboardButton("Школы в центральном округе")
			markup3.add(q0, q1, q2, q3, q4)
			bot.send_message(call.message.chat.id, "Выберите округ", reply_markup=markup3)
		if call.data == 'col':
			markup4 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			q0 = types.KeyboardButton("Колледжи в северном округе")
			q1 = types.KeyboardButton("Колледжи в восточном округе")
			q2 = types.KeyboardButton("Колледжи в южном округе")
			q3 = types.KeyboardButton("Колледжи в западном округе")
			q4 = types.KeyboardButton("Колледжи в центральном округе")
			markup4.add(q0, q1, q2, q3, q4)
			bot.send_message(call.message.chat.id, "Выберите округ", reply_markup=markup4)
		if call.data == 'v':
			markup5 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			q0 = types.KeyboardButton("ВУЗы в северном округе")
			q1 = types.KeyboardButton("ВУЗы в восточном округе")
			q2 = types.KeyboardButton("ВУЗы в южном округе")
			q3 = types.KeyboardButton("ВУЗы в западном округе")
			q4 = types.KeyboardButton("ВУЗы в центральном округе")
			markup5.add(q0, q1, q2, q3, q4)
			bot.send_message(call.message.chat.id, "Выберите округ", reply_markup=markup5)
		if call.data == 'main':
			markup1 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
			i1 = types.KeyboardButton("Детский сад")
			i2 = types.KeyboardButton("Школа")
			i3 = types.KeyboardButton("Колледж")
			i4 = types.KeyboardButton("ВУЗ")
			markup1.add(i1,i2,i3,i4)
			bot.send_message(call.message.chat.id, 'Привет!\n\nЯ создан для помощи в выборе учебного учреждения.\n\nДля продолжения диалога, выбери тип учебного учреждения!\n\n<b><i>Данные актуальны на 2022 год</i></b>'.format(call.message.from_user, bot.get_me()),
			parse_mode='html', reply_markup=markup1)
		



		if call.data == 'os1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (499) 976-30-85", reply_markup=inlinemarkupos1)
		if call.data == 'os2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: Ивановская ул., 17, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'os3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: ostrov-sad.ru", reply_markup=inlinemarkupos1)
		


		if call.data == 'ds1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (499) 477-13-13", reply_markup=inlinemarkupos1)
		if call.data == 'ds2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: Ясный пр., 7А, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'ds3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: schsv285.mskobr.ru", reply_markup=inlinemarkupos1)
		



		if call.data == 'cs1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (495) 602-41-12", reply_markup=inlinemarkupos1)
		if call.data == 'cs2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: 3-я Новоостанкинская ул., 17, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'cs3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: отсутствует", reply_markup=inlinemarkupos1)
		


		if call.data == 'ot1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (495) 307-38-01", reply_markup=inlinemarkupos1)
		if call.data == 'ot2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: 	Саянская ул., 15Г, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'ot3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: sch922v.mskobr.ru", reply_markup=inlinemarkupos1)
		


		if call.data == 'at1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: 8 (495) 179-20-07", reply_markup=inlinemarkupos1)
		if call.data == 'at2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Москва, ул. Юных Ленинцев, д. 45, корп. 3", reply_markup=inlinemarkupos1)
		if call.data == 'at3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: отсутствует", reply_markup=inlinemarkupos1)
		


		if call.data == 'rt1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (499) 179-57-95", reply_markup=inlinemarkupos1)
		if call.data == 'rt2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: 	Зелёный просп., 99А, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'rt3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: отсутствует", reply_markup=inlinemarkupos1)
		


		if call.data == 'kar1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (495) 712-30-90", reply_markup=inlinemarkupos1)
		if call.data == 'kar2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: 	ул. Грина, 3, корп. 3, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'kar3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: sch2006uz.mskobr.ru", reply_markup=inlinemarkupos1)
		

		if call.data == 'k1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (499) 973-50-93", reply_markup=inlinemarkupos1)
		if call.data == 'k2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: 	ул. Фадеева, 2, стр. 2, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'k3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: lyc1574.mskobr.ru", reply_markup=inlinemarkupos1)




		if call.data == 'sk1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: 8 (495) 435-72-33", reply_markup=inlinemarkupos1)
		if call.data == 'sk2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: Москва, ул. 50 лет Октября, д. 3Б", reply_markup=inlinemarkupos1)
		if call.data == 'sk3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: www.gouskazka.ru", reply_markup=inlinemarkupos1)



		if call.data == 'yd21':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: +7 (499) 131-59-06", reply_markup=inlinemarkupos1)
		if call.data == 'yd22':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: ул. Коштоянца, 8, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'yd23':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: det-sad2.ru", reply_markup=inlinemarkupos1)



		if call.data == 'mz1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон:+7 (926) 530-89-49", reply_markup=inlinemarkupos1)
		if call.data == 'mz2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: пер. Чернышевского, 8, стр. 1, Москва", reply_markup=inlinemarkupos1)
		if call.data == 'mz3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: kidclub.xbridge.ru", reply_markup=inlinemarkupos1)



		if call.data == 'dz1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: 8 (495) 697-70-00", reply_markup=inlinemarkupos1)
		if call.data == 'dz2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: Москва, Богословский переулок, д. 10", reply_markup=inlinemarkupos1)
		if call.data == 'dz3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: отсутствует", reply_markup=inlinemarkupos1)



		if call.data == 'du1':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Телефон: 8 (495) 608-84-15", reply_markup=inlinemarkupos1)
		if call.data == 'du2':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Адрес: Москва, ул. Новорязанская, д. 30/32", reply_markup=inlinemarkupos1)
		if call.data == 'du3':
			inlinemarkupos1 = types.InlineKeyboardMarkup(row_width=2)
			back = types.InlineKeyboardButton("⬅️Назад", callback_data='ds')
			inlinemarkupos1.add(back)
			bot.send_message(call.message.chat.id, "Сайт: отсутствует", reply_markup=inlinemarkupos1)
















































		#run
bot.polling(none_stop=True)