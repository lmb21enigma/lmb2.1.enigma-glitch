# -*- coding: utf-8 -*-
from flask import Flask
from threading import Thread
import datetime
import random
import re
CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

app = Flask('')
      
def glitchme():
    while(1):
      time.sleep(120)
      try:
        res = requests.get("https://sand-balanced-cathedral.glitch.me/")
      except:
        print("glitch respond late")
        
@app.route('/')
def home():
    return "Hello. Request Bot am alive!"


def run():
    background_thread = Thread(target=glitchme)
    background_thread.start()
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


import discord
import os
import requests
import time
from threading import Thread
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import six
import asyncio
import json

codes = []
main_codes=[]
lcodes=[]

redata=dict()
maindataone=dict()
maindatatwo=dict()

admins = list(str(os.getenv('admin')).split(","))

client = discord.Client(intents=discord.Intents.default())

def render_mpl_table(data,
                     fname,
                     col_width=3.0,
                     row_height=0.625,
                     font_size=14,
                     header_color='#000',
                     row_colors=['#f1f1f2', 'w'],
                     edge_color='w',
                     bbox=[0, 0, 1, 1],
                     header_columns=0,
                     ax=None,
                     **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array(
            [col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values,
                         bbox=bbox,
                         colLabels=data.columns,
                         cellLoc='center',
                         **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0] % len(row_colors)])
    fig.savefig(fname)


def sub_redeem(i, temp,names, code, ops):
        global redata
        try:
          # print(datetime.datetime.now())
          URL = 'https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902'
          payload = {
              'ac': 'get_gifts',
              'type':'0',
              'iggid': str(temp[i - 1]),
              'charname': '',
              'cdkey': str(code),
              'lang': 'en',
          }
          response = requests.post(URL, data=payload)
          # print(response.text)
          finalme=str(json.loads(response.text)['msg'])
          finalme=cleanhtml(finalme)
          print(finalme)
          # print(datetime.datetime.now())
          # channel = client.get_channel(int(os.getenv('chanlnel_id')))
          # send_msg(channel, "\n----------------------------------------------------------\nGame Name :- " + str(names[i - 1]) + ", Code :- " +str(code) + ", Result From IGG :- \n" + str(finalme)+"\n----------------------------------------------------------\n")
          # print(datetime.datetime.now())
        except Exception as e:
          print("Error :- ", e)
          channel = client.get_channel(int(os.getenv('chanlnel_id')))
          send_msg(channel, "Serious Issue Occured from IGG :-\n" + str(e))
          finalme=str(e)
        redata[code][names[i-1]]=finalme

def redeem(code, ops,itime):
    global redata
    print(time.ctime())
    data = pd.read_csv(os.getenv('data_sheet'))
    temp = list(data['ID'])
    names=list(data['Game Name'])
    c = len(temp)
    redata[code]=dict()
    for i in range(1, c + 1):
        # sub_redeem(i,temp,code):
        background_thread = Thread(target=sub_redeem,
                                   args=(
                                       i,
                                       temp,
                                      names,
                                       code,
                                       ops,
                                   ))
        background_thread.start()
        # response = requests.get("https://lmcrbot-" + str(i) +
        #                         ".vercel.app/" + str(temp[i - 1]) + "/" +
        #                         str(code))
        # print("Bot-", i, response.status_code, time.ctime())
        # if (response.status_code == 504):
        #     time.sleep(2)
        #     response = requests.get("https://lmcrbot-" + str(i) +
        #                             ".vercel.app/" + str(temp[i - 1]) +
        #                             "/" + str(code))
        #     print("Bot-", i, response.status_code, time.ctime())
    # print("🚀", code, "Redemeed Successfully...!!!")
    channelx = client.get_channel(int(os.getenv('schan')))      
    while(len(temp)!=len(redata[code].keys())):
      # print(len(temp),len(redata[code]))
      pass
    import datetime
    seconds_in_day = 24 * 60 * 60
    mtime=datetime.datetime.now()
    difference = mtime - itime
    redeemtime=str(difference)
    # send_msg(
    #     ops, "🚀 " + str(code) +
    #     " Received Successfully...!!!\n=================================="+str(redata[code]))
    embed=discord.Embed(title="🎉 Record For Code 📣 "+str(code)+ " ✅",color=discord.Color.green())
    # print(redata[code],type(redata[code]))
    for k in redata[code].keys():
        embed.add_field(name="😎  "+str(k) +"  🤗", value="> "+str(redata[code][k])+"\n🧿 ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ ⛄ ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ 🧿", inline=False)
    client.loop.create_task(ops.send(embed=embed))
    ltime=datetime.datetime.now()
    difference = ltime - itime
    totaltime=str(difference)
    difference = ltime - mtime
    msgtime=str(difference)
    embed1=discord.Embed(title="🎉 Time Taken For Code 📣 "+str(code)+ " ✅",color=discord.Color.blue())
    timemsg=f"🎉 Redeem Time :- {redeemtime} microseconds\n> 📝 Messsage Time :- {msgtime} microseconds\n> 🕕 Total Time Taken :- {totaltime} microseconds"
    embed1.add_field(name="😎 Time Checker  🤗", value="> "+str(timemsg)+"\n🧿 ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ ⛄ ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ 🧿", inline=False)
    client.loop.create_task(ops.send(embed=embed1))
    if(channelx!=ops):
      client.loop.create_task(channelx.send(embed=embed))
      client.loop.create_task(channelx.send(embed=embed1))


def main_sub_redeem_one(i, temp,names, code, ops):
        global maindataone
        try:
          # print(datetime.datetime.now())
          URL = 'https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902'
          payload = {
              'ac': 'get_gifts',
              'type':'0',
              'iggid': str(temp[i - 1]),
              'charname': '',
              'cdkey': str(code),
              'lang': 'en',
          }
          response = requests.post(URL, data=payload)
          finalme=str(json.loads(response.text)['msg'])
          finalme=cleanhtml(finalme)
          print(finalme)
        except Exception as e:
          print("Error :- ", e)
          finalme=str(e)
        maindataone[code][names[i-1]]=finalme
      
def main_sub_redeem_two(i, temp,names, code, ops):
        global maindatatwo
        try:
          # print(datetime.datetime.now())
          URL = 'https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902'
          payload = {
              'ac': 'get_gifts',
              'type':'0',
              'iggid': str(temp[i - 1]),
              'charname': '',
              'cdkey': str(code),
              'lang': 'en',
          }
          response = requests.post(URL, data=payload)
          finalme=str(json.loads(response.text)['msg'])
          finalme=cleanhtml(finalme)
          print(finalme)
        except Exception as e:
          print("Error :- ", e)
          finalme=str(e)
        maindatatwo[code][names[i-1]]=finalme
        
def main_redeem_one(code, ops):
    global maindataone
    print(time.ctime())
    data = pd.read_csv(os.getenv('mainsheet1'))
    temp = list(data['ID'])
    names=list(data['Game Name'])
    c = len(temp)
    maindataone[code]=dict()
    for i in range(1, c + 1):
        background_thread = Thread(target=main_sub_redeem_one,
                                   args=(
                                       i,
                                       temp,
                                      names,
                                       code,
                                       ops,
                                   ))
        background_thread.start()
    channelx = client.get_channel(int(os.getenv('mainchannel1')))      
    while(len(temp)!=len(maindataone[code].keys())):
      pass
    embed=discord.Embed(title="🎉 Record For Code 📣 "+str(code)+ " ✅",color=discord.Color.green())
    for k in maindataone[code].keys():
        embed.add_field(name="😎  "+str(k) +"  🤗", value="> "+str(maindataone[code][k])+"\n🧿 ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ ⛄ ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ 🧿", inline=False)
    client.loop.create_task(channelx.send(embed=embed))
     
def main_redeem_two(code, ops):
    global maindatatwo
    print(time.ctime())
    data = pd.read_csv(os.getenv('mainsheet2'))
    temp = list(data['ID'])
    names=list(data['Game Name'])
    c = len(temp)
    maindatatwo[code]=dict()
    for i in range(1, c + 1):
        background_thread = Thread(target=main_sub_redeem_two,
                                   args=(
                                       i,
                                       temp,
                                      names,
                                       code,
                                       ops,
                                   ))
        background_thread.start()
    channelx = client.get_channel(int(os.getenv('mainchannel2')))      
    while(len(temp)!=len(maindatatwo[code].keys())):
      pass
    embed=discord.Embed(title="🎉 Record For Code 📣 "+str(code)+ " ✅",color=discord.Color.green())
    for k in maindatatwo[code].keys():
        embed.add_field(name="😎  "+str(k) +"  🤗", value="> "+str(maindatatwo[code][k])+"\n🧿 ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ ⛄ ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ 🧿", inline=False)
    client.loop.create_task(channelx.send(embed=embed))      

    
    
    
    
    
    
guess_code = dict()
guess_thread = []


def redeem_it(ids, code, name):
    global guess_code
    URL = 'https://lordsmobile.igg.com/project/gifts/ajax.php?game_id=1051029902'
    payload = {
    'ac': 'get_gifts',
    'type':'0',
    'iggid': str(ids),
    'charname': '',
    'cdkey': str(code),
    'lang': 'en',
    }
    response = requests.post(URL, data=payload)
    finalme=str(json.loads(response.text)['msg'])
    finalme=cleanhtml(finalme)
    print(finalme)
    if(finalme.strip()=="Congratulations! You won: 1,000 Gems *5".strip()):
        background_thread = Thread(target=main_redeem_two,
                                           args=(
                                               str(code),
                                               '',
                                           ))
        background_thread.start()
    guess_code[code] = [ids, name, finalme]


def add_redeem(code):
    global guess_code
    guess_code = dict()
    guess_thread=[]
    data = pd.read_csv(os.getenv('mainsheet2'))
    ids = list(data['ID'])
    names=list(data['Game Name'])
    start = datetime.datetime.now()
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while(len(l) > 0):
        for i in range(len(ids)):
            random_num = random.choice(l)
            l.remove(random_num)
            import threading
            do_it = threading.Thread(target=redeem_it, args=(
                int(ids[i]), code.replace(".", str(random_num)).upper(), names[i]))
            do_it.start()
            guess_thread.append(do_it)
    for x in guess_thread:
        x.join()
    print(guess_code)
    end = datetime.datetime.now()
    print(end-start)
    channelx = client.get_channel(int(os.getenv('mainchannel2')))      
    embed=discord.Embed(title="🎉 Record For Code 📣 "+str(code)+ " ✅",color=discord.Color.green())
    for k in guess_code.keys():
        embed.add_field(name="😎  code :- "+str(k) + " name :- " + guess_code[k][1] +"  🤗", value="> "+str(guess_code[k][2])+"\n🧿 ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ ⛄ ~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~~-~ 🧿", inline=False)
    client.loop.create_task(channelx.send(embed=embed))      
    
    
    
    
    

    
    
    
    
    
    
def send_msg(ops, msg):
    client.loop.create_task(ops.send(msg))


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(
        name="With Lords Mobile Gift Codes"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global codes
    global main_codes
    global lcodes
    if message.author == client.user:
        return

    if message.content.startswith(
        ('&Code@history', '&Code@History', '&code@History', '&code@history',
         '&CODE@HISTORY')):
        if str(message.author.name) in admins:
            msg1 = '🧿{0.author.mention} History of Codes Till Today As Follows...'.format(
                message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')
            if (len(list(
                    pd.read_csv('code_history.csv')["Codes History"])) == 0):
                await message.channel.send("🤐    Co History Is Empty...!!!")
            else:
                await message.channel.send(
                    "\n ----------------------------------------------------------"
                )
                c = 1
                for i in list(
                        pd.read_csv('code_history.csv')["Codes History"]):
                    await message.channel.send('\n' + str(c) + ') ' + str(i))
                    c = c + 1
                await message.channel.send(
                    "\n ----------------------------------------------------------"
                )
                await message.channel.send('=================================='
                                           )
                render_mpl_table(pd.read_csv('code_history.csv'),
                                 "codes.png",
                                 header_columns=0,
                                 col_width=2.0)
                await message.channel.send(file=discord.File('codes.png'))
            await message.channel.send('==================================')
            file_path = "codes.png"
            if os.path.isfile(file_path):
              os.remove(file_path)
        else:
            msg1 = '🧐 {0.author.mention} Warning Its Only For Admins...!!!'.format(
                message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')

    if message.content.startswith(('^help', '^Help')):
        msg1 = '🚀 Hey Dude, Here are bot commands for you !!! {0.author.mention}'.format(
            message)
        await message.channel.send('==================================')
        await message.channel.send(msg1)
        await message.channel.send('==================================')
        await message.channel.send(
            '✅ Bot Commands :-\n1)  ^help\n2) ^hi\n3) ^code LM_Code')
        await message.channel.send('==================================')

    if message.content.startswith(('&help', '&Help')):
        if str(message.author.name) in admins:
            msg1 = '☯ Hey Dude, Here are bot Admin commands for you !!! {0.author.mention}'.format(
                message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')
            await message.channel.send(
                '🎉 Bot Commands :-\n1)  &help\n2) &code@history\n3) &data@history\n4) &code@reset '
            )
            await message.channel.send('==================================')
        else:
            msg1 = '🧐 {0.author.mention} Warning Its Only For Admins...!!!'.format(
                message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')

    if message.content.startswith(('^hi', '^Hi', '^Hii', '^hii')):
        msg1 = '✨ Hey Dude, Welcome Here !!! {0.author.mention}'.format(
            message)
        await message.channel.send('==================================')
        await message.channel.send(msg1)
        await message.channel.send('==================================')
    
    if message.content.startswith(('^code', '^Code','^^code', '^^Code')):
        l = str(message.content)
        li = l.split()
        if (len(li) == 1):
            await message.channel.send("👀 No Code Entered...!!!")
        elif str(li[1].upper()) in codes:
            await message.channel.send(
                "🙄 Duplication Of Code Is Not Allowed...!!!")
        else:
            li[1] = li[1].upper()
            old_code = pd.read_csv('code_history.csv')
            new_code = pd.DataFrame({"Codes History": [li[1]]})
            old_code = pd.concat([old_code, new_code])
            # old_code.append(new_code)
            old_code.to_csv('code_history.csv', index=False)
            await message.channel.send('==================================')
            await message.channel.send(
                '🔰 Code :- {}, Added For Redeemption'.format(li[1]))
            await message.channel.send('==================================')
            await message.channel.send(
                '⛄ Please Wait For a Minute Untill You Enter Another...!!!')
            await message.channel.send('==================================')
            # redeem(li[1])
            background_thread = Thread(target=redeem,
                                       args=(
                                           li[1],
                                           message.channel,
                                       ))
            background_thread.start()
            # await message.channel.send("🚀" + str(li[1]) +
            #                            " ,Redemeed Successfully...!!!")

    if message.content.startswith(
        ('&Data@history', '&data@history', '&Data@History', '&DATA@HISTORY',
         '&data@History')):
        if str(message.author.name) in admins:
            msg1 = '🧿{0.author.mention} Data Is As Follows...'.format(message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')
            if (len(list(pd.read_csv(os.getenv('data_sheet'))["ID"])) == 0):
                await message.channel.send('👀 Data History Is Empty...!!!')
                await message.channel.send('=================================='
                                           )
            else:
                await message.channel.send(
                    pd.read_csv(
                        os.getenv('data_sheet')).to_markdown(index=False))
                await message.channel.send('=================================='
                                           )
                render_mpl_table(pd.read_csv(os.getenv('data_sheet')),
                                 "data.png",
                                 header_columns=0,
                                 col_width=2.0)
                await message.channel.send(file=discord.File('data.png'))
                await message.channel.send('=================================='
                                           )
                file_path = "data.png"
                if os.path.isfile(file_path):
                  os.remove(file_path)
        else:
            msg1 = '🧐 {0.author.mention} Warning Its Only For Admins...!!!'.format(
                message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')

    if message.content.startswith(('&code@reset', '&Code@Reset', '&Code@reset',
                                   '&code@Reset', '&CODE@RESET')):
        if str(message.author.name) in admins:
            await message.channel.send('==================================')
            new_code = pd.DataFrame(columns=["Codes History"])
            new_code.to_csv('code_history.csv', index=False)
            main_codes=[]
            lcodes=[]
            codes=[]
            await message.channel.send("Code History Deleted Successfully..!!!"
                                       )
            await message.channel.send('==================================')
        else:
            msg1 = '🧐 {0.author.mention} Warning Its Only For Admins...!!!'.format(
                message)
            await message.channel.send('==================================')
            await message.channel.send(msg1)
            await message.channel.send('==================================')
    
    if message.content.startswith(('!code', '!Code','!CODE')):
        import datetime
        l = str(message.content)
        li = l.split()
        if (len(li) == 1):
            await message.channel.send("👀 No Code Entered...!!!")
        elif str(li[1].upper()) in codes:
            await message.channel.send(
                "🙄 Duplication Of Code Is Not Allowed...!!!")
        else:
            li[1] = li[1].upper()
            codes.append(li[1])
            old_code = pd.read_csv('code_history.csv')
            new_code = pd.DataFrame({"Codes History": [li[1]]})
            old_code = pd.concat([old_code, new_code])
            # old_code.append(new_code)
            old_code.to_csv('code_history.csv', index=False)
            background_thread = Thread(target=redeem,
                                       args=(
                                           li[1],
                                           message.channel,
                                         datetime.datetime.now(),
                                       ))
            background_thread.start()
    
    if message.content.lower().startswith('!bcode'):
        l = str(message.content)
        li = l.split()
        if (len(li) == 1):
            await message.channel.send("👀 No Code Entered...!!!")
        elif str(li[1].upper()) in main_codes:
            await message.channel.send(
                "🙄 Duplication Of Code Is Not Allowed...!!!")
        else:
            li[1] = li[1].upper()
            main_codes.append(li[1])
            background_thread = Thread(target=main_redeem_one,
                                       args=(
                                           li[1],
                                           message.channel,
                                       ))
            background_thread.start()
            background_thread = Thread(target=main_redeem_two,
                                       args=(
                                           li[1],
                                           message.channel,
                                       ))
            background_thread.start()
            
    if message.content.lower().startswith('!ocode'):
        l = str(message.content)
        li = l.split()
        if (len(li) == 1):
            await message.channel.send("👀 No Code Entered...!!!")
        elif str(li[1].upper()) in main_codes:
            await message.channel.send(
                "🙄 Duplication Of Code Is Not Allowed...!!!")
        else:
            li[1] = li[1].upper()
            background_thread = Thread(target=main_redeem_one,
                                       args=(
                                           li[1],
                                           message.channel,
                                       ))
            background_thread.start()
            
    if message.content.lower().startswith('!mcode'):
        l = str(message.content)
        li = l.split()
        if (len(li) == 1):
            await message.channel.send("👀 No Code Entered...!!!")
        elif str(li[1].upper()) in main_codes:
            await message.channel.send(
                "🙄 Duplication Of Code Is Not Allowed...!!!")
        else:
            li[1] = li[1].upper()
            if '.' in li[1]:
                import threading
                do_it = threading.Thread(target=add_redeem, args=(li[1],))
                do_it.start()

            else:
                background_thread = Thread(target=main_redeem_two,
                                           args=(
                                               li[1],
                                               message.channel,
                                           ))
                background_thread.start()
            await message.channel.send(
                '🔰 Code :- {}, Added For Redeemption'.format(li[1]))
    
    
keep_alive()
loop = asyncio.get_event_loop()
loop.create_task(client.start(os.getenv('TOKEN')))
Thread(target=loop.run_forever).start()
