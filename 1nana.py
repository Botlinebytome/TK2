# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
import requests
from io import StringIO
from threading import Thread
from urllib import urlopen
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,wikipedia,tempfile

cl = LINETCR.LINE()
cl.login(token="Eq4Sp2Xs79dOIlZy46A7.OcHNPPDXFzFo0s25hKNPDW.IrDUU3DRnwaPjBeT3OC1Ui/9biPHNGQ7M5cXKQx6hT4=")
cl.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

myhelpMessage ="""──────┅═ই۝ई═┅──────
╔════════════════
╠==[ DAENG TEAM BOT ]==
╚════════════════
──────┅═ই۝ई═┅──────
       🄲🄾🄼🄼🄰🄽🄳 🄷🄴🄻🄿
──────┅═ই۝ई═┅──────
❂͜͡☆➣ ╠Id
❂͜͡☆➣ ╠Cek @
❂͜͡☆➣ ╠Mid @
❂͜͡☆➣ ╠Gn: 
❂͜͡☆➣ ╠Gname:
❂͜͡☆➣ ╠Cancel
❂͜͡☆➣ ╠tagmem
❂͜͡☆➣ ╠Halo
❂͜͡☆➣ ╠Hola
❂͜͡☆➣ ╠Tag all
❂͜͡☆➣ ╠Lurk on/off
❂͜͡☆➣ ╠Lurkers
❂͜͡☆➣ ╠Intip on/off
❂͜͡☆➣ ╠Intip
❂͜͡☆➣ ╠Apakah
❂͜͡☆➣ ╠Kapan 
❂͜͡☆➣ ╠Berapa
❂͜͡☆➣ ╠Ginfo
❂͜͡☆➣ ╠Glist
❂͜͡☆➣ ╠Memlist
❂͜͡☆➣ ╠Friendlist
❂͜͡☆➣ ╠Friendinfo:
❂͜͡☆➣ ╠Frienpict:
❂͜͡☆➣ ╠Speed
❂͜͡☆➣ ╠.Speed 
❂͜͡☆➣ ╠About
❂͜͡☆➣ ╠About1
❂͜͡☆➣ ╠Runtime
❂͜͡☆➣ ╠Runtime1
❂͜͡☆➣ ╠Detail @
❂͜͡☆➣ ╠Detail grup
❂͜͡☆➣ ╠Pp @
❂͜͡☆➣ ╠Cover @
❂͜͡☆➣ ╠Picturl @
❂͜͡☆➣ ╠Backup:on / off
❂͜͡☆➣ ╠Mybackup
❂͜͡☆➣ ╠Allname:
❂͜͡☆➣ ╠Allbio
❂͜͡☆➣ ╠Invite
❂͜͡☆➣ ╠Blacklist
❂͜͡☆➣ ╠Blacklist:
❂͜͡☆➣ ╠Blacklist @
❂͜͡☆➣ ╠Unban:
❂͜͡☆➣ ╠Unban:on
❂͜͡☆➣ ╠Unban @
❂͜͡☆➣ ╠Whitelist  
❂͜͡☆➣ ╠Whitelist @
──────┅═ই۝ई═┅──────
    🄲🄾🄼🄼🄰🄽🄳 🄰🄳🄼🄸🄽
──────┅═ই۝ई═┅──────
❂͜͡☆➣ ╠•cw
❂͜͡☆➣ ╠•lc
❂͜͡☆➣ ╠•pt
❂͜͡☆➣ ╠•ps
❂͜͡☆➣ ╠•fb
❂͜͡☆➣ ╠Frofileig
❂͜͡☆➣ ╠Music
❂͜͡☆➣ ╠•ms
❂͜͡☆➣ ╠•Music 
❂͜͡☆➣ ╠/musik
❂͜͡☆➣ ╠/musrik
❂͜͡☆➣ ╠•lr
❂͜͡☆➣ ╠Lirik
❂͜͡☆➣ ╠•yt 
❂͜͡☆➣ ╠•Youtube
❂͜͡☆➣ ╠ytsearch
❂͜͡☆➣ ╠Youtube
❂͜͡☆➣ ╠Youtubemp4
❂͜͡☆➣ ╠Gift @
❂͜͡☆➣ ╠List favorite
❂͜͡☆➣ ╠Reboot
❂͜͡☆➣ ╠Hay @
❂͜͡☆➣ ╠Woy! @
❂͜͡☆➣ ╠Spamtag @
❂͜͡☆➣ ╠Update sambutan
❂͜͡☆➣ ╠Papay
──────┅═ই۝ई═┅──────
 🄲🄾🄼🄼🄰🄽🄳 🅂🄴🅃🅃🄸🄽🄶🅂
──────┅═ই۝ई═┅──────
❂͜͡☆➣ ╠Auto join on/off
❂͜͡☆➣ ╠Auto add on/off
❂͜͡☆➣ ╠Leave on/off
❂͜͡☆➣ ╠Backup:on/off
❂͜͡☆➣ ╠Contact on/off
❂͜͡☆➣ ╠Com on/off
❂͜͡☆➣ ╠Share on/off
❂͜͡☆➣ ╠Protect on/off
❂͜͡☆➣ ╠Qrprotect on/off
❂͜͡☆➣ ╠InviteProtect on/off
❂͜͡☆➣ ╠Cancelprotect on/off
❂͜͡☆➣ ╠Set all on/off
❂͜͡☆➣ ╠Panick:on/off
❂͜͡☆➣ ╠Respon on/off
❂͜͡☆➣ ╠Tag on/off
❂͜͡☆➣ ╠Sambutan on/off
❂͜͡☆➣ ╠Simisimi on/off
❂͜͡☆➣ ╠Like:on/off
──────┅═ই۝ई═┅──────
        🅃🅁🄰🄽🅂🄻🄰🅃🄴
──────┅═ই۝ई═┅──────
❂͜͡☆➣ ╠En@id
❂͜͡☆➣ ╠Jp@id
❂͜͡☆➣ ╠Ko@id
❂͜͡☆➣ ╠Ar@id
❂͜͡☆➣ ╠Th@id
❂͜͡☆➣ ╠Say
❂͜͡☆➣ ╠Say-ar
❂͜͡☆➣ ╠Say-jp
❂͜͡☆➣ ╠Say-ko
❂͜͡☆➣ ╠Say-en
──────┅═ই۝ई═┅──────
╔════════════════
╠==[ DAENG TEAM BOT ]==
╚════════════════
──────┅═ই۝ई═┅──────

"""
helo=""

KAC=[cl]
mid = cl.getProfile().mid
admin = []
targets = []
Bots = ["ua02867a697717d97ced12db91e49e977"]
creator = "ua02867a697717d97ced12db91e49e977"
admsa = "ua02867a697717d97ced12db91e49e977"
admin = "ua02867a697717d97ced12db91e49e977"
whitelist=[""]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'AutoJoinCancel':True,
    'Admin':True,
    'Members':1,
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Hayo ketauan nge add",
    "lang":"JP",
    "comment1":"Auto Like By ҉̶̶̘̟̼̉̈́͐͋͌̊D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊ ",
    "commentOn":True,
    "likeOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "me":"me",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "detectMention":True,
    "kickMention":False,
    "Backup":False,
    "atjointicket":True,
    "gift":{},
    "Sider":{},
    "tag":False,
    "sticker":{},
    "Sambutan":False,
    "userAgent": [
		"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
		"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
	],
}


wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
 
tikel = {
     'STKID': '17866',
     'STKPKGID': '1070',
     'STKVER': '2'
     } 
 
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }      
    
setTime = {}
setTime = wait2['setTime']
mulai = time.time()

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def removeAllMessages(self, lastMessageId):
        return self.Talk.client.removeAllMessages(0, lastMessageId)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def sendSticker(self,
                    stickerId = "13",
                    stickerPackageId = "1",
                    stickerVersion = "100",
                    stickerText="[null]"):
        try:
            message = Message(to=self.id, text="")
            message.contentType = ContentType.STICKER

            message.contentMetadata = {
                'STKID': stickerId,
                'STKPKGID': stickerPackageId,
                'STKVER': stickerVersion,
                'STKTXT': stickerText,
            }

            self._client.sendMessage(message)

            return True
        except Exception as e:
            raise e

def sendSticker(self, to, packageId, stickerId):
        contentMetadata = {
            'STKVER': '100',
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)

def summon(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
      cl.sendMessage(msg)
    except Exception as error:
      print error
     
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs) 
    
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi    
    
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
         
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.client.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')

        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass
    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)                                      
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u9fb3e682d923b374004d3942221fc439":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")                                                      
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))
       
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True: 
                    #msg.text.replace("@"+cl.getProfile().displayName,"")
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    #balas = ["Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]"]
                    balas = [cName + "\n Iɴɪ Pᴇɴᴀᴍᴘᴀᴋᴀɴ Mᴀᴋʜʟᴜᴋ Jᴏɴᴇs \nYᴀɴɢ sᴜᴋᴀ Nɢᴇᴛᴀɢ ɢᴡ!! ",cName + "\nHᴀʟᴏ Fᴀɴs Bᴇʀᴀᴛ Gᴡ!! \nAᴅᴀ Pᴇʀʟᴜ ᴀᴘᴀ Tᴀɢ Gᴡ..",cName + "\nɴᴀᴘᴀ ʟᴏ ᴛᴀɢ ɢᴡ! \nᴘᴇʀɢɪʜ ᴊᴀᴜʜ ᴊᴀᴜʜ sᴀɴᴀ",cName + "\nHᴀᴅɪʀʀʀʀʀ Sᴇʟᴀʟᴜ \nAᴅᴀ ʏᴀɴɢ ʙɪsᴀ sᴀʏᴀ ʙᴀɴᴛᴜ",cName + "\nJᴀᴅɪ ᴏʀᴀɴɢ cantik ᴇᴍᴀɴᴋ sᴜsᴀʜ \nsʟᴀʟᴜ ᴅɪ ᴛᴀɢ ᴅᴍɴᴀ ᴍᴀɴᴀ",cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ....!!! \nPᴇʀɢɪ sᴀɴᴀ ᴊᴀᴜʜ ᴊᴀᴜʜ \nHᴜs Hᴜs Hᴜs"]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = "[Auto Respond] \n" + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                           	   #cl.sendText(msg.to,"@"+cl.getProfile().displayName,"")
                                  #summon(op.param1, [op.param2])
                                  cl.sendText(msg.to,ret_)
                                  summon(op.param1, [op.param2])
                                  cl.sendImageWithURL(msg.to,path)
                                  #msg.contentType = 7    
                                  #msg.text = None
                                  #msg.contentMetadata = {'STKID' : '22987198'
                                 #   'STKPKGID' : '1711359'
                                 #   'STKVER' : '1'
                                 #   'STKVER' : '1'}
                                  #cl.sendMessage(msg) 
                                  msg.contentType = 7    
                                  msg.text = None
                                  msg.contentMetadata = {'STKID': '20217684',
                                    'STKPKGID': '1592292',
                                    'STKVER': '1'}
                                    #'STKVER': '1'}
                                  
                                #  cl.sendMessage(msg)                                
                                #  msg.contentType = 7    
                                #  msg.text = None
                                #  msg.contentMetadata = {'STKID': '7',
                                 #   'STKPKGID': '1',
                                  #  'STKVER': '100'}
                                  
                                  cl.sendMessage(msg)                                
                                  
                                  break                                                                      

            #------------------------------------------------------------------------------------------#
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                 if wait["tag"] == True:
                    names = re.findall(r'@(\w+)',msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            xname = cl.getContact(msg.from_).displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            balas = "@" +xname+ "\nApasih tag-tag? Penting PC aja. ","@" +xname+ "\nfans aku yaa?","@" +xname+ "\nNggak Usah Tag-Tag! \nKalo Ada Perlu PC Aja!","@" +xname+ "\n\nKenapa Tag saya?","@" +xname+ "\n\nSokap deh ngetag.  ","@" +xname+ "\n\napaan ngetag?"
                            msg.text = random.choice(balas)
                            #ret_ = "[Auto Respond] \n" + random.choice(balas)
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                            #cl.sendText(msg.to,ret_)
                            cl.sendMessage(msg)                                                           

            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     cl.like(url[25:58], url[66:], likeType=1005)
                     #ki.like(url[25:58], url[66:], likeType=1002)
                     #ki2.like(url[25:58], url[66:], likeType=1004)
                     #ki3.like(url[25:58], url[66:], likeType=1003)
                     #ki4.like(url[25:58], url[66:], likeType=1001)
                     #ki5.like(url[25:58], url[66:], likeType=1001)
                     #ki6.like(url[25:58], url[66:], likeType=1001)
                     #ki7.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     #ki.comment(url[25:58], url[66:], wait["comment2"])
                     #ki2.comment(url[25:58], url[66:], wait["comment3"])
                     #ki3.comment(url[25:58], url[66:], wait["comment4"])
                     #ki4.comment(url[25:58], url[66:], wait["comment5"])
                     #ki5.comment(url[25:58], url[66:], wait["comment6"])
                     #ki6.comment(url[25:58], url[66:], wait["comment7"])
                     #ki7.comment(url[25:58], url[66:], wait["comment8"])
                     #cl.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = True
                     
        if op.type == 25:
            msg = op.message
            if msg.contentType == 7:
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "☸ Sticker Check ☸\n\n☑ STKID : %s\n☑ STKPKGID : %s\n☑ STKVER : %s\n☸ Link:\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass            
#------------------------------------------------------------------------------------------#            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ngapain Ngetag?, ", cName + " Kenapa Tag saya?,  " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., ", "Tersummon -_-, "]
                     ret_ = "[**Auto Respond**]\n " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break  
                                                                                                             
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))

            if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki. getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in kimid:
                    if op.param2 in ki2mid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
   
                if op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)

                if op.param3 in ki5mid:
                    if op.param2 in ki6mid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        k5.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        #Ti = ki2.reissueGroupTicket(op.param1)
                                          
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,myhelpMessage)
                else:
                    cl.sendText(msg.to,myhelpMessage)
            elif "Mybot" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg) 
            elif "Pro1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["Bot4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki4.sendMessage(msg)

            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Pro1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Pro2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Pro3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Pro4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Pro5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "Pro6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
#            elif "Pro7 mid" == msg.text:
#                ki7.sendText(msg.to,ki7mid)
#            elif "Pro8 mid" == msg.text:
#                ki8.sendText(msg.to,ki8mid)
#            elif "Pro9 mid" == msg.text:
#                ki9.sendText(msg.to,ki9mid)
#            elif "Pro10 mid" == msg.text:
#                k1.sendText(msg.to,k1mid)
#            elif "Pro11 mid" == msg.text:
#                k2.sendText(msg.to,k2mid)
#            elif "Pro12 mid" == msg.text:
#                k3.sendText(msg.to,k3mid)
#            elif "Pro13 mid" == msg.text:
#                k4.sendText(msg.to,k4mid)
#            elif "Pro14 mid" == msg.text:
#                k5.sendText(msg.to,k5mid)
#            elif "Pro15 mid" == msg.text:
#                k6.sendText(msg.to,k6mid)
#            elif "Pro16 mid" == msg.text:
#                k7.sendText(msg.to,k7mid)
#            elif "Pro17 mid" == msg.text:
#                k8.sendText(msg.to,k8mid)
#            elif "Pro18 mid" == msg.text:
#                k9.sendText(msg.to,k9mid)
#            elif "Pro19 mid" == msg.text:
#                w1.sendText(msg.to,w1mid)
#            elif "Pro20 mid" == msg.text:
#                w2.sendText(msg.to,w2mid)
#            elif "Pro21 mid" == msg.text:
#                w3.sendText(msg.to,w3mid)
#            elif "Pro22 mid" == msg.text:
#                w4.sendText(msg.to,w4mid)
#            elif "Pro23 mid" == msg.text:
#                w5.sendText(msg.to,w5mid)
#            elif "Pro24 mid" == msg.text:
#                w6.sendText(msg.to,w6mid)
#            elif "Pro25 mid" == msg.text:
#                w7.sendText(msg.to,w7mid)
#            elif "Pro26 mid" == msg.text:
#                w8.sendText(msg.to,w8mid)
#            elif "Pro27 mid" == msg.text:
#                w9.sendText(msg.to,w9mid)
#            elif "Pro28 mid" == msg.text:
#                l1.sendText(msg.to,l1mid)
#            elif "Pro29 mid" == msg.text:
#                l2.sendText(msg.to,l2mid)
#            elif "Pro30 mid" == msg.text:
#                l3.sendText(msg.to,l3mid)
#            elif "Pro31 mid" == msg.text:
#                l4.sendText(msg.to,l4mid)
#            elif "Pro32 mid" == msg.text:
#                l5.sendText(msg.to,l5mid)
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                #ki7.sendText(msg.to,ki7mid)
                #ki8.sendText(msg.to,ki8mid)
                #ki9.sendText(msg.to,ki9mid)
                #k1.sendText(msg.to,k1mid)
                #k2.sendText(msg.to,k2mid)
                #k3.sendText(msg.to,k3mid)
                #k4.sendText(msg.to,k4mid)
                #k5.sendText(msg.to,k5mid)
                #k6.sendText(msg.to,k6mid)
                #k7.sendText(msg.to,k7mid)
                #k8.sendText(msg.to,k8mid)
                #k9.sendText(msg.to,k9mid)
                #w1.sendText(msg.to,w1mid)
                #w2.sendText(msg.to,w2mid)
                #w3.sendText(msg.to,w3mid)
                #w4.sendText(msg.to,w4mid)
                #w5.sendText(msg.to,w5mid)
                #w6.sendText(msg.to,w6mid)
                #w7.sendText(msg.to,w7mid)
                #w8.sendText(msg.to,w8mid)
                #w9.sendText(msg.to,w9mid)
                #l1.sendText(msg.to,l1mid)
                #l2.sendText(msg.to,l2mid)
                #l3.sendText(msg.to,l3mid)
                #l4.sendText(msg.to,l4mid)
                #l5.sendText(msg.to,l5mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Allname: " in msg.text:
                string = msg.text.replace("Allname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = ki7.getProfile()
#                    profile.displayName = string
#                    ki7.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = ki8.getProfile()
#                    profile.displayName = string
#                    ki8.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = ki9.getProfile()
#                    profile.displayName = string
#                    ki9.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k1.getProfile()
#                    profile.displayName = string
#                    k1.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k2.getProfile()
#                    profile.displayName = string
#                    k2.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k3.getProfile()
#                    profile.displayName = string
#                    k3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k4.getProfile()
#                    profile.displayName = string
#                    k4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k5.getProfile()
#                    profile.displayName = string
#                    k5.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k6.getProfile()
#                    profile.displayName = string
#                    k6.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k7.getProfile()
#                    profile.displayName = string
#                    k7.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k8.getProfile()
#                    profile.displayName = string
#                    k8.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = k9.getProfile()
#                    profile.displayName = string
#                    k9.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w1.getProfile()
#                    profile.displayName = string
#                    w1.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w2.getProfile()
#                    profile.displayName = string
#                    w2.updateProfile(profile)
#               if len(string.decode('utf-8')) <= 20:
#                    profile = w3.getProfile()
#                    profile.displayName = string
#                    w3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w4.getProfile()
#                    profile.displayName = string
#                    w4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w5.getProfile()
#                    profile.displayName = string
#                    w5.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w6.getProfile()
#                    profile.displayName = string
#                    w6.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w7.getProfile()
#                    profile.displayName = string
#                    w7.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w8.getProfile()
#                    profile.displayName = string
#                    w8.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = w9.getProfile()
#                    profile.displayName = string
#                    w9.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l1.getProfile()
#                    profile.displayName = string
#                    l1.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l2.getProfile()
#                    profile.displayName = string
#                    l2.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l3.getProfile()
#                    profile.displayName = string
#                    l3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l4.getProfile()
#                    profile.displayName = string
#                    l4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l5.getProfile()
#                    profile.displayName = string
#                    l5.updateProfile(profile)
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string            
                    ki6.updateProfile(profile)  
#--------------------------------------------------------
            elif "Out: " in msg.text:
		ng = msg.text.replace("Out: ","")
		gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
		    if h == ng:
			cl.sendText(i,"Bye "+h+"~")
		        cl.leaveGroup(i)
			cl.sendText(msg.to,"Sukses Keluar Dari Grup ["+ h +"] ~")
		    else:
			pass    
#-----------------------------------------------                    
#---------------------------------------------------------
            elif msg.text in ["Mibot"]:
                #msg.contentType = 13
                #msg.contentMetadata = {'mid': mid}
                #cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)  
#--------------------------     
#---------------------------------------------------------
            elif "1pro: " in msg.text:
                string = msg.text.replace("1pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2pro: " in msg.text:
                string = msg.text.replace("2pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3pro: " in msg.text:
                string = msg.text.replace("3pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4pro: " in msg.text:
                string = msg.text.replace("4pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5pro: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁??􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6pro: " in msg.text:
                string = msg.text.replace("6pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif msg.text.lower() == "runtime":
                eltime = time.time() - mulai
                dan = "「Waktu Keaktifan Bot」\n"+waktu(eltime)
                cl.sendText(msg.to,dan)
            elif msg.text.lower() == 'runtime1':
                eltime = time.time() - mulai
                van = "「ᴘʟᴀsᴇ ᴡᴀɪᴛᴇ....」\nsᴇʟғʙᴏᴛ ʜᴀs ʙᴇᴇɴ ᴀᴋᴛɪᴠᴇ "+waktu(eltime)
                cl.sendText(msg.to,van)                
#--------------------------------------------------------
            elif "Update sambutan:" in msg.text:
              #if msg.from_ in admin + owner + creator:
                wait["Sambutan"] = msg.text.replace("Update sambutan:","")
                cl.sendText(msg.to,"ˢᵃᵐᵇᵘᵗᵃⁿ ᴬᵏᵗᶦᵛᵉ ᶜʰᵃⁿᵍᵉᵈ"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome message"]:
              #if msg.from_ in admin + creator + owner:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"ʸᵒᵘʳ ᴮᵒᵗ ᴹᵉˢˢᵃᵍᵉ\n\n" + wait["Sambutan"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["Sambutan"])
#--------------------------------------------------------
            elif msg.text == ".Speed":
                    cl.sendText(msg.to,"「ʟᴏᴀᴅɪɴɢ....」\nᴛᴇsᴛ sᴘᴇᴇᴅ sᴇʟғʙᴏᴛ")
                    start = time.time()
                    for i in range(3000):
                        1+1
                    elsp = time.time() - start
                    cl.sendText(msg.to,"%sᴅᴇᴛɪᴋ" % (elsp))    
                
            elif 'Crash' in msg.text:
              if msg.from_ in admsa:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "mid,'"}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                #cl.sendText(msg.to,("@"+cl.getProfile().displayName,"ɪɴɪʟᴀʜ ᴀᴋᴜ ᴀᴘᴀ ᴀᴅᴀ ɴʏᴀ \nʏᴀɴɢ sᴇʀʙᴀ sᴇᴅᴇʀʜᴀɴᴀ \nᴅᴀɴ sᴇʀʙᴀ ᴋᴇᴋᴜʀᴀɴɢᴀɴ \nʙᴀʜᴋᴀɴ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ \nᴋᴇʟᴇʙɪʜᴀɴ ᴀᴘᴀᴘᴜɴ"))
                cl.sendMessage(msg)             
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendMessage(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                #cl.sendMessage(msg.to,("@"+cl.getProfile().displayName,"ɪɴɪʟᴀʜ ᴀᴋᴜ ᴀᴘᴀ ᴀᴅᴀ ɴʏᴀ \nʏᴀɴɢ sᴇʀʙᴀ sᴇᴅᴇʀʜᴀɴᴀ \nᴅᴀɴ sᴇʀʙᴀ ᴋᴇᴋᴜʀᴀɴɢᴀɴ \nʙᴀʜᴋᴀɴ ᴛɪᴅᴀᴋ ᴍᴇᴍɪʟɪᴋɪ \nᴋᴇʟᴇʙɪʜᴀɴ ᴀᴘᴀᴘᴜɴ"))
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Proses")
                    cl.sendText(msg.to, "https://www.facebook.com" + b)
                    cl.sendText(msg.to,"「 Mencari 」\n" "Type:Mencari Info\nStatus: Sukses")                
#--------------------------------------------------------
            elif "Spam change:" in msg.text:
                if msg.toType == 2:
                 wait["spam"] = msg.text.replace("Spam change:","")
                cl.sendText(msg.to,"spam changed")
#==========================[Kris]===========================
            elif "Tambah admin @" in msg.text:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Tambah admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                #else:
                #    kr.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                #    kr.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")
#==========================[Kris]===========================
            elif "Hapus admin @" in msg.text:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Hapus admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                #else:
                #    kr.sendText(msg.to,"Command DiTolak")
                #    kr.sendText(msg.to,"Admin Tidak Bisa Menggunakan")
#==========================[Kris]===========================
            elif msg.text in ["Adminlist","admlist"]:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Sabar Dikit Boss kris.....")
                    mc = ""
                    for mi_d in admin:
                        mc += "☄ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#==========================[Kris]===========================
            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                cl.sendText(msg.to,"Send Contact")
#===============Image====================#
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
#==============Image finish================#
            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    cl.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    cl.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}
#===============Image====================#
            elif msg.text in ["Mycover"]:
                h = cl.getContact(mid)
                cu = cl.channel.getCover(mid)
                path = str(cu)
                cl.sendImageWithURL(msg.to, path)
 #==============Image finish================#
            elif msg.text in ["Backup:on"]:
              if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵃᶜᵗᶦᵛᵉ"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵉⁿᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵃᶜᵗᶦᵛᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᵇᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵉⁿᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
              if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵘⁿᵃᶜᵗᶦᵛᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵈᶦˢᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵘⁿᵃᶜᵗᶦᵛᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"ᴮᵃᶜᵏᵘᵖ ʰᵃˢ ᵇᵉᵉⁿ ᵈᶦˢᵃᵇˡᵉ\n\n"+ datetime.today().strftime('%H:%M:%S'))
#-------------------------------------------------------- 
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = ki2.getGroup(msg.to)
                  gs = ki3.getGroup(msg.to)
                  gs = ki4.getGroup(msg.to)
                  gs = ki5.getGroup(msg.to)
                  gs = ki6.getGroup(msg.to)
                  #gs = ki7.getGroup(msg.to)
                  #gs = ko.getGroup(msg.to)
                  #gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        ki2.findAndAddContactsByMid(target)
                        ki3.findAndAddContactsByMid(target)
                        ki4.findAndAddContactsByMid(target)
                        ki5.findAndAddContactsByMid(target)
                        ki6.findAndAddContactsByMid(target)
                        #ki7.findAndAddContactsByMid(target)
                        #ke.findAndAddContactsByMid(target)
                        #ku.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")                       
#--------------------------------------------------------
            elif "Mayhem" in msg.text:
                if msg.toType == 2:
                    print "Cleanse is going."
                    _name = msg.text.replace("Mayhem ","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"ᴘᴇᴍʙᴇʀsɪʜᴀɴ ᴀᴋᴀɴ ᴅɪʟᴀᴋsᴀɴᴀᴋᴀɴ")
                    cl.sendText(msg.to,"sᴀʏ ɢᴏᴏᴅ ʙʏᴇ ᴛᴏ ᴍᴇ")
                    cl.sendText(msg.to,"ᴘᴇᴍʙᴇʀsɪʜᴀɴ ᴅɪʟᴀᴋsᴀɴᴀᴋᴀɴ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                                cl.sendText(msg.to,"ɢʀᴏᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴇʀsɪʜᴋᴀɴ")
                            except:
                                cl.sendText(msg,to,"Group cleanse")
                                cl.sendText(msg,to,"Group cleanse")
#-------------------------------------------------------
            elif msg.text in ["Purge"]:
              if msg.from_ in admin :
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"group purge")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl]
                            kicker = random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#--------------------------------------------------------                            
#--------------------------------------------------------
            elif "intip on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"ˢᵉᵗᵖᵒᶦⁿᵗ ᵃˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "intop off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"ˢᵉᵗ ʳᵉᵃᵈᶦⁿᵍ ᵖᵒᶦⁿᵗ ᵈᶦˢᵃᵇˡᵉ")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "ᴰᵉˡᵉᵗᵉᵈ ᴿᵉᵃᵈʸⁿᵍ ᴾᵒᶦⁿᵗ:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "intip" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "ᴸᵘʳᵏᶦⁿᵍ ᴴᵃˢ ᴺᵒᵗ ᴮᵉⁿ ˢᵉᵗ.")
#==============================================
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam") 
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(g.mid,"Spam")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

#==============================================================================#
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"Simi mode Off")
                
            #elif msg.text in ["Autoread on","Read:on"]:
                #wait['alwayRead'] = True
                #cl.sendText(msg.to,"Auto read On")
                
            #elif msg.text in ["Autoread off","Read:off"]:
                #wait['alwayRead'] = False
                #cl.sendText(msg.to,"Auto read Off")
                
            elif msg.text in ["Respontag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
                
            elif msg.text in ["Respontag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                cl.sendText(msg.to,"ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"ʀᴇsᴘᴏɴ ᴋɪᴄᴋ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"ʀᴇsᴘᴏɴ ᴋɪᴄᴋ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ")
            elif "Time" in msg.text:
              if msg.toType == 2:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif "Tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Para Jones"
                 cnt.to = msg.to
                 cl.sendMessage(cnt)
#==============================================================================#            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  cl.sendAudio(msg.to,'tts.mp3')
            
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            
            elif "ytsearch " in msg.text:
                    query = msg.text.replace("ytsearch ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        cl.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "LinkNya: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollowerNya : "+followerIG+"\nFollowingNya : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))

            elif 'instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "********************\n"
                    details = "\n********************="
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
#=============================================================================#
            elif "hola" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " ᴘᴀʀᴀ ᴍᴏɴsᴛᴇʀ ᴅᴀʀᴀᴛ ʏᴀɴɢ sᴀɴɢᴀᴛ ʙᴜᴀs"
                 cnt.to = msg.to
                 cl.sendText(msg.to,"sᴜᴋsᴇs ᴛᴏ sᴜᴍᴏɴ ᴍᴏɴsᴛᴇʀ ᴅᴇsᴛʀᴏʏᴇᴅ")
                 cl.sendMessage(cnt)                
#==============================================================================#
            elif msg.text in ["Set all on"]:
		if msg.from_ in admsa:
                    wait["protect"] = True
                    wait["cancelprotect"] = True
                    wait["inviteprotect"] = True
                    wait["linkprotect"] = True
                    wait["Backup"] = True
                    wait["Contact"] = True
                    wait["Sambutan"] = True
                    cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ")
		else:
		    cl.sendText(msg.to,"Khusus Alvian")

            elif msg.text in ["Set all off"]:
		if msg.from_ in admsa:
                    wait["protect"] = False
                    wait["cancelprotect"] = False
                    wait["inviteprotect"] = False
                    wait["linkprotect"] = False
                    wait["Backup"] = False
                    wait["Contact"] = False
                    wait["Sambutan"] = False
                    cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ")
		else:
		    cl.sendText(msg.to,"Khusus Alvian")
#==============================================================================#
            elif msg.text.lower().startswith(".cw "):
                            sep = msg.text.split(" ")
                            location = msg.text.lower().replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(wait["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "╔══[ Weather Status ]"
                                    ret_ += "\n╠ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n╠ " + data[1]+"°C"
                                    ret_ += "\n╠ " + data[2] + "%"
                                    ret_ += "\n╠ " + data[3] + " milibar"
                                    ret_ += "\n╠ " + data[4] +"km/jam"
                                    ret_ += "\n╚══[ Complete ]"
                                else:
                                    ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                                cl.sendText(msg.to, str(ret_))
#--------------------------------------
            elif ".pt " in msg.text.lower():
                            pisah = msg.text.split("t ")
                            location = msg.text.replace(pisah[0]+"t ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "╠ ⌬「 Subuh」: " and data[2] != "╠ ⌬「 Dzuhur」: " and data[3] != "╠ ⌬「 Ashar」: " and data[4] != "╠ ⌬「 Maghrib」: " and data[5] != "╠ ⌬「 Isya」: ":
                                    ret_ = "╔══『 Jadwal Sholat 』"
                                    ret_ += "\n╠ ⌬「 Lokasi 」: " + data[0]
                                    ret_ += "\n" + data[1]
                                    ret_ += "\n" + data[2]
                                    ret_ += "\n" + data[3]
                                    ret_ += "\n" + data[4]
                                    ret_ += "\n" + data[5]
                                    ret_ +=  "\n╚══『 Jadwal Sholat 』"
                                else:
                                    ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                cl.sendText(msg.to, str(ret_))
#----------------------------------------     
            elif ".lc " in msg.text.lower():
                            pisah = msg.text.split("c ")
                            location = msg.text.replace(pisah[0]+"c ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(wait["userAgent"])
                                r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "╔══『 Detail Location 』"
                                    ret_ += "\n╠ ⌬「 Lokasi」: " + data[0]
                                    ret_ += "\n╠ ⌬「 Google Maps 」: " + link
                                    ret_ += "\n╚══『 Detail Location 』"
                                else:
                                    ret_ = "[ Details Location ] Error : Location not found"
                                cl.sendText(msg.to, str(ret_))
#--------------------------------------   
            elif '.wp ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace(".wp ","")
                      wikipedia.set_lang("id")
                      pesan="「 "
                      pesan+=wikipedia.page(wiki).title
                      pesan+=" 」\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n「 "
                      pesan+=wikipedia.page(wiki).url
                      pesan+=" 」"
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Jumlah text kebanyakan~\nUntuk info lebih lanjut silahkan klik link dibawah ini.\n"
                              pesan+="「 "+wikipedia.page(wiki).url+" 」"
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))    
#--------------------------------------                    
#==============================================================================#
#----------------SEARCH SECTION----------------------------------------
	    elif ".ms " in msg.text:
					songname = msg.text.replace(".ms ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
            elif ".lr" in msg.text.lower():
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(wait["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[3]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                cl.sendText(msg.to, str(ret_))
                        except:
                            cl.sendText(to, "Lirik tidak ditemukan")
            elif ".yt " in msg.text:
                query = msg.text.replace(".yt ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#------------------------------------------------                               
#-------------------------------------------------                    
            elif "Mid: " in msg.text:
                mmid = msg.text.replace("Mid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵒⁿᵗᵃᶜᵗ ᴿᵉᵃᵈʸ ᵒⁿ")
                    else:
                        cl.sendText(msg.to,"ᶜᵒⁿᵗᵃᶜᵗ ᴿᵉᵃᵈʸ ᵒⁿ")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴬˡˡ ᴿᵉᵃᵈʸ")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᵒᶠᶠ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᵒᶠᶠ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴿᵉᵃᵈʸ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴸᶦⁿᵏ ᴾʳᵒᵗᵉᶜᵗ ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᶜᵃⁿᶜᵉˡ ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                    else:
                        cl.sendText(msg.to,"ᵃˡᵉʳᵈʸ ᵃᶜᵗᶦᵛᵉ ᵖʳᵒᵗᵉᶜᵗ")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴿᵉᵃᵈʸ ᴬᶜᵗᶦᵛᵉ")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴶᵒᶦⁿ ᵈᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᵁʳˡ ᵖʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᵉⁿʸᶦⁿᵛᶦᵗᵉ ᴬˡˡ ᴾʳᵒᵗᵉᶜᵗ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"ᴾʳᵒᵗᵉᶜᵗ ᶜᵃⁿᶜᵉˡ ᴰᶦˢᵃᵇˡᵉ")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬˡʳᵉᵃᵈʸ ᵃᶜᵗᶦᵛᵉ")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴬᵘᵗᵒ ᴸᵉᵃᵛᵉ ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
                    else:
                        cl.sendText(msg.to,"ᵃᶜᵗᶦᵛᵉ")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
            elif msg.text.lower() == 'set':                        
                md = ""
                if wait["contact"] == True: md+="Dᴀғᴛᴀʀ Sᴇᴛᴛɪɴɢ\n\n▩ ᴄᴏɴᴛᴀᴄᴛ → ᴏɴ\n"
                else: md+="Dᴀғᴛᴀʀ Sᴇᴛᴛɪɴɢ\n\n▩ ᴄᴏɴᴛᴀᴄᴛ → ᴏғғ\n"
                if wait["autoJoin"] == True: md+="▩ ᴀᴜᴛᴏ ᴊᴏɪɴ → ᴏɴ\n"
                else: md+="▩ ᴀᴜᴛᴏ ᴊᴏɪɴ → ᴏғғ\n"
                if wait["autoCancel"]["on"] == True:md+="▩ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ: " + str(wait["autoCancel"]["members"]) + " → ᴏɴ\n"
                else: md+="▩ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ → ᴏғғ\n"
                if wait["leaveRoom"] == True: md+="▩ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ → ᴏɴ\n"
                else: md+="▩ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ → ᴏғғ\n"
                if wait["timeline"] == True: md+="▩ sʜᴀʀᴇ → ᴏɴ\n"
                else:md+="▩ sʜᴀʀᴇ → ᴏғғ\n"
                if wait["autoAdd"] == True: md+="▩ ᴀᴜᴛᴏ ᴀᴅᴅ → ᴏɴ\n"
                else:md+="▩ ᴀᴜᴛᴏ ᴀᴅᴅ → ᴏғғ\n"
                if wait["commentOn"] == True: md+="▩ ᴄᴏᴍᴍᴇɴᴛ → ᴏɴ\n"
                else:md+="▩ ᴄᴏᴍᴍᴇɴᴛ → ᴏғғ\n"
                if wait["protect"] == True: md+="▩ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ → ᴏɴ\n"
                else:md+="▩ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ → ᴏғғ\n"
                if wait["linkprotect"] == True: md+="▩ ᴘʀᴏᴛᴇᴄᴛ ᴜʀʟ → ᴏɴ\n"
                else:md+="▩ ᴘʀᴏᴛᴇᴄᴛ ᴜʀʟ → ᴏғғ\n"
                if wait["inviteprotect"] == True: md+="▩ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ → ᴏɴ\n"
                else:md+="▩ ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ → ᴏғғ\n"
                if wait["cancelprotect"] == True: md+="▩ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ → ᴏɴ\n"
                else:md+="▩ ᴘʀᴏᴛᴇᴄᴛ ᴄᴀɴᴄᴇʟ → ᴏғғ\n"
                if wait["kickMention"] == True: md+="▩ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ → ᴏɴ\n"
                else:md+="▩ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ → ᴏғғ\n"
                if wait["likeOn"] == True: md+="▩ ʟɪᴋᴇ → ᴏɴ\n"
                else:md+="▩ ʟɪᴋᴇ → ᴏғғ\n"
                if wait["Backup"] == True: md+="▩ ʙᴀᴄᴋᴜᴘ → ᴏɴ\n"
                else:md+="▩ ʙᴀᴄᴋᴜᴘ → ᴏғғ\n"
                if wait["Sambutan"] == True: md+="▩ ᴡᴇʟᴄᴏᴍᴇ → ᴏɴ\n"
                else:md+="▩ ᴡᴇʟᴄᴏᴍᴇ → ᴏғғ\n"
                if wait["tag"] == True: md+="▩ ʀᴇsᴘᴏɴ ᴛᴀɢ → ᴏɴ\n"
                else:md+="▩ ʀᴇsᴘᴏɴ ᴛᴀɢ → ᴏғғ\n"
                if wait["detectMention"] == True: md+="▩ Tᴀɢ → ᴏɴ\n\nPᴏᴡᴇʀᴇᴅ ʙʏ: \n==[ DAENG TEAM BOT ]=="
                else:md+="▩ Tᴀɢ → ᴏғғ\n\nPᴏᴡᴇʀᴇᴅ ʙʏ:\n==[ DAENG TEAM BOT ]==" 
                cl.sendText(msg.to,md)
            
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text in ["いいね:オフ","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
                    else:
                        cl.sendText(msg.to,"ᴬᶜᵗᶦᵛᵉᵈ")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Additional information is automatically set to the following \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᴀᴜᴛᴏ ᴄᴏᴍᴍᴇɴᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
                    else:
                        cl.sendText(msg.to,"ᴄᴏᴍᴍᴇɴᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to," 「Lurking already on」")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "「Set Reading Sider System」\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to," 「Lurking Already off」")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "「Delete reading point」\n" + datetime.now().strftime('%H:%M:%S'))
            elif "lurkers" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass

#-----------------------[Add Staff Section]------------------------
            elif "About1" in msg.text: #ABOUT BOT#
                if msg.from_ in admin:
                   x = "「ᴀʙᴏᴜᴛ ʙᴏᴛ」\nsᴇʟғʙᴏᴛ “ʙᴏᴛ” ᴇᴅɪᴛɪᴏɴ♪\n"
                   x+="ᴛɪᴍᴇ: " + datetime.today().strftime('%H:%M:%S') + " \n\n"
                   x+="「ʙᴏᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ」\n"
                   x+="╠═════════════════════\n"
                   x+="╠ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ɪɴ: 06-01-2018\n"
                   x+="╠️ ʙᴏᴛ ᴄʀᴇᴀᴛᴏʀ: 「ᵃˡᵛᶦᵃⁿᴘᴜᴛʀᴀ」\n"
                   x+="╠️ ʙᴏᴛ Oᴡɴᴇʀ: "+cl.getProfile().displayName+"\n"
                   x+="╠️ ʙᴏᴛ ᴛʏᴘᴇ: Sᴇʟғʙᴏᴛ\n"
                   x+="╠️ ᴍʏᴛᴇᴀᴍ: sᴋɪʟᴇʀʀ ʜᴏʟʟᴏᴡ\n"
                   x+="╠️ Vᴇʀsɪᴏɴ: 1.01\n"
                   x+="╠═════════════════════\n"
                   x+= "「Cᴏɴᴛᴀᴄᴛ Pᴇʀsᴏɴᴀʟ」\n"
                   x+="「ID LINE: line://ti/p/~alvian_putra777 」\n\n"
                   x+="「ᵃˡᵛᶦᵃⁿᴘᴜᴛʀᴀ」"
                   cl.sendText(msg.to,x)
                   msg.contentType = 13
                   msg.contentMetadata = {'mid': admin}
                   cl.sendMessage(msg)
#----------------------------------------------------------- 
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name)) 
#---------------------------------------------------
            elif ("Maav!" in msg.text):
				if msg.from_ in admin:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							cl.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Error")             
#-----------------------------------------------------------
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
                        cl.sendMessage(msg,g)
#----------------------------------------------------------------
            elif "Mode on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"「ᴍᴏᴅᴇ ᴏɴ sɪᴅᴇʀ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ」")
                
            elif "Mode off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "「ᴍᴏᴅᴇ ᴏɴ sɪᴅᴇʀ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ」")
                else:
                    cl.sendText(msg.to, "「ᴍᴏᴅᴇ ᴏɴ ᴅᴜʟᴜ ᴅᴏᴅᴏʟ」")           
#-----------------------------------------------------------
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    contact = cl.getContact(i)
                    cu = cl.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                        cl.sendImageWithURL(msg.to,image)
                        cl.sendText(msg.to,"Cover " + contact.displayName)
                        cl.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = cl.getAllContactIds()
                for i in gid:
                    h = cl.getContact(i).displayName
                    gna = cl.getContact(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#-----------------------------------------------------------
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                cl.sendText(msg.to, rst) 
#-----------------------------------------------------------
            elif "tagmem" == msg.text:
		    group = cl.getGroup(msg.to)
		    mem = [contact.mid for contact in group.members]
		    for mm in mem:
		        xname = cl.getContact(mm).displayName
		        xlen = str(len(xname)+1)
		        msg.contentType = 0
		        msg.text = "@"+xname+" "
		        msg.contentMetadata = {'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		        try:
		            cl.sendMessage(msg)
		        except Exception as e:
			    print str(e)


            elif msg.text in ["Tagall","Tag all"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                      #cl.sendText(receiver, "Members :"+str(jml))
                  except Exception as error:
                      print error                        
#-----------------------------------------------------------)
            elif msg.text in ["Papay"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------------------
            elif msg.text in ["About"]:
                today = datetime.today()
                future = datetime(2020,01,31)
                days = (str(future - today))
                comma = days.find(",")
                days = days[:comma]
                cl.sendText(msg.to,"「ᴀʙᴏᴜᴛ 」\n「ᴛᴇᴀᴍ sᴋɪʟᴇʀʀ ʜᴏʟʟᴏᴡ」 \n 「ᴘᴏᴡᴇʀᴇᴅ ʙʏ : ᴀʟᴠɪᴀɴ ᴘᴜᴛʀᴀ」 \n 「sᴇʟғʙᴏᴛ ᴇᴅɪᴛɪᴏɴ」 \n\n「Subscription」\nTeam bot skiller hollow \nDont kick me from groups \nᴍᴀsᴀ ᴀᴋᴛɪғ sᴇʟғʙᴏᴛ \n Expired: " + "\n In days: " + days +  "\n\n「Contact」\n・ LINE me \n http://line.me/ti/p/~alvian_putra777")
                msg.contentType = 13
                msg.contentMetadata = {'mid':mid}
                cl.sendMessage(msg)
#-----------------------------------------------------------
#----------------------ADMIN COMMAND------------------------------#

            elif ("Fuck " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            #cl.sendText(msg.to,"Fᴜᴄᴋ Fᴏʀ Yᴏᴜ Iᴅɪᴏᴛs"
                        except:
                            cl.sendText(msg.to,"Error")
                    
            elif "Halo" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 

            elif "Kickall" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Kickall","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[cl]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")

            elif msg.text in ["List grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee i