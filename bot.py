import redis
import os
import telebot
import random
import threading
from telebot import types
import dataa
from emoji import emojize
import math
import time





token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)





def runfight(id):
  if dataa.game.person[id]['die']!=1:
    if dataa.game.person[id]['fight']==1:
          if dataa.game.person[id]['grasseat']==1:
            Keyboard = types.InlineKeyboardMarkup()
            Keyboard.add(types.InlineKeyboardButton(text="Вправо", callback_data='right'))
            Keyboard.add(types.InlineKeyboardButton(text="Влево", callback_data='left'))
            msg = bot.send_message(id, 'Похоже, что вы с каким-то животным не поделили локацию...'+"\n"+
                                 'Выберите, куда бежать. Если хищник выберет такой же вариант, ваши шансы спастись уменьшатся. '+
                                 'Иначе - увеличатся.', reply_markup=Keyboard)
            dataa.game.person[id]['special'] = msg.message_id
  else:
      bot.send_message(id, 'you died')


def fightrun(id):
 if dataa.game.person[id]['die'] != 1:
  if dataa.game.person[id]['fight']==1:
    if dataa.game.person[id]['hunter']==1:
            if dataa.game.person[id]['fightwithhunt']==0:
              Keyboard = types.InlineKeyboardMarkup()
              Keyboard.add(types.InlineKeyboardButton(text="Вправо", callback_data='right'))
              Keyboard.add(types.InlineKeyboardButton(text="Влево", callback_data='left'))
              msg=bot.send_message(id, 'Похоже, что вы нашли добычу!'+"\n"+
                                   'Попытайтесь угадать, куда побежит цель. Если угадаете - ваши шансы поймать ее увеличатся. '+
                                   'Иначе - уменьшатся.',reply_markup=Keyboard)
              dataa.game.person[id]['special'] = msg.message_id
 else:
      bot.send_message(id, 'you died')



def fightfight(id):
 if dataa.game.person[id]['die'] != 1:
  if dataa.game.person[id]['hod'] != dataa.hod:
   if dataa.game.person[id]['fight']==1:
    if dataa.game.person[id]['fightwithhunt']==1:
        Keyboard = types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="Справа", callback_data='right'))
        Keyboard.add(types.InlineKeyboardButton(text="Слева", callback_data='left'))
        msg=bot.send_message(id, 'Встретились хищники... Сейчас будет бой. И пусть победит сильнейший! Выберите, откуда будете атаковать. Если '+
                                   'ваши атаки совпадут, урон останется таким же. Если нет - каждый из вас получит дополнительные 25% урона',reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id
        print('player hod ' + str(dataa.game.person[id]['hod']))
        print('game hod ' + str(dataa.hod))
  else:
      shag(id)
 else:
      bot.send_message(id, 'you died')


def shag(id):
        dataa.game.person[id]['readys']=0
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="Локации", callback_data='loc'))
        Keyboard.add(types.InlineKeyboardButton(text="Способности", callback_data='skill'))
        msg=bot.send_message(id, 'Основное меню',reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id
        print(dataa.game.person[id]['fight'])
        print('player hod '+str(dataa.game.person[id]['hod']))
        print('game hod ' + str(dataa.hod))


def go():
    for id in dataa.game.person:
     if dataa.game.person[id]['die'] != 1:
       if dataa.game.person[id]['fight'] == 0:
        shag(id)
     else:
        bot.send_message(id, 'you died')
     fightfight(id)
     fightrun(id)
     runfight(id)
        
















        #directory='C:\Users\Егор\Desktop\Main_and_not_files\All_for_bot\Map'
        #all_files_in_directory=os.listdir(directory)
        #for file in all_files_in_directory:
        #    img=open(directory+'/'+ file, 'rb')
        #    bot.send_photo(id, img)
        #    img.close()

        




def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode='Markdown'):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)

def reboot(id):
    dataa.game.person[id]['y']=''
    dataa.game.person[id]['stat']=0
    dataa.game.person[id]['grasses']=0
    dataa.game.person[id]['miranimal']=''
    dataa.game.person[id]['losetarget']=0
    dataa.game.person[id]['seelocation']=[]
    dataa.game.person[id]['losetarget']=0
    dataa.game.person[id]['alreadydraka']=0
    dataa.game.person[id]['escapelist']=[]
    dataa.game.person[id]['notrun']=0
    dataa.game.person[id]['fightwithhunt']=0
    dataa.game.person[id]['fight']=0
    dataa.game.person[id]['fightwith']=[]
    dataa.game.person[id]['alreadysee']=0
    dataa.game.person[id]['timeanimal']=''
    dataa.game.person[id]['loc']['1'] = 0
    dataa.game.person[id]['loc']['2'] = 0
    dataa.game.person[id]['loc']['3'] = 0
    dataa.game.person[id]['loc']['4'] = 0
    dataa.game.person[id]['loc']['5'] = 0
    dataa.game.person[id]['loc']['6'] = 0
    dataa.game.person[id]['loc']['7'] = 0
    dataa.game.person[id]['loc']['8'] = 0
    dataa.game.person[id]['loc']['9'] = 0
    dataa.game.person[id]['loc']['10'] = 0
    dataa.game.person[id]['loc']['11'] = 0
    dataa.game.person[id]['loc']['12'] = 0
    dataa.game.person[id]['loc']['13'] = 0
    dataa.game.person[id]['loc']['14'] = 0
    dataa.game.person[id]['loc']['15'] = 0
    dataa.game.person[id]['loc']['16'] = 0
    dataa.game.person[id]['loc']['17'] = 0
    dataa.game.person[id]['loc']['18'] = 0
    dataa.game.person[id]['loc']['19'] = 0
    dataa.game.person[id]['loc']['20'] = 0
    dataa.game.person[id]['loc']['21'] = 0
    dataa.seelocation=[]
    dataa.textt='Видимые локации:'


def rebootloc(id):
    dataa.game.person[id]['loc']['1'] = 0
    dataa.game.person[id]['loc']['2'] = 0
    dataa.game.person[id]['loc']['3'] = 0
    dataa.game.person[id]['loc']['4'] = 0
    dataa.game.person[id]['loc']['5'] = 0
    dataa.game.person[id]['loc']['6'] = 0
    dataa.game.person[id]['loc']['7'] = 0
    dataa.game.person[id]['loc']['8'] = 0
    dataa.game.person[id]['loc']['9'] = 0
    dataa.game.person[id]['loc']['10'] = 0
    dataa.game.person[id]['loc']['11'] = 0
    dataa.game.person[id]['loc']['12'] = 0
    dataa.game.person[id]['loc']['13'] = 0
    dataa.game.person[id]['loc']['14'] = 0
    dataa.game.person[id]['loc']['15'] = 0
    dataa.game.person[id]['loc']['16'] = 0
    dataa.game.person[id]['loc']['17'] = 0
    dataa.game.person[id]['loc']['18'] = 0
    dataa.game.person[id]['loc']['19'] = 0
    dataa.game.person[id]['loc']['20'] = 0
    dataa.game.person[id]['loc']['21'] = 0


@bot.callback_query_handler(func=lambda call:True)
def inline(call):
    if call.data=='loc':
        if dataa.x==1:
            medit(
            'Перемещение.',
            call.from_user.id,
        call.message.message_id
        )
            locs(call.from_user.id)




    elif call.data=='back':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        medit('Назад.', call.from_user.id, dataa.game.person[call.from_user.id]['special'])
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="Локации", callback_data='loc'))
        Keyboard.add(types.InlineKeyboardButton(text="Способности", callback_data='use'))
        msg=bot.send_message(call.from_user.id, 'Основное меню',reply_markup=Keyboard)
        dataa.game.person[call.from_user.id]['special'] = msg.message_id



    elif call.data=='right':
        dataa.game.person[call.from_user.id]['right']=1
        medit(
            'Действие выбрано. Ожидайте конца хода...',
            call.from_user.id,
            call.message.message_id)
        dataa.readys = dataa.readys + 1
        dataa.game.person[call.from_user.id]['readys'] = dataa.game.person[call.from_user.id]['readys'] + 1
        testturn()


    elif call.data=='left':
        dataa.game.person[call.from_user.id]['left'] = 1
        medit(
            'Действие выбрано. Ожидайте конца хода...',
            call.from_user.id,
            call.message.message_id)
        dataa.readys = dataa.readys + 1
        dataa.game.person[id]['readys'] = dataa.game.person[id]['readys'] + 1
        testturn()



    elif call.data=='1':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber']='1'
        move(call.from_user.id, call.message.message_id)


    elif call.data=='2':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber']='2'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '3':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '3'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '4':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '4'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '5':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '5'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '6':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '6'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '7':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '7'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '8':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '8'
        move(call.from_user.id, call.message.message_id)

    elif call.data == '9':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '9'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '10':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '10'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '11':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '11'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '12':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '12'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '13':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '13'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '14':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '14'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '15':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '15'
        move(call.from_user.id, call.message.message_id)


    elif call.data == '16':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '16'
        move(call.from_user.id, call.message.message_id)

    elif call.data == '17':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '17'
        move(call.from_user.id, call.message.message_id)

    elif call.data == '18':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '18'
        move(call.from_user.id, call.message.message_id)

    elif call.data == '19':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '19'
        move(call.from_user.id, call.message.message_id)

    elif call.data == '20':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '20'
        move(call.from_user.id, call.message.message_id)

    elif call.data == '21':
      if dataa.game.person[call.from_user.id]['fight'] == 0:
        dataa.game.person[call.from_user.id]['timenumber'] = '21'
        move(call.from_user.id, call.message.message_id)

    elif call.data=='skill':
        pass





def animaleat():
    return 'Никого'

def animaldie():
    return 'Никто'

def results(id):
    bot.send_message(id, 'За ход произошло:'+"\n"+
                     'Убили: '+str(animaleat())+"\n"+
                     'Умерли: '+str(animaldie())
                     )



def battle(id, x, secondid): #ПРОВЕРКА НА ТО, ЕСТЬ ЛИ БИТВА
    if dataa.game.person[id]['loc'][x]==dataa.game.person[secondid]['loc'][x]:
        if dataa.game.person[id]['loc'][x]==2:
          if dataa.game.person[id]['grasseat']!=1 and dataa.game.person[secondid]['grasseat']!=1:
            if dataa.game.person[id]['hunter']==1 and dataa.game.person[secondid]['hunter']==1:
              dataa.game.person[id]['fightwith']=dataa.game.person[secondid]['selfid']
              dataa.game.person[secondid]['fightwith']=dataa.game.person[id]['selfid']
              dataa.game.person[id]['fightwithhunt']=1
              dataa.game.person[secondid]['fightwithhunt']=1
              dataa.game.person[id]['fight']=1
              dataa.game.person[secondid]['fight']=1
            else:

              dataa.game.person[id]['fight'] = 1
              dataa.game.person[secondid]['fight'] = 1
              dataa.game.person[id]['fightwith'] = dataa.game.person[secondid]['selfid']
              dataa.game.person[secondid]['fightwith'] = dataa.game.person[id]['selfid']


          elif dataa.game.person[id]['grasseat']==1 and dataa.game.person[secondid]['grasseat']!=1:

              dataa.game.person[id]['fightwith'] = dataa.game.person[secondid]['selfid']
              dataa.game.person[secondid]['fightwith'] = dataa.game.person[id]['selfid']
              dataa.game.person[id]['fight']=1
              dataa.game.person[secondid]['fight']=1
          elif dataa.game.person[secondid]['grasseat']==1 and dataa.game.person[id]['grasseat']!=1:

              dataa.game.person[id]['fightwith'] = dataa.game.person[secondid]['selfid']
              dataa.game.person[secondid]['fightwith'] = dataa.game.person[id]['selfid']
              dataa.game.person[id]['fight'] = 1
              dataa.game.person[secondid]['fight'] = 1
          elif dataa.game.person[id]['grasseat']==1 and dataa.game.person[secondid]['grasseat']==1:

              dataa.game.person[id]['grasses']=1
              dataa.game.person[id]['miranimal']+=dataa.game.person[secondid]['animal']+', '
              dataa.game.person[secondid]['grasses'] = 1
              dataa.game.person[secondid]['miranimal'] += dataa.game.person[id]['animal']+', '

          #dataa.game.person[id]['miranimal']=dataa.game.person[id]['miranimal'][:(len(dataa.game.person[id]['miranimal']) - 2)]
          #dataa.game.person[id]['miranimal'] = dataa.game.person[secondid]['miranimal'][:(len(dataa.game.person[secondid])['miranimal'] - 2)]





def die(id):
    dataa.game.person[id]['die']=1
    reboot(id)
    dataa.game.person[id]['hp']=0

def runchoice(id):
    z = random.choice(dataa.game.person[id]['escapelist'])
    if z not in dataa.game.person[id]['notrun']:
        dataa.game.person[id]['loc'][z] = 2
        locchoice()
    else:
        runchoice(id)



def run(id):
    for x in dataa.game.person[id]['loc']:
        if dataa.game.person[id]['loc'][x]==1:
            dataa.game.person[id]['escapelist'].append(x)
            for y in dataa.game.person[id]['loc']:
                if dataa.game.person[id]['loc'][y]==2:
                    dataa.game.person[id][notrun].append(dataa.game.person[id][y])
    runchoice(id)
    runchoice(id)


def escape(id, mainid):
    run(id)
    dataa.game.person[mainid]['losetarget']=1



def draka(id, secondid):#ПРОЦЕСС БИТВЫ
    if dataa.game.person[id]['alreadydraka']!=1:
      if dataa.game.person[id]['hunter']==1:
       if dataa.game.person[secondid]['hunter'] == 1:
        dataa.game.person[id]['fightout'] = 1
        if dataa.game.person[id]['hod'] <= dataa.hod:
          dataa.game.person[id]['hod']=dataa.hod+1
        if dataa.game.person[secondid]['hod'] != dataa.hod:
          dataa.game.person[secondid]['hod'] = dataa.hod + 1
        dataa.game.person[secondid]['fightout'] = 1
        a=random.randint(20, dataa.game.person[id]['dmg'])
        dataa.game.person[secondid]['hp']-=a
        b=random.randint(20, dataa.game.person[secondid]['dmg'])
        dataa.game.person[id]['hp'] -= b
        dataa.game.person[id]['alreadydraka']=1
        dataa.game.person[secondid]['alreadydraka'] = 1
        dataa.game.person[id]['fight']=0
        dataa.game.person[secondid]['fight'] = 0

       else:
           c=((dataa.game.person[id]['speed'])/(2*(dataa.game.person[secondid]['speed'])))
           d=random.randint(1,100)
           if d>c:
               die(secondid)
               dataa.game.person[id]['fight'] = 0
               dataa.game.person[secondid]['fight'] = 0
           else:
               escape(secondid, id)
               dataa.game.person[id]['fight'] = 0
               dataa.game.person[secondid]['fight'] = 0
      elif dataa.game.person[secondid]['hunter']==1:
          c = ((dataa.game.person[secondid]['speed']) / (2 * (dataa.game.person[id]['speed'])))
          d = random.randint(1, 100)
          if d > c:
              die(id)
              dataa.game.person[id]['fight'] = 0
              dataa.game.person[secondid]['fight'] = 0
          else:
              escape(id, secondid)
              dataa.game.person[id]['fight'] = 0
              dataa.game.person[secondid]['fight'] = 0











def endturn():
        for id in dataa.game.person:
            mainid=id
            dataa.game.person[id]['sawanimal']=''
            if dataa.game.person[id]['readys']==0:
                medit('Время вышло!', id, dataa.game.person[id]['special'])
            if dataa.game.person[id]['fight']!=1:
              reboot(id)
              dataa.game.person[id]['loc'][dataa.game.person[id]['timenumber']]=2
              changeloc(id)
            else:
                draka(id, dataa.game.person[id]['fightwith'])
                for id in dataa.game.person:
                    if dataa.game.person[id]['losetarget']==1:
                        bot.send_message(id, 'Цель была проворнее, и сбежала от вас. Чтобы не умереть с голоду, придется быть быстрее...')

            for id in dataa.game.person:


              if id != mainid:
                x = 1
                while x < 22:
                    a = xfd(x)
                    battle(mainid, a, id)
                    x = x + 1




        for id in dataa.chats:
            dataa.hod += 1;
            bot.send_message(id, 'Ход: '+str(dataa.hod))
            results(id)
            dataa.readys = 0
        xod()




def testturn():
    if dataa.readys==len(dataa.players):
        endturn()
        

def move(id, callid):
    medit(
        'Локация выбрана. Ожидайте конца хода...',
        id,
        callid)
    dataa.readys=dataa.readys+1
    dataa.game.person[id]['readys']=dataa.game.person[id]['readys']+1
    testturn()











def skill(id):
    if dataa.game.person[id]['animal']=='Eagle':
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add((types.InlineKeyboardButton(text="Способность животного", callback_data='skill_1')))
        Keyboard.add((types.InlineKeyboardButton(text="Еще одна способность", callback_data='skill_2')))
        msg=bot.send_message(id, 'Способности',reply_markup=Keyboard)




    elif call.data=='use':
        pass



def see(id, y):
         z=xfd(y)

         if dataa.game.person[id]['loc'][z]==1:
             t=seeinloc(id, z)
             dataa.game.person[id]['timeanimal']=''

             return t


def xfd(y):
    if y == 1:
        z = '1'
    elif y == 2:
        z = '2'
    elif y == 3:
        z = '3'
    elif y == 4:
        z = '4'
    elif y == 5:
        z = '5'
    elif y == 6:
        z = '6'
    elif y == 7:
        z = '7'
    elif y == 8:
        z = '8'
    elif y == 9:
        z = '9'
    elif y == 10:
        z = '10'
    elif y == 11:
        z = '11'
    elif y == 12:
        z = '12'
    elif y == 13:
        z = '13'
    elif y == 14:
        z = '14'
    elif y == 15:
        z = '15'
    elif y == 16:
        z = '16'
    elif y == 17:
        z = '17'
    elif y == 18:
        z = '18'
    elif y == 19:
        z = '19'
    elif y == 20:
        z = '20'
    elif y == 21:
        z = '21'
    return z



def seeinloc(mainid, z):

    for id in dataa.game.person:
            if id!=mainid:
              if dataa.game.person[id]['loc'][z]==2:
                c=dataa.game.person[mainid]['vision']-dataa.game.person[id]['hide']
                d=random.randint(0,100)
                if dataa.game.person[mainid]['alreadysee'] == 0:
                  if d>c:
                      dataa.game.person[mainid]['alreadysee'] = 1

                  elif d<=c:

                    if dataa.game.person[mainid]['alreadysee']==0:
                      if dataa.game.person[mainid]['timeanimal']=='Wolf':
                          animal=emojize(':wolf:', use_aliases=True)
                      elif dataa.game.person[mainid]['timeanimal'] == 'Eagle':
                          animal = emojize(':eagle:', use_aliases=True)
                      elif dataa.game.person[mainid]['timeanimal']=='Rabbit':
                          animal=emojize(':rabbit:', use_aliases=True)
                      dataa.game.person[mainid]['timeanimal']+=dataa.game.person[id]['animal']+', '#+animal
                      dataa.game.person[mainid]['sawanimal'] = dataa.game.person[mainid]['timeanimal']
                      dataa.game.person[mainid]['alreadysee'] = 1
                else:
                    dataa.game.person[mainid]['alreadysee'] = 1
                    s=len(dataa.game.person[mainid]['sawanimal'])
                    return dataa.game.person[mainid]['sawanimal'][:(s-2)]

    se=dataa.game.person[mainid]['timeanimal']
    z=len(se)
    se=dataa.game.person[mainid]['timeanimal'][:(z-2)]

    return se





def locs(id):
    if dataa.game.person[id]['loc']['1']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="2", callback_data='2'))
        Keyboard.add(types.InlineKeyboardButton(text="5", callback_data='5'))
        Keyboard.add(types.InlineKeyboardButton(text="8", callback_data='8'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))

        msg=bot.send_message(id, 'В локации 2 вы видите:'+see(id, 2)+"\n"+
          'В локации 5 вы видите:' + see(id, 5)+"\n"+
        'В локации 8 вы видите:' + see(id, 8)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special']=msg.message_id

    elif dataa.game.person[id]['loc']['2']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="1", callback_data='1'))
        Keyboard.add(types.InlineKeyboardButton(text="5", callback_data='5'))
        Keyboard.add(types.InlineKeyboardButton(text="3", callback_data='3'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 1 вы видите:'+see(id, 1)+"\n"+
                             'В локации 5 вы видите:' + see(id, 5)+"\n"+
                             'В локации 3 вы видите:' + see(id, 3)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['3']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="2", callback_data='2'))
        Keyboard.add(types.InlineKeyboardButton(text="4", callback_data='4'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 2 вы видите:'+see(id, 2)+"\n"+
                             'В локации 4 вы видите:' + see(id, 4)+"\n"
                             ,reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['4']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="3", callback_data='3'))
        Keyboard.add(types.InlineKeyboardButton(text="6", callback_data='6'))
        Keyboard.add(types.InlineKeyboardButton(text="7", callback_data='7'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 3 вы видите:'+see(id, 3)+"\n"+
                             'В локации 6 вы видите:' + see(id, 6)+"\n"+
                             'В локации 7 вы видите:' + see(id, 7)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['5']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="8", callback_data='8'))
        Keyboard.add(types.InlineKeyboardButton(text="1", callback_data='1'))
        Keyboard.add(types.InlineKeyboardButton(text="2", callback_data='2'))
        Keyboard.add(types.InlineKeyboardButton(text="9", callback_data='9'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 8 вы видите:'+see(id, 8)+"\n"+
                             'В локации 1 вы видите:' + see(id, 1)+"\n"+
                             'В локации 2 вы видите:' + see(id, 2)+"\n"+
                             'В локации 9 вы видите:' + see(id, 9)+"\n"
                             ,reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['6']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="21", callback_data='21'))
        Keyboard.add(types.InlineKeyboardButton(text="11", callback_data='11'))
        Keyboard.add(types.InlineKeyboardButton(text="4", callback_data='4'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 21 вы видите:'+see(id, 21)+"\n"+
                             'В локации 11 вы видите:' + see(id, 11)+"\n"+
                             'В локации 4 вы видите:' + see(id, 4)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['7']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="4", callback_data='4'))
        Keyboard.add(types.InlineKeyboardButton(text="13", callback_data='13'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 4 вы видите:'+see(id, 4)+"\n"+
                             'В локации 13 вы видите:' + see(id, 13)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['8']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="1", callback_data='1'))
        Keyboard.add(types.InlineKeyboardButton(text="5", callback_data='5'))
        Keyboard.add(types.InlineKeyboardButton(text="19", callback_data='19'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 1 вы видите:'+see(id, 1)+"\n"+
                             'В локации 5 вы видите:' + see(id, 5)+"\n"+
                             'В локации 19 вы видите:' + see(id, 19)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['9']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="5", callback_data='5'))
        Keyboard.add(types.InlineKeyboardButton(text="10", callback_data='10'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 5 вы видите:'+see(id, 5)+"\n"+
                             'В локации 10 вы видите:' + see(id, 10)+"\n"
                             ,reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['10']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="9", callback_data='9'))
        Keyboard.add(types.InlineKeyboardButton(text="21", callback_data='21'))
        Keyboard.add(types.InlineKeyboardButton(text="11", callback_data='11'))
        Keyboard.add(types.InlineKeyboardButton(text="20", callback_data='20'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 9 вы видите:'+see(id, 9)+"\n"+
                             'В локации 21 вы видите:' + see(id, 21)+"\n"+
                             'В локации 11 вы видите:' + see(id, 11)+"\n"+
                          'В локации 20 вы видите:' + see(id, 20)+"\n"  ,reply_markup=Keyboard)


        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['11']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="20", callback_data='20'))
        Keyboard.add(types.InlineKeyboardButton(text="10", callback_data='10'))
        Keyboard.add(types.InlineKeyboardButton(text="6", callback_data='6'))
        Keyboard.add(types.InlineKeyboardButton(text="12", callback_data='12'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 20 вы видите:'+see(id, 20)+"\n"+
                             'В локации 10 вы видите:' + see(id, 10)+"\n"+
                             'В локации 6 вы видите:' + see(id, 6)+"\n"+
                              'В локации 12 вы видите:' + see(id, 12)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['12']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="11", callback_data='11'))
        Keyboard.add(types.InlineKeyboardButton(text="15", callback_data='15'))
        Keyboard.add(types.InlineKeyboardButton(text="14", callback_data='14'))
        Keyboard.add(types.InlineKeyboardButton(text="13", callback_data='13'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 11 вы видите:'+see(id, 11)+"\n"+
                             'В локации 15 вы видите:' + see(id, 15)+"\n"+
                             'В локации 14 вы видите:' + see(id, 14)+"\n"+
                             'В локации 13 вы видите:' + see(id, 13)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['13']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="7", callback_data='7'))
        Keyboard.add(types.InlineKeyboardButton(text="12", callback_data='12'))
        Keyboard.add(types.InlineKeyboardButton(text="14", callback_data='14'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 7 вы видите:'+see(id, 7)+"\n"+
                             'В локации 12 вы видите:' + see(id, 12)+"\n"+
                             'В локации 14 вы видите:' + see(id, 14)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['14']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="15", callback_data='15'))
        Keyboard.add(types.InlineKeyboardButton(text="12", callback_data='12'))
        Keyboard.add(types.InlineKeyboardButton(text="13", callback_data='13'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 15 вы видите:'+see(id, 15)+"\n"+
                             'В локации 12 вы видите:' + see(id, 12)+"\n"+
                             'В локации 13 вы видите:' + see(id, 13)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['15']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="16", callback_data='16'))
        Keyboard.add(types.InlineKeyboardButton(text="12", callback_data='12'))
        Keyboard.add(types.InlineKeyboardButton(text="14", callback_data='14'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 16 вы видите:'+see(id, 16)+"\n"+
                             'В локации 12 вы видите:' + see(id, 12)+"\n"+
                             'В локации 14 вы видите:' + see(id, 14)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['16']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="17", callback_data='17'))
        Keyboard.add(types.InlineKeyboardButton(text="20", callback_data='20'))
        Keyboard.add(types.InlineKeyboardButton(text="15", callback_data='15'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 17 вы видите:'+see(id, 17)+"\n"+
                             'В локации 20 вы видите:' + see(id, 20)+"\n"+
                             'В локации 15 вы видите:' + see(id, 15)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['17']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="18", callback_data='18'))
        Keyboard.add(types.InlineKeyboardButton(text="20", callback_data='20'))
        Keyboard.add(types.InlineKeyboardButton(text="16", callback_data='16'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 18 вы видите:'+see(id, 18)+"\n"+
                             'В локации 20 вы видите:' + see(id, 20)+"\n"+
                             'В локации 16 вы видите:' + see(id, 16)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['18']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="19", callback_data='19'))
        Keyboard.add(types.InlineKeyboardButton(text="17", callback_data='17'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 19 вы видите:'+see(id, 19)+"\n"+
                             'В локации 17 вы видите:' + see(id, 17)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['19']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="8", callback_data='8'))
        Keyboard.add(types.InlineKeyboardButton(text="18", callback_data='18'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 8 вы видите:'+see(id, 8)+"\n"+
                             'В локации 18 вы видите:' + see(id, 18)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['20']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="17", callback_data='17'))
        Keyboard.add(types.InlineKeyboardButton(text="16", callback_data='16'))
        Keyboard.add(types.InlineKeyboardButton(text="10", callback_data='10'))
        Keyboard.add(types.InlineKeyboardButton(text="11", callback_data='11'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 17 вы видите:'+see(id, 17)+"\n"+
                             'В локации 16 вы видите:' + see(id, 16)+"\n"+
                             'В локации 10 вы видите:' + see(id, 10)+"\n"+
                             'В локации 11 вы видите:' + see(id, 11)+"\n"
        ,reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id

    elif dataa.game.person[id]['loc']['21']==2:
        Keyboard=types.InlineKeyboardMarkup()
        Keyboard.add(types.InlineKeyboardButton(text="10", callback_data='10'))
        Keyboard.add(types.InlineKeyboardButton(text="6", callback_data='6'))
        Keyboard.add(types.InlineKeyboardButton(text="Назад", callback_data='back'))
        msg=bot.send_message(id, 'В локации 10 вы видите:'+see(id, 10)+"\n"+
                             'В локации 6 вы видите:' + see(id, 6)+"\n",reply_markup=Keyboard)
        dataa.game.person[id]['special'] = msg.message_id
                             
                             
                             




            
            

        
    

def gamebreak():
    dataa.game.person.clear
    dataa.players.clear
    dataa.chats.clear
    dataa.x=0
    dataa.eaglepoints=0
    dataa.rabbitpoints=0
    dataa.wolfpoints=0
    dataa.w=0
    dataa.q=0
    dataa.z=0
    dataa.e=0
    dataa.k=0
    dataa.gotov=0
    for id in dataa.timers:        
        bot.send_message(id, 'Игра отменена - не все игроки нажали /ready')
    
    









def createUser(id):
    return {'animal':random.choice(dataa.game.spisok),
            'readys':0,
            'fightout':0,
            'x':0,
            'hod':-2,
            'y':'',
            'stat':0,
            'grasses':0,
            'miranimal':'',
            'selfid':id,
            'fightwith':0,
            'die':0,
            'textt':'',
            'seelocation':[],
            'escapelist':[],
            'notrun':[],
            'losetarget':0,
            'fightwithhunt':0,
            'hunter':0,
            'right':0,
            'left':0,
            'alreadydraka':0,
            'alreadysee':0,
            'text':'',
            'grasseat':0,
            'fight':0,
            'sawanimal':'',
            'timeanimal':'',
            'timenumber':0,
            'hp':0,
            'food':0,
            'travell':0,
            'vision':0,
            'hide':0,
            'speed':0,
            'dmg':0,
            'special':0,
            'loc':{'1':0,
                   '2':0,
                   '3':0,
                   '4':0,
                   '5':0,
                   '6':0,
                   '7':0,
                   '8':0,
                   '9':0,
                   '10':0,
                   '11':0,
                   '12':0,
                   '13':0,
                   '14':0,
                   '15':0,
                   '16':0,
                   '17':0,
                   '18':0,
                   '19':0,
                   '20':0,
                   '21':0
                  }
            }

def locchoice(id):           
    if dataa.e==1:        
        dataa.game.person[id]['loc']['1']=2
        dataa.game.person[id]['timenumber']='1'
    elif dataa.e==2:
        dataa.game.person[id]['loc']['2']=2
        dataa.game.person[id]['timenumber'] = '2'
    elif dataa.e==3:
        dataa.game.person[id]['loc']['3']=2
        dataa.game.person[id]['timenumber'] = '3'
    elif dataa.e==4:
        dataa.game.person[id]['loc']['4']=2
        dataa.game.person[id]['timenumber'] = '4'
    elif dataa.e==5:
        dataa.game.person[id]['loc']['5']=2
        dataa.game.person[id]['timenumber'] = '5'
    elif dataa.e==6:
        dataa.game.person[id]['loc']['6']=2
        dataa.game.person[id]['timenumber'] = '6'
    elif dataa.e==7:
        dataa.game.person[id]['loc']['7']=2
        dataa.game.person[id]['timenumber'] = '7'
    elif dataa.e==8:
        dataa.game.person[id]['loc']['8']=2
        dataa.game.person[id]['timenumber'] = '8'
    elif dataa.e==9:
        dataa.game.person[id]['loc']['9']=2
        dataa.game.person[id]['timenumber'] = '9'
    elif dataa.e==10:
        dataa.game.person[id]['loc']['10']=2
        dataa.game.person[id]['timenumber'] = '10'
    elif dataa.e==11:
        dataa.game.person[id]['loc']['11']=2
        dataa.game.person[id]['timenumber'] = '11'
    elif dataa.e==12:
        dataa.game.person[id]['loc']['12']=2
        dataa.game.person[id]['timenumber'] = '12'
    elif dataa.e==13:
        dataa.game.person[id]['loc']['13']=2
        dataa.game.person[id]['timenumber'] = '13'
    elif dataa.e==14:
        dataa.game.person[id]['loc']['14']=2
        dataa.game.person[id]['timenumber'] = '14'
    elif dataa.e==15:
        dataa.game.person[id]['loc']['15']=2
        dataa.game.person[id]['timenumber'] = '15'
    elif dataa.e==16:
        dataa.game.person[id]['loc']['16']=2
        dataa.game.person[id]['timenumber'] = '16'
    elif dataa.e==17:
        dataa.game.person[id]['loc']['17']=2
        dataa.game.person[id]['timenumber'] = '17'
    elif dataa.e==18:
        dataa.game.person[id]['loc']['18']=2
        dataa.game.person[id]['timenumber'] = '18'
    elif dataa.e==19:
        dataa.game.person[id]['loc']['19']=2
        dataa.game.person[id]['timenumber'] = '19'
    elif dataa.e==20:
        dataa.game.person[id]['loc']['20']=2
        dataa.game.person[id]['timenumber'] = '20'
    elif dataa.e==20:
        dataa.game.person[id]['loc']['21']=2
        dataa.game.person[id]['timenumber'] = '21'
    

@bot.message_handler(commands=['begin'])
def begin_message(message):
  if message.chat.id not in list(dataa.chats):
    if dataa.x==0:
      bot.send_message(message.chat.id, "Начинается набор игроков! /join для присоединения")
      dataa.chats.append(message.chat.id)                  
  else:
    bot.send_message(message.chat.id, "Игра уже была запущена! /join для присоединения")

@bot.message_handler(commands=['join'])
def join_message(message):
  #bot.send_message(441399484,str(message.from_user.first_name)+"\n"+str(message.from_user.id))
  if message.from_user.id not in list(dataa.players):
    if message.chat.id in list(dataa.chats):
      if dataa.x==0:
        if message.from_user.id not in dataa.game.aidi:
          #emoj=emojize(':cake:', use_aliases=True)
          dataa.game.aidi.append(message.from_user.id)
          dataa.game.person[message.from_user.id] = createUser(message.from_user.id)        
          dataa.players.append(message.from_user.id)        
          bot.send_message(message.from_user.id, "Вы успешно присоединились!")                           
         # bot.send_message(message.chat.id, message.from_user.id)
          bot.send_message(message.chat.id, text="Количество игроков: "+"\n"+str(len(dataa.players)))
         # bot.send_message(message.chat.id, 'Ты - '+data.game.person[message.from_user.id]['animal'])
         # bot.send_message(message.chat.id, 'хп - '+str(data.game.person[message.from_user.id]['hp']))
    else:
      bot.send_message(message.chat.id, "Нет запущенной игры! /begin для начала.")
  else:
        pass
      

    
@bot.message_handler(commands=['cancel'])
def cancel_message(message):
  if dataa.x==0:
    if len(dataa.chats)>0:
      dataa.players.clear()
      dataa.chats.clear()
      bot.send_message(message.chat.id, "Игра отменена.")



#@bot.message_handler(commands=['win'])
#def win_message(message):
 # if data.x==1:
  #  for id in list(data.chats):
   #   if message.from_user.id in list(data.players):
    #    bot.send_message(id, message.from_user.first_name+" выиграл!")
    #    data.players.clear()
     #   data.chats.clear()
      #  data.x=0
  


  

@bot.callback_query_handler(func=lambda call: True)
def inline(call):
  if call.data=='zz':
    bot.edit_message_text(chat_id=call.message.chat.id,text='zz', parse_mode='Markdown')
  else:
    pass

   
    
    
@bot.message_handler(commands=['start'])
def start_message(message):
  if len(dataa.players)>0:    
    if dataa.x==0:      
      bot.send_message(message.chat.id, "Игра начинается!")
      dataa.x=1
      for id in dataa.game.person:
          dataa.game.person[id]['x']=1
      dataa.timers.append(message.chat.id)
      #breaktimer=threading.Timer(6.0, gamebreak)
      #breaktimer.start()
      for id in dataa.game.person: 
          if dataa.game.person[id]['animal']=='Eagle':
              dataa.eaglepoints=dataa.eaglepoints+1
              dataa.game.person[id]['hp']=200
              dataa.game.person[id]['food']=6
              dataa.game.person[id]['travell']=1
              dataa.game.person[id]['vision']=100
              dataa.game.person[id]['hide']=20
              dataa.game.person[id]['speed']=60
              dataa.game.person[id]['dmg']=60
              dataa.game.person[id]['hunter']=1
              

              dataa.e=random.randint(4,20)
              dataa.w=dataa.e
              locchoice(id)
              eagle=emojize(':eagle:', use_aliases=True)
              bot.send_message(id, 'ты - '+eagle+'орел, поздравляю!')
              dataa.predatornumber = dataa.predatornumber + 1

              
          elif dataa.game.person[id]['animal']=='Wolf':
              dataa.wolfpoints=dataa.wolfpoints+1
              dataa.game.person[id]['hp']=200
              dataa.game.person[id]['food']=6
              dataa.game.person[id]['travell']=1
              dataa.game.person[id]['vision']=100
              dataa.game.person[id]['hide']=20
              dataa.game.person[id]['speed']=40
              dataa.game.person[id]['dmg']=50
              dataa.game.person[id]['hunter']=1

              dataa.e=random.randint(4,20)
              if dataa.e!=dataa.w:
                  dataa.q=dataa.e
                  locchoice(id)
              else:
                  dataa.game.person[id]['loc']['2']=2
              wolf = emojize(':wolf:', use_aliases=True)
              bot.send_message(id, 'ты - ' + wolf + 'Волк, поздравляю!')
              dataa.predatornumber=dataa.predatornumber+1


              
          elif dataa.game.person[id]['animal']=='Rabbit':
              dataa.rabbitpoints=dataa.rabbitpoints+1
              dataa.game.person[id]['hp']=1
              dataa.game.person[id]['food']=4
              dataa.game.person[id]['travell']=1
              dataa.game.person[id]['vision']=100
              dataa.game.person[id]['hide']=20
              dataa.game.person[id]['speed']=80
              dataa.game.person[id]['dmg']=0
              dataa.game.person[id]['grasseat']=1

              dataa.e=random.randint(4,20)
              if dataa.e!=dataa.w and dataa.e!=dataa.q:                                   
                  if dataa.e!=dataa.w:
                      locchoice(id)                   
              else:
                  dataa.game.person[id]['loc']['3']=2
              rabbit = emojize(':rabbit:', use_aliases=True)
              bot.send_message(id, 'ты - ' + rabbit + 'Кролик, поздравляю!')
      bot.send_message(message.chat.id, 'кол-во кроликов:'+str(dataa.rabbitpoints)+' кол-во волков:'+str(dataa.wolfpoints)+' кол-во орлов:'+str(dataa.eaglepoints))
      maingame()   
          
          #bot.send_message(id, 'Нажмите /ready для подтверждения готовности; игра будет автоматически удалена через 1 минуту')
  elif len(dataa.players)>0:
      bot.send_message(message.chat.id, "Недостаточно игроков!")
  else:
    bot.send_message(message.chat.id, "Нет запущенной игры! /begin для начала.")

      
def currentloc(dict):   
    for key in dict:              
        if dict[key]==2:        
            return key
    return 'Игра не началась!'

def seeloc(dict, id):
    for key in dict:
        if dict[key]==1:        
            dataa.game.person[id]['seelocation'].append(key)
    return 'Игра не началась!'
    


                             

                             
    
    
                            


def send(id):
    for item in dataa.game.person[id]['seelocation']:
        dataa.game.person[id]['textt']+=item+', '
    z=len(dataa.game.person[id]['textt'])
    dataa.game.person[id]['textt']=dataa.game.person[id]['textt'][:(z-2)]
    #if dataa.game.person[id]['seelocation']==[]:
    if dataa.game.person[id]['x']==0:
        return 'Игра не началась!'
    return dataa.game.person[id]['textt']
        





@bot.message_handler(commands=['stats'])
def stats_message(message):
    if message.from_user.id in dataa.game.person:
      seeloc(dataa.game.person[message.from_user.id]['loc'], message.from_user.id)
        #bot.send_message(message.from_user.id, sendmap)
      bot.send_message(message.from_user.id, 'Локация: '+currentloc(dataa.game.person[message.from_user.id]['loc'])+"\n"+
                     'Видимые локации: '+send(message.from_user.id)+"\n"+
                     'С вами в локации: '+dataa.game.person[message.from_user.id]['miranimal']+"\n"+
                     'Животное: '+str(dataa.game.person[message.from_user.id]['animal'])+"\n"+
                     'ХП: '+str(dataa.game.person[message.from_user.id]['hp'])+"\n"+
                     'Еда: '+str(dataa.game.person[message.from_user.id]['food'])+"\n"+
                     'На сколько локаций может переместиться: '+str(dataa.game.person[message.from_user.id]['travell'])+"\n"+
                     'Зрение: '+str(dataa.game.person[message.from_user.id]['vision'])+"\n"+
                     'Маскировка: '+str(dataa.game.person[message.from_user.id]['hide'])+"\n"+
                     'Скорость: '+str(dataa.game.person[message.from_user.id]['speed'])+"\n"+
                     'Урон: '+str(dataa.game.person[message.from_user.id]['dmg'])+"\n"                    
                       )
      dataa.game.person[message.from_user.id]['textt']=''
      dataa.game.person[message.from_user.id]['seelocation'] = []
      dataa.game.person[message.from_user.id]['stat']=1






#@bot.message_handler(commands=['ready'])
#def ready():
#    if dataa.x==1:
#        Keyboard=types.InlineKeyboardMarkup()
#        Keyboard.add((types.InlineKeyboardButton(text="Я готов!", callback_data='gotov')))
#        msg=bot.send_message(message.from_user.id, 'Нажмите для подтверждения готовности; игра будет автоматически удалена через 1 минуту',
#                         reply_markup=Keyboard)
    
    


#@bot.callback_query_handler(func=lambda call:True)
#def inline(call):
#    print(call.data)
#    if call.data=='gotov':
#        bot.send_message(call.message.chat.id, 'sosi')
#, parse_mode='Markdown'

def changeloc(id):
        
    if dataa.game.person[id]['loc']['1']==2:        
            
        dataa.game.person[id]['loc']['2']=1
        dataa.game.person[id]['loc']['5']=1
        dataa.game.person[id]['loc']['8']=1
            
    elif dataa.game.person[id]['loc']['2']==2:
            
        dataa.game.person[id]['loc']['1']=1
        dataa.game.person[id]['loc']['3']=1
        dataa.game.person[id]['loc']['5']=1
            
    elif dataa.game.person[id]['loc']['3']==2:
        
        dataa.game.person[id]['loc']['2']=1
        dataa.game.person[id]['loc']['4']=1
            
    elif dataa.game.person[id]['loc']['4']==2:
            
        dataa.game.person[id]['loc']['6']=1
        dataa.game.person[id]['loc']['3']=1
        dataa.game.person[id]['loc']['7']=1
            
    elif dataa.game.person[id]['loc']['5']==2:
        
        dataa.game.person[id]['loc']['1']=1
        dataa.game.person[id]['loc']['2']=1
        dataa.game.person[id]['loc']['8']=1
        dataa.game.person[id]['loc']['9']=1
            
    elif dataa.game.person[id]['loc']['6']==2:
        
        dataa.game.person[id]['loc']['21']=1
        dataa.game.person[id]['loc']['11']=1
        dataa.game.person[id]['loc']['4']=1
     
    elif dataa.game.person[id]['loc']['7']==2:

        dataa.game.person[id]['loc']['13']=1
        dataa.game.person[id]['loc']['4']=1

    elif dataa.game.person[id]['loc']['8']==2:

        dataa.game.person[id]['loc']['19']=1
        dataa.game.person[id]['loc']['5']=1
        dataa.game.person[id]['loc']['1']=1

    elif dataa.game.person[id]['loc']['9']==2:
        
        dataa.game.person[id]['loc']['5']=1
        dataa.game.person[id]['loc']['10']=1

    elif dataa.game.person[id]['loc']['10']==2:

        dataa.game.person[id]['loc']['9']=1
        dataa.game.person[id]['loc']['11']=1
        dataa.game.person[id]['loc']['20']=1
        dataa.game.person[id]['loc']['21']=1

    elif dataa.game.person[id]['loc']['11']==2:

        dataa.game.person[id]['loc']['10']=1
        dataa.game.person[id]['loc']['6']=1
        dataa.game.person[id]['loc']['20']=1
        dataa.game.person[id]['loc']['12']=1

    elif dataa.game.person[id]['loc']['12']==2:

        dataa.game.person[id]['loc']['11']=1
        dataa.game.person[id]['loc']['13']=1
        dataa.game.person[id]['loc']['14']=1
        dataa.game.person[id]['loc']['15']=1

    elif dataa.game.person[id]['loc']['13']==2:

        dataa.game.person[id]['loc']['12']=1
        dataa.game.person[id]['loc']['14']=1
        dataa.game.person[id]['loc']['7']=1

    elif dataa.game.person[id]['loc']['14']==2:

        dataa.game.person[id]['loc']['12']=1
        dataa.game.person[id]['loc']['13']=1
        dataa.game.person[id]['loc']['15']=1

    elif dataa.game.person[id]['loc']['15']==2:

        dataa.game.person[id]['loc']['16']=1
        dataa.game.person[id]['loc']['12']=1
        dataa.game.person[id]['loc']['14']=1

    elif dataa.game.person[id]['loc']['16']==2:

        dataa.game.person[id]['loc']['17']=1
        dataa.game.person[id]['loc']['20']=1
        dataa.game.person[id]['loc']['15']=1

    elif dataa.game.person[id]['loc']['17']==2:

        dataa.game.person[id]['loc']['18']=1
        dataa.game.person[id]['loc']['20']=1
        dataa.game.person[id]['loc']['16']=1

    elif dataa.game.person[id]['loc']['18']==2:

        dataa.game.person[id]['loc']['19']=1
        dataa.game.person[id]['loc']['17']=1

    elif dataa.game.person[id]['loc']['19']==2:

        dataa.game.person[id]['loc']['18']=1
        dataa.game.person[id]['loc']['8']=1

    elif dataa.game.person[id]['loc']['20']==2:

        dataa.game.person[id]['loc']['11']=1
        dataa.game.person[id]['loc']['10']=1
        dataa.game.person[id]['loc']['17']=1
        dataa.game.person[id]['loc']['16']=1

    elif dataa.game.person[id]['loc']['21']==2:

        dataa.game.person[id]['loc']['6']=1
        dataa.game.person[id]['loc']['10']=1
       
               





    
def endgame():
    pass





def xod():
    if dataa.predatornumber > 0:
        for id in dict(dataa.game.person):
            if dataa.game.person[id]['die']!=1:
              changeloc(id)
        go()
        if dataa.ren==1:
            dataa.maintimer.cancel()
            dataa.ren=0
        xodtime=threading.Timer(6.0, endturn)
        xodtime.start()
        dataa.ren=1
        dataa.maintimer=xodtime


    else:
        endgame()



def maingame():
    xod()



    
    





if __name__ == '__main__':
  bot.polling(none_stop=True)

