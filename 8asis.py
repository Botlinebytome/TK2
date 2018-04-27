# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
import requests
from io import StringIO
from urllib import urlopen
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,wikipedia,tempfile

cl = LINETCR.LINE()
cl.login(token="Ep5X8ie8KSAVyrEU5mPf.AyjFsYEoCdZCVl48EB+cFW.uqNlX4y/nVCbTqVWOlHJvLuiMD9HacxVwOQdU0s8poM=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EpWvB7lSpQwk7TpY03Wf.gDw+76cr78yJcCzkbeimFW.O/bDlJJ3KivUOwrjehXjGsmTrq0Px9E5ATF1prUsb3I=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EpXvU9TaVfL2hVzKu4l7.15ivad1OBzlrkDqL9uWKTW.Zceu7ELYSXMiKNIbPK2kkg/P/6Do4zyhXRsOz7v4uhQ=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EpKQgTJ19NwnyzFnY6j4.iNFWaB4JUKOa+w+DUcp2Da.Fnc5Tr6W2qLpx5UhnHWy1KuHvPqkGKRFjpnyToIGHUA=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="Ep8KWXlIr3DGNRBDPCAf.iW1GofpnCaOR5oEc/7mT7W.xGtv/cFOd4d5qLsYobMnHglZgpNCju7hnJhhWSaS8nY=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EpyArSSgkRNCrHr49Zg6.MBHat6Ugpjr/qIzAs7yvPG.hFX5UZJi/ETHw6tVhShqVFfiPVMD3+hR22u5SvTFLRs=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EppiHyBJIcsLuoE4bds4.hwaBQvPauR+cIavFzOrDfa.VaEt+fTcDc6+a2MfmxOZPtL2eZeSxBdDIxcepaxnZu4=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="EpPgQPZZQWqinLWskd72.LwWKVgCUUwtgWaMmMoTOKG.t3hsLYya1euYNPoNJCvLZwgONxSrBm3jTpfg5CkfjCs=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EpUseS0qfZh9YGPhAXw9.0Ph8nFWeE7WudwEaIfnRUq.7MJdivGXWxZLnLhwBWWCHpruBbtG0iqtqbSQ9DRvD94=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="Epe7YCsxIX1F0aRUf4L6.ZVVD7+OIphN4iTt9hmCerG.dquW2/rXI8415/vbjVudPsQsnBtheSoOAoNx9VoduiM=")
ki9.loginResult()

print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""──────┅═ই۝ई═┅──────
╔════════════════
╠  ──━͜͜͜͜͡《🅰🅽🅳🅸》͜͡͡━──
╚════════════════
──────┅═ই۝ई═┅──────
               ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘ
──────┅═ই۝ई═┅──────
╔════════════════
╠╬ ɪᴅ
╠╬ ᴍᴇ
╠╬ ᴍɪᴅ @
╠╬ ᴍʏᴍɪᴅ
╠╬ ɢɪɴғᴏ
╠╬ ᴍᴇᴍʟɪsᴛ
╠╬ ɢʟɪsᴛ
╠╬ ɢɴ:
╠╬ ᴄᴏᴠᴇʀ @
╠╬ ᴘᴘɢʀᴜᴘ
╠╬ ᴘɪᴄᴛᴜʀʟ @
╠╬ ᴘᴘ @
╠╬ ᴍʏᴄᴏᴠᴇʀ
╠╬ ᴍʏᴘɪᴄᴛ
╠╬ ᴍʏᴄᴏᴘʏ @
╠╬ ᴍʏsᴇʟғ
╠╬ ᴀʙᴏᴜᴛ
╠╬ sᴘᴇᴇᴅ 
╠╬ ʀᴜɴᴛɪᴍᴇ
╠╬ ʀᴜɴᴛɪᴍᴇ1
╠╬ ʟᴜʀᴋ ᴏɴ/ᴏғғ
╠╬ ʟᴜʀᴋᴇʀs
╠╬ ᴄᴄᴛᴠ ᴏɴ/ᴏғғ
╠╬ sᴇᴘɪ
╠╬ ʜᴏʟʟᴀ
╠╬ ʙᴏᴛᴋᴜ
╠╬ ᴍʏʙᴏᴛ
╠╬ ɪɴᴠɪᴛᴇ
╠╬ sɪᴅᴇʀ
╠╬ ʟᴜʀᴋɪɴɢ
╠╬ ᴋᴀʟᴇɴᴅᴇʀ
╠╬ ᴄʀᴀsʜ
╠╬ ᴄᴡ [ᴛᴇxᴛ]
╠╬ ʟᴄ [ᴛᴇxᴛ]
╠╬ ᴘᴛ [ᴛᴇxᴛ]
╠╬ ɢᴏᴏɢʟᴇ [ᴛᴇxᴛ]
╠╬ ɢɪᴛ [ᴛᴇxᴛ]
╠╬ ʜᴀʏ @
╠╬ ʜᴀʟᴏ
╠╬ sᴘᴀᴍᴛᴀɢ @
╠╬ ʟɪsᴛ ғᴀᴠᴏʀɪᴛᴇ
╠╬ ɢɪғᴛ @
╠╬ ɢɪғᴛ
╠╬ ʀᴇsᴘᴏɴs
╠╬ ʀᴇsᴘᴏɴsᴇɴᴀᴍᴇ
╠╬─────┅═ই۝ई═┅─────
╠╬════════════════
╠╬  ──  ᴄᴏᴍᴍᴀɴᴅ ʜᴀᴘᴘʏ  ──
╠╬════════════════
╠╬─────┅═ই۝ई═┅─────
╠╬ sᴀʏ
╠╬ sᴀʏ-ᴊᴘ 
╠╬ sᴀʏ-ᴋᴏ
╠╬ sᴀʏ-ᴀʀ
╠╬ ᴀᴘᴀᴋᴀʜ
╠╬ ᴋᴀᴘᴀɴ
╠╬ ʟᴀɢᴜ 
╠╬ ʏᴠɪᴅᴇᴏ:
╠╬ ᴍᴜsɪᴋ
╠╬ ᴍᴜsʀɪᴋ
╠╬ ᴡɪᴋɪ 
╠╬ ᴘʀᴏғɪʟᴇɪɢ
╠╬ ғʙ
╠╬─────┅═ই۝ई═┅─────
╠╬════════════════
╠╬    ──  ᴄᴏᴍᴍᴀɴᴅ ᴀᴅᴍɪɴ  ──
╠╬════════════════
╠╬─────┅═ই۝ई═┅─────
╠╬ ʙᴀɴs:
╠╬ ʙᴀɴ @
╠╬ ᴜɴʙᴀɴs:ᴏɴ
╠╬ ᴜɴʙᴀɴ @
╠╬ ᴄᴏɴʙᴀɴ
╠╬ ʙᴀɴʟɪsᴛ
╠╬ ᴄʟᴇᴀʀ ʙᴀɴ
╠╬ ᴅᴇʟ ʙᴀɴ
╠╬ ᴋɪʟʟ
╠╬ - [ᴍᴀɴɢɢɪʟ ᴀsɪs]
╠╬ _ [ᴀsɪs ʙᴀᴘᴇʀ]
╠╬ ʙᴜɴᴜʜ @
╠╬ ᴠᴋɪᴄᴋ @
╠╬ ᴛᴇʟᴀɴ @
╠╬ !ʙᴏᴍ
╠╬ ɢᴏᴏᴅʙʏᴇ
╠╬─────┅═ই۝ई═┅─────
╠╬════════════════
╠╬  ──  Cᴏᴍᴍᴀɴᴅ Sᴇᴛᴛɪɴɢs  ──
╠╬════════════════
╠╬─────┅═ই۝ई═┅─────
╠╬ ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ/ᴏғғ
╠╬ ᴀᴜᴛᴏ ᴀᴅᴅ ᴏɴ/ᴏғғ
╠╬ ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ ᴏɴ/ᴏғғ
╠╬ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ
╠╬ sʜᴀʀᴇ ᴏɴ/ᴏғғ
╠╬ ᴄᴏᴍᴍᴇɴᴛ ᴏɴ/ᴏғғ
╠╬ ᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
╠╬ ǫʀᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
╠╬ ᴄᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
╠╬ ɪɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ
╠╬ ʀᴇsᴘᴏɴ ᴏɴ/ᴏғғ
╠╬ ʀᴇsᴘᴏɴ ᴋɪᴄᴋ ᴏɴ/ᴏғғ
╠╬ ᴡᴇʟᴄᴏᴍᴇ ᴏɴ/ᴏғғ
╠╬ ʟɪɴᴋ ᴏɴ/ᴏғғ
╠╬ ᴛᴀɢ ᴏɴ/ᴏғғ
╠╬ Lɪᴋᴇ:ᴏɴ/ᴏғғ
╠╬ sᴇᴛ ᴏɴ/ᴏғғ
╠╬─────┅═ই۝ई═┅─────
╠╬════════════════
╠╬       ──  Tʀᴀɴsʟᴀᴛᴇ  ──
╠╬════════════════
╠╬─────┅═ই۝ई═┅─────
╠╬ ᴇɴ@ɪᴅ
╠╬ ᴊᴘ@ɪᴅ
╠╬ ᴋᴏ@ɪᴅ
╠╬ ᴀʀ@ɪᴅ
╠╬ ᴛʜ@ɪᴅ
╠╬ sᴀʏ-ᴇɴ
╠╬ sᴀʏ-ᴊᴘ
╠╬ sᴀʏ-ᴋᴏ
╠╬ sᴀʏ
╚════════════════
──────┅═ই۝ई═┅──────
╔════════════════
╠  ──━͜͜͜͜͡《🅰🅽🅳🅸》͜͡͡━──
╚════════════════
──────┅═ই۝ई═┅──────

"""
helo=""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
Bots = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid]
admsa = "u69825f4b278e703cdcbcbe3c79bfc27f"
admin = "u69825f4b278e703cdcbcbe3c79bfc27f"
#Creator = "u923fca3dc907e047572ad25c24f1d29b"

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks For Add Me",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "comment1":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment2":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment3":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment4":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment5":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment6":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment7":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment8":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment9":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "comment10":"Auto Like By D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Sambutan":False,
    "detectMention":True,
    "kickMention":False,
    "tag":False,
    "sticker":{},
    "sider":{},
    "gift":{},
    "likeOn":True,
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
    'ROM':{}
    }

tikel = {
     'STKID': '17866',
     'STKPKGID': '1070',
     'STKVER': '2'
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

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki2.getProfile()
backup = ki2.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki3.getProfile()
backup = ki3.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki4.getProfile()
backup = ki4.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki5.getProfile()
backup = ki5.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki6.getProfile()
backup = ki6.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki7.getProfile()
backup = ki7.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki8.getProfile()
backup = ki8.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result    
    
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
                if msg.from_ == "u69825f4b278e703cdcbcbe3c79bfc27f":
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
                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True: 
                    #msg.text.replace("@"+cl.getProfile().displayName,"")
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    #balas = ["Kenapa Tag Si "+cl.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]","Nah ngetag lagi si "+cl.getProfile().displayName+" mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]"]
                    balas = [cName + "",cName + "",cName + "",cName + "",cName + "",cName + ""]
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
                                  msg.contentMetadata = {'STKID': '24638748',
                                    'STKPKGID': '1780124',
                                    'STKVER': '1'}
                                    #'STKVER': '1'}
                                  
                                #  cl.sendMessage(msg)                                
                                #  msg.contentType = 7    
                                #  msg.text = None
                                #  msg.contentMetadata = {'STKID': '7',
                                 #   'STKPKGID': '1',
                                  #  'STKVER': '100'}
                                  
                                  cl.sendMessage(msg)
                                  summon(op.param1, [op.param2])
                                  
                                  break                                    

            if msg.text in ["Crash","crash"]:
              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash!","Kamu asu ngecrash terus!","crash cresh crash cresh, bikin hp orang lag anjing!")
              ngkol = random.choice(dia)
              cl.sendText(msg.to,ngkol)
              cl.kickoutFromGroup(msg.to,[msg.from_])
              cl.sendText(msg.to,"Mampus!")
            if msg.text in ["!kickall",".kickall","Nuke","Cleanse","Ratakan","Mayhem","MB Mayhem","Kickall","kickall","!salken","Bom","."]:
                Peringatan = ("Manual kek jangan pake bot.","Cupu lu! Ratain pake bot!","Lain kali liat liat dulu~","ＴＥＲＣＹＤＵＣＫ")
                Vonis = random.choice(Peringatan)
                cl.sendText(msg.to, Vonis)
                cl.kickoutFromGroup(msg.to, [msg.from_])
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
                     ki.like(url[25:58], url[66:], likeType=1002)
                     ki2.like(url[25:58], url[66:], likeType=1004)
                     ki3.like(url[25:58], url[66:], likeType=1003)
                     ki4.like(url[25:58], url[66:], likeType=1001)
                     ki5.like(url[25:58], url[66:], likeType=1001)
                     ki6.like(url[25:58], url[66:], likeType=1001)
                     ki7.like(url[25:58], url[66:], likeType=1001)
                     ki8.like(url[25:58], url[66:], likeType=1001)
                     ki9.like(url[25:58], url[66:], likeType=1001)
                     #k10.like(url[25:58], url[66:], likeType=1001)
                     cl.comment(url[25:58], url[66:], wait["comment1"])
                     ki.comment(url[25:58], url[66:], wait["comment2"])
                     ki2.comment(url[25:58], url[66:], wait["comment3"])
                     ki3.comment(url[25:58], url[66:], wait["comment4"])
                     ki4.comment(url[25:58], url[66:], wait["comment5"])
                     ki5.comment(url[25:58], url[66:], wait["comment6"])
                     ki6.comment(url[25:58], url[66:], wait["comment7"])
                     ki7.comment(url[25:58], url[66:], wait["comment8"])
                     ki8.comment(url[25:58], url[66:], wait["comment9"])
                     ki9.comment(url[25:58], url[66:], wait["comment10"])
                     #k10.comment(url[25:58], url[66:], wait["comment11"])
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
                     ret_ = "[Auto Respond]\n " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break                
#--------------------------------------------------------
               
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
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
            elif msg.text.lower() == 'Myhelp':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Botku" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                #msg.contentMetadata = {'mid': k10mid}
                #cl.sendMessage(msg)
                #msg.contentType = 13
            elif "Bot1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Bot2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)

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

            elif msg.text in ["B Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites")
                        else:
                            cl.sendText(msg.to,"Invite people inside not")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL sudah di buka")
                    else:
                        cl.sendText(msg.to,"URL sudah di buka")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL di block")
                    else:
                        cl.sendText(msg.to,"URL sudah di block")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  ")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Pb1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Pb2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Pb3 mid" == msg.text:
                ki3.sendText(msg.to,kimid)
            elif "Pb4 mid" == msg.text:
                ki4.sendText(msg.to,ki2mid)
            elif "Pb5 mid" == msg.text:
                ki5.sendText(msg.to,kimid)
            elif "Pb6 mid" == msg.text:
                ki6.sendText(msg.to,ki2mid)
            elif "all mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki5mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")

#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["aduh","Sepi"]:
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
                  except Exception as error:
                      print error
#-------------Fungsi Tag All Finish---------------#

#---------------------------------------------------------
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔��Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#---------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah di aktifkan")
                    else:
                        cl.sendText(msg.to,"Contact di aktifkan")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact off")
                    else:
                        cl.sendText(msg.to,"contact off ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect on")
                    else:
                        cl.sendText(msg.to,"set to on protect")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set to on")
                    else:
                        cl.sendText(msg.to,"Protect set to on")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Url di aktifkan")
                    else:
                        cl.sendText(msg.to,"Sudah di aktifkan")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah di aktifkan")
                    else:
                        cl.sendText(msg.to,"Sudah di aktifkan")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah di aktifkan")
                    else:
                        cl.sendText(msg.to,"Deny invite set to on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Deny invite set to on")
                    else:
                        cl.sendText(msg.to,"Deny invite set to on")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"set to on")
                    else:
                        cl.sendText(msg.to,"Cancel invite set to on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"set to on")
                    else:
                        cl.sendText(msg.to,"Cancel invite set to on")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join set to on")
                    else:
                        cl.sendText(msg.to,"Auto join set to on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join set to on")
                    else:
                        cl.sendText(msg.to,"Auto join set to on")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Allprotect on","Mode on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")      
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Allprotect off","Mode Off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")      
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Off")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Set To off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"set to off")
                    else:
                        cl.sendText(msg.to,"Auto join set to off")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect set to off")
                    else:
                        cl.sendText(msg.to,"Protect off ")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect off")
                    else:
                        cl.sendText(msg.to,"Protect set to off")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"set to off")
                    else:
                        cl.sendText(msg.to,"Deny url set to off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"set to off")
                    else:
                        cl.sendText(msg.to,"Deny url set to off")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Deny invite set to off")
                    else:
                        cl.sendText(msg.to,"Set to off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Deny invite set to off")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Protect cancel set to off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Protect cancell set to off")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
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
                        cl.sendText(msg.to,"===Alvian==Putra===")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Auto leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to on")
                    else:
                        cl.sendText(msg.to,"Set to on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Auto leave set to on")
            elif msg.text in ["Auto leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Set to off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Auto leave set to off")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Share set to on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to on")
                    else:
                        cl.sendText(msg.to,"Set to on")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Share set to off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Set to off")
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
                if wait["Sambutan"] == True: md+="▩ ᴡᴇʟᴄᴏᴍᴇ → ᴏɴ\n"
                else:md+="▩ ᴡᴇʟᴄᴏᴍᴇ → ᴏғғ\n"
                if wait["tag"] == True: md+="▩ ʀᴇsᴘᴏɴ ᴛᴀɢ → ᴏɴ\n"
                else:md+="▩ ʀᴇsᴘᴏɴ ᴛᴀɢ → ᴏғғ\n"
                if wait["detectMention"] == True: md+="▩ Tᴀɢ → ᴏɴ\n\nPᴏᴡᴇʀᴇᴅ ʙʏ: \n҉̶̶̘̟̼̉̈́͐͋͌̊D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊ "
                else:md+="▩ Tᴀɢ → ᴏғғ\n\nPᴏᴡᴇʀᴇᴅ ʙʏ:\n҉̶̶̘̟̼̉̈́͐͋͌̊D҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊Δ̶҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊N҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊G҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊ྈT҉̶̶̘̟̼̉̈́͐͋͌̊҉̘̉̈́͐͋͌̊҉̶̘̟̼̉̈́͐͋͌̊҉̘̟̉̈́͐͋͌̊E҉̶̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊A҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊҉̶̶̶̘̟̼̉̈́͐͋͌̊҉ͩ͂҉̘̟̼̉̈́͐͋͌̊҉̶̶̘̟̼̉̈́͐͋͌̊M҉̶̘̟̼̉̈́͐͋͌̊҉ͩ͂ྈB҉̶̶̘̟̼̉̈́͐͋͌̊Ω҉̶̘̟̼̉̈́͐͋͌̊T҉̶̘̟̼̉̈́͐͋͌̊S҉̶̘̟̼̉̈́͐͋͌̊ " 
                cl.sendText(msg.to,md)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto like set to on")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto like set to on")
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto like set to off")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto like set to off")                
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"My creator")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Siapa Hayo Yang Mau Ditikung")
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"Done")	
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album👈")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Bot out"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki7.leaveGroup(i)                    
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
            elif msg.text in ["Auto add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Set to on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to on")
                    else:
                        cl.sendText(msg.to,"Auto add set to on")
            elif msg.text in ["Auto add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Auto add set to off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Auto add set to off")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"Sudah di ubah")
            elif "Help set:" in msg.text:
                wait["help"] = msg.text.replace("Help set:","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add-" in msg.text:
                wait["message"] = msg.text.replace("Pesan add-","")
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
                    cl.sendText(msg.to,"I changed the language to engglis")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia")
            elif "Message set" in msg.text:
                c = msg.text.replace("Message set","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed\n\n" + c)
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Commnet set to on")
                    else:
                        cl.sendText(msg.to,"Set to on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto comment set to on")
                    else:
                        cl.sendText(msg.to,"Set to on")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"Set to off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                    else:
                        cl.sendText(msg.to,"Comment set to off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut: \n\n" + str(wait["comment"]))
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "V1 gurl" in msg.text:
                if msg.toType == 1:
                    gid = msg.text.replace("gurl","")
                    gurl = ki.reissueGroupTicket(tid)
                    ki.sendText(msg.to,"line://ti/p" + turl)
                else:
                    ki.sendText(msg.to,"error")

            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
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
                    cl.sendText(msg.to,"Jam on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
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

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.1)
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
                                    k10.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    k10.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)

            elif msg.text == "Sider":
                    cl.sendText(msg.to, "Ada Sider Ya Boss")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text == "Lurking":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Di Read Oleh||%s\n||By : Alvian Putra||\n\n>Pelaku CCTV<\n%s-=CCTV=-\n•Tukang Ngintip\n•Tukang Nyimak\n•Jomblo Ngenes\n•Jomblo Anuan\n\nHahahahahahahah\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")						

#-----------------------[Add Staff Section]------------------------
            elif "Admin add @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = ki2.getGroup(msg.to)
                gs = ki3.getGroup(msg.to)
                gs = ki4.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = ki2.getGroup(msg.to)
                gs = ki3.getGroup(msg.to)
                gs = ki4.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Perintah Ditolak.")
                cl.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin Selfbot Alvian||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"								
#-----------------------------------------------------------
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
#----------------------------------------------------------
            elif 'Crash' in msg.text:
              if msg.from_ in admsa:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "mid,'"}
                cl.sendMessage(msg) 
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
#----------------------------------------------------------
            elif msg.text in ["Mypict"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)                
#----------------------------------------------------------
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
#-----------------------------------------------------
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
#---------------------------------------------------
            elif ("Bunuh " in msg.text):
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
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Fuck " in msg.text:                  
                       nk0 = msg.text.replace("Fuck ","")
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
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")

#----------------------------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#---------------------------------------
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
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki9.sendText(g.mid,"Your Account Has Been Spammed !")  
                       k10.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "Hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki6.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki7.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki8.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki9.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       k10.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------)
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Bosque")
                   except:
                      pass
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
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
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")
#-----------------------------------------------------------
            elif "Wiki " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wiki ","")
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
#---------------------------------------------
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
            elif msg.text in ["Set on"]:
		if msg.from_ in admsa:
                    wait["protect"] = True
                    wait["cancelprotect"] = True
                    wait["inviteprotect"] = True
                    wait["linkprotect"] = True
                    #wait["Backup"] = True
                    wait["Contact"] = True
                    wait["Sambutan"] = True
                    cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ")
		else:
		    cl.sendText(msg.to,"Khusus Alvian")

            elif msg.text in ["Set off"]:
		if msg.from_ in admsa:
                    wait["protect"] = False
                    wait["cancelprotect"] = False
                    wait["inviteprotect"] = False
                    wait["linkprotect"] = False
                    #wait["Backup"] = False
                    wait["Contact"] = False
                    wait["Sambutan"] = False
                    cl.sendText(msg.to,"ʙᴇʀʜᴀsɪʟ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴍᴜᴀ ᴘʀᴏᴛᴇᴄᴛ")
		else:
		    cl.sendText(msg.to,"Khusus Alvian")
#---------------------------------------------------
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
#-------------------------------------------------
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
                                    

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki3.updateDisplayPicture(backup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki4.updateDisplayPicture(backup.pictureStatus)
                    ki4.updateProfile(backup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------<------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Sp","sp"]:
					start = time.time()
					cl.sendText(msg.to, "「 Speed Bot 」 \n◈ Type: Test Speed \n◈ Status: Progress....")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "「 Speed Bot 」\n◈ Type: Test Speed \n◈ Time Taken:  %s/Detik" % (elapsed_time))
					
            elif msg.text in ["Speed","speed"]:
					start = time.time()
					cl.sendText(msg.to, "「 Speed Bot 」 \n◈ Type: Test Speed \n◈ Status: Progress....")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "「 Speed Bot 」\n◈ Type: Test Speed \n◈ Time Taken:  %s/Detik" % (elapsed_time))
#            elif "Speed" in msg.text:
#                start = time.time()
#                cl.sendText(msg.to, "「 Speed Bot 」 \n◈ Type: Test Speed \n◈ Status: Progress....")
#                elapsed_time = time.time() - start
#                cl.sendText(msg.to, "「 Speed Bot 」 \n◈ Status: Done... \n◈ Time : 「%sDetik 」" % (elapsed_time))
#------------------------------------
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
#-------------------------------------------
            elif "Myself" in msg.text: #ABOUT BOT#
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
#-------------------------------------------
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
#----------------------------------------------------------------
            elif "Cctv on" in msg.text:
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
                
            elif "Cctv off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "「ᴍᴏᴅᴇ ᴏɴ sɪᴅᴇʀ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ」")
                else:
                    cl.sendText(msg.to, "「ᴍᴏᴅᴇ ᴏɴ ᴅᴜʟᴜ ᴅᴏᴅᴏʟ」")                
#-----------------------------------------------------------
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = profile.displayName + "\nReady protect groups"
                ki8.sendText(msg.to, text)
                #profile = ki9.getProfile()
                #text = profile.displayName + "\nReady protect groups"
                #ki9.sendText(msg.to, text)
                #profile = k10.getProfile()
                #text = profile.displayName + "\nReady protect groups"
                #k10.sendText(msg.to, text)
                #profile = ki5.getProfile()
                #text = profile.displayName + "\nReady protect groups"
                #ki5.sendText(msg.to, text)
#==============================================================================#
            elif ".music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
 
            elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "ˢᵉˡᵃᵐᵃᵗ ᴹᵉⁿᵈᵉⁿᵍᵃʳᵏᵃⁿ ᴸᵃᵍᵘ ᴾᶦˡᶦʰᵃⁿ ᴬⁿᵈᵃ " + song[0]) 
 
            elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						cl.sendText(msg.to, "ˢᵉˡᵃᵐᵃᵗ ᴹᵉⁿᵈᵉⁿᵍᵃʳᵏᵃⁿ ᴸᵃᵍᵘ ᴾᶦˡᶦʰᵃⁿ ᴬⁿᵈᵃ " + song[0])
#==============================================================================#
            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)
#----------------------------------------------------------
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Bʟᴀᴄᴋʟɪsᴛ ᴇᴍᴘᴛʏ")
                else:
                    cl.sendText(msg.to,"Lɪsᴛ ᴄᴏɴᴛᴀᴄᴛ ʙʟᴀᴄᴋʟɪsᴛ")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)         
#------------------------------
            elif msg.text in ["List favorite"]:
                dj = cl.getFavoriteMids()
                kontak = cl.getContacts(dj)
                num = 1
                family = str(len(dj))
                msgs = "[List Favorite Friends]"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs)
#-------------------------------
            elif "Gift " in msg.text:
                strnum = msg.text.replace("Gift ","")
                num = int(strnum)
                for var in range(0,num):
                	try:
                    	   msg.contentType = 9
                           msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                 'PRDTYPE': 'THEME',
                                 'MSGTPL': '10'}
                           msg.text = None
                           cl.sendMessage(msg)
                           print "SEND STICKER"
                        except:
                 	   pass
#-----------------------------------------------------------
            elif "Detail" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass 
#-----------------------------------------------------------
            elif 'Yvideo: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")                 
#-------------------------------------------
            elif "Ginfo" in msg.text:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    ret_ = "╔════════Grup Info═════════"
                    ret_ += "\n╠Nama Grup : {}".format(group.name)
                    ret_ += "\n╠ID Grup : {}".format(group.id)
                    ret_ += "\n╠Pembuat Grup : {}".format(gCreator)
                    ret_ += "\n╠Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠Grup QR : {}".format(gQr)
                    ret_ += "\n╠Grup URL : {}".format(gTicket)
                    ret_ += "\n╚════════Grup Info═════════"
                    cl.sendText(msg.to, str(ret_))
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
#---------------------------------------------                    
            elif "Pictgroup" in msg.text:
                group = cl.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                cl.sendImageWithURL(msg.to, path)
#-----------------------------------------------------------
            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !") 
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki6.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki7.sendText(g.mid,"Your Account Has Been Spammed !")
                       cl.sendText(msg.to, "Target sudah di spam ")
                       print " Spammed !"
#-----------------------------------------------------------
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                    else:
                        pass

            elif "Getname @" in msg.text:
                _name = msg.text.replace("Getname @","")
                _nametarget = _name.rstrip(" ")
                gs = cl.getGroup(msg.to)
                for h in gs.members:
                  if _nametarget == h.displayName:
                      cl.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                  else:
                    pass                        
#-------------------------------------------------------------------
            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.") 
#==============================================================================#
            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                cl.sendText(msg.to,"Upload image failed.")

            elif msg.text.lower() in ["pap owner","pap creator"]:
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/0hNPsZGNvyEX9OIz0w4GxuKHJmHxI5DRc3NkJaETwkRklqGwQoJkNbTGklHRo2G1B7cxFXH2NxSU03")
#-----------------------------------------------  
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                cl.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                cl.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                cl.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                cl.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                cl.sendText(msg.to,str(trans))
            elif "Tr-my " in msg.text:
                nk0 = msg.text.replace("Tr-my ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'my')
                cl.sendText(msg.to,str(trans))
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'af')
                cl.sendText(msg.to,str(trans))
            elif "Tr-sq " in msg.text:
                nk0 = msg.text.replace("Tr-sq ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'sq')
                cl.sendText(msg.to,str(trans))
            elif "Tr-am " in msg.text:
                nk0 = msg.text.replace("Tr-am ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'am')
                cl.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                cl.sendText(msg.to,str(trans))
            elif "Tr-hy " in msg.text:
                nk0 = msg.text.replace("Tr-hy ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hy')
                cl.sendText(msg.to,str(trans))
#-----------------------------------------------
            elif "Ghost out" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass                                          
#----------------------------------------------- 
            elif "Ghost in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)                                               
#-----------------------------------------------
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
#---------------------------------------------------                
            elif msg.text.lower().startswith("imagetext "):
                sep = msg.text.split(" ")
                textnya = msg.text.replace(sep[0] + " ","")
                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                cl.sendImageWithURL(msg.to, urlnya)
            elif ".ps " in msg.text.lower():
                tob = msg.text.lower().replace(".ps ","")
                dan = urllib.quote(tob)
                cl.sendText(msg.to,"「 Searching 」\n" "Type: Play Store Search\nStatus: Processing...")
                cl.sendText(msg.to,"Title : "+tob+"\nhttps://play.google.com/store/search?q=" + dan)
                cl.sendText(msg.to,"「 Searching 」\n" "Type: Play Store Search\nStatus: Success")
            elif ".gl " in msg.text:
                    a = msg.text.replace(".gl ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Google Search\nStatus: Processing...")
                    cl.sendText(msg.to,"Title: " + a + "\nhttps://google.co.id/search?dcr=0&source=hp&ei=iysxWvH4JcbwvgSa5IqYDg&q=" + b + "&oq=" + b + "&gs_l=mobile-gws-hp.3..0i203k1l3j0j0i203k1.2672.5074.0.5502.18.11.2.5.6.0.190.1542.0j10.10.0....0...1c.1j4.64.mobile-gws-hp..3.15.1347.3..35i39k1j0i131k1j0i10i203k1j0i10k1.140.cERNZUVYbV8#scso=uid_WjEr7gABqeYKj7vFEw8Fug_7:228")
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Google Search\nStatus: Success")
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    replace = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Facebook Search\nStatus: Processing...")
                    cl.sendText(msg.to, "Title: " + a + "\nhttps://m.facebook.com/search/top/?q="+replace+"&ref=content_filter&tsid=0.7682944806717842&source=typeahead")
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Search Info\nStatus: Success")
            elif ".git " in msg.text:
                    a = msg.text.replace(".git ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                    cl.sendText(msg.to, "Title: " + a + "\nhttps://github.com/search?utf8=✓&q="+b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Success")
            elif ".gi" in msg.text.lower():
                    start = time.time()
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    url = 'https://www.google.com/search?q=' + search.replace(" ","+") +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    cl.sendImageWithURL(msg.to,path)
                    a = items.index(path)
                    b = len(items)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to,"Gambar #%s dari #%s gambar.\nMendapatkan gambar selama %s detik." %(str(a), str(b), elapsed_time))    
                            
            elif "say " in msg.text.lower():
                say = msg.text.lower().replace("say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#--------------------------------------
            elif "/botadd @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  print "[Command]Add executing"
                  _name = msg.text.replace("/botadd @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = ki2.getGroup(msg.to)
                  gs = ki3.getGroup(msg.to)
                  gs = ki4.getGroup(msg.to)
                  gs = ki5.getGroup(msg.to)
                  gs = ki6.getGroup(msg.to)
                  gs = ki7.getGroup(msg.to)
                  gs = ki8.getGroup(msg.to)
                  gs = ki9.getGroup(msg.to)
                  #gs = k10.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        ki2.findAndAddContactsByMid(target)
                        ki3.findAndAddContactsByMid(target)
                        ki4.findAndAddContactsByMid(target)
                        ki5.findAndAddContactsByMid(target)
                        cl.senText(msg.to, "Berhasil Menambah Kan Teman")
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hanya Untuk Admin")             
#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Clear ban"]:
                cl.sendText(msg.to,"ʙʟᴀᴄᴋʟɪsᴛ ʜᴀs ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ "+ str(len(wait["blacklist"]))+ " ᴜsᴇʀs")
                wait["blacklist"] = {}
                cl.sendText(msg.to,"sᴜᴋsᴇs ʜᴀᴘᴜs ʙᴀɴᴇᴅ")                
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"ɴᴏᴛʜɪɴɢ ʙʟᴀᴄᴋʟɪsᴛ")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "• " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"「 ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ 」\n" + mc +"\nᴛᴏᴛᴀʟ : "+ str(len(wait["blacklist"])))
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Goodbye" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Goodbye","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    #gs = ki9.getGroup(msg.to)                    
                    ki.sendText(msg.to,"Datang Tanpa Permisi  ")
                    ki2.sendText(msg.to,"Membawa Bencana")
                    ki3.sendText(msg.to,"Tangkis GW Bacok ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        ki2.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"Rata Sayang")
                                cl.sendText(msg,to,"Gc Gak Jelas")
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
    
            elif msg.text in ["Mangat","B"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			

#-----------------------------------------------
            elif "!Bom" in msg.text:
                 if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("!Bom","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    #gs = ki9.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"Kami Dataaaang ")
                    random.choice(KAC).sendText(msg.to,"Membawa Bencana Untuk GC loe")
                    random.choice(KAC).sendText(msg.to,"Jangan Baper HaHaHaHaHaHa")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target in Bots:
                            pass
                          elif target in admin:
                            pass
                          else:
                            try:
                              klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8]
                              kicker=random.choice(klist)
                              kicker.kickoutFromGroup(msg.to,[target])
                              print (msg.to,[g.mid])
                            except:
                              random.choice(KAC).kickoutFromGroup(msg.to,[target])
                              random.choice(KAC).sendText(msg.to,"Koq Ga Ditangkis Njiiing?\nLemah Banget Nih Room")
#-----------------------------------------------
            elif msg.text.lower() == ["Rejoice"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        #ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["Cuss","-"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)                        
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)                        
                        time.sleep(0.2)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        #ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

            elif msg.text.lower() == 'Sp come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
#-----------------------------------------------
            elif "Kb1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Kb2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Kb3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Kb4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Kb5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Kb6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["_","bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki3.leaveGroup(msg.to)
                        ki4.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki4.leaveGroup(msg.to)
                        ki5.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki5.leaveGroup(msg.to)
                        ki6.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki6.leaveGroup(msg.to)
                        ki7.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki7.leaveGroup(msg.to)
                        ki8.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki8.leaveGroup(msg.to)
                        #ki9.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        #ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pb1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pb2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Pb3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Kb4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Kb5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Kb6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Del ban","Delban","Clear ban","Clearban","Clear"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Banlist Hasbeen Deleted...\n\n"+datetime.today().strftime('%H:%M:%S'))                        
#-----------------------------------------------
            elif msg.text in ["Key","Myhelp","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
#-----------------------------------------------
            elif ("Telan " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")
#-----------------------------------------------
#----------------------------------------------- 
            elif msg.text.lower() == 'responsename':
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + ""
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile() 
                text = profile.displayName + ""
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + ""               
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName + ""
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = profile.displayName + ""
                ki8.sendText(msg.to, text)
                #profile = ki9.getProfile() 
                #text = profile.displayName + ""
                #ki9.sendText(msg.to, text)              
#-----------------------------------------------
            elif msg.text.lower() == 'Mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                #msg.contentMetadata = {'mid': ki9mid}
                #cl.sendMessage(msg)
                #msg.contentType = 13
                
#-----------------------------------------------
            elif msg.text.lower() == 'reboot':
                    print "[Command]Restart"
                    try:
                        cl.sendText(msg.to,"ʀᴇsᴛᴀʀᴛɪɴɢ...")
                        cl.sendText(msg.to,"ʀᴇsᴛᴀʀᴛɪɴɢ ᴍʏ sᴇʟғʙᴏᴛ sᴜᴋsᴇs")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
                        restart_program()
                        pass
#----------------------------------------------- 
#-----------------------------------------------
            elif msg.text in ["Sticker on"]:
                if wait["sticker"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                else:
                    wait["sticker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ɪɴ ᴀᴄᴛɪᴠᴇ")

            elif msg.text in ["Sticker off"]:
                if wait["sticker"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                else:
                    wait["sticker"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Uɴᴀᴄᴛɪᴠᴇ")
#-----------------------------------------------
            elif msg.text in ["Welcome on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Aʟʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ʀᴇᴀᴅʏ ɪɴ ᴀᴄᴛɪᴠᴇ")

            elif msg.text in ["Welcome off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sᴀᴍʙᴜᴛᴀɴ Wᴇʟᴄᴏᴍᴇ Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Rᴇᴀᴅʏ Uɴᴀᴄᴛɪᴠᴇ")
#-----------------------------------------------
            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to on")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to on")

            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set to off")                
#-----------------------------------------------
            elif "Bye " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Bye ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
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
                        ki9.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        ki9.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
#-----------------------------------------------
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                cl.sendAudio(msg.to,'tts.mp3')
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki2.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki3.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki4.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki5.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki6.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki8.sendText(msg.to,"Ping 􀜁􀇔􏿿")
                ki9.sendText(msg.to,"Ping 􀜁􀇔􏿿")
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        
                        
                elif op.param3 in ki8mid:
                    if op.param2 in ki9mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)                        
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in admin and Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki9.acceptGroupInvitationByTicket(op.param1, Ticket)
                    time.sleep(0.01)
                    ki9.kickoutFromGroup(op.param1,[op.param2])
                    ki9.leaveGroup(op.param1)
                    ki.updateGroup(G)
                    x = Message(to=op.param1, from_=None, text=None, contentType=13)
                    x.contentMetadata={'mid':op.param2}
                    cl.sendMessage(x)
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
#------------------------------------------------------------------------------------
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\n╔═════════════\n║Hᴀɪ Sᴀʏ Wᴇʟᴄᴏᴍᴇ ᴛᴏ   " + str(ginfo.name) + "\n╠═════════════\n" + "║Fᴏᴜɴᴅᴇʀ ɢʀᴏᴜᴘ =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Sᴇᴍᴏɢᴀ Bᴇᴛᴀʜ ʏᴀ 😘 \n╚═════════════")
            cl.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            #cl.sendText(op.param1,"Hᴜsss Hᴜssss Sᴀɴᴀᴀ Pᴇʀɢɪ " \n + cl.getContact(op.param2).displayName +  "\n╔═════════════\n║Jᴀɴɢᴀɴ Kᴇᴍʙᴀʟɪ ʟᴀɢɪ Yᴀ \n║Gᴋ ᴘᴀɴᴛᴀs Lᴏ ᴀᴅᴀ ᴅɪ sɪɴɪ..!! \n╚═════════════")
            cl.sendText(op.param1,"Hᴜsss Hᴜssss Sᴀɴᴀᴀ Pᴇʀɢɪ " + cl.getContact(op.param2).displayName +  "\n╔═════════════\n Jᴀɴɢᴀɴ Kᴇᴍʙᴀʟɪ ʟᴀɢɪ Yᴀ :v \n║Gᴋ ᴘᴀɴᴛᴀs Lᴏ ᴀᴅᴀ ᴅɪ sɪɴɪ..!! \n╚═════════════")
            print "MEMBER HAS LEFT THE GROUP"
            
                #--------------NOTIFIED_INVITE_INTO_GROUP----------------        
#--------------------------------------------------
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:                	
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Name = cl.getContact(op.param2).displayName
                            Name = cl.getContact(op.param2).displayName
                            Name = cl.getContact(op.param2).displayName
                            Name = cl.getContact(op.param2).displayName
                            Np = cl.getContact(op.param2).pictureStatus
                            Np = cl.getContact(op.param2).pictureStatus
                            Np = cl.getContact(op.param2).pictureStatus
                            Np = cl.getContact(op.param2).pictureStatus
                            Np = cl.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:                                   	
                                        cl.sendText(op.param1, "ʜᴀʟᴏ " + "☞ " + nick[0] + " ☜" + "\nɴɢᴀᴘᴀɪɴ ʟᴏ ᴄᴄᴛᴠ ᴅᴏᴀɴᴋ \nᴄᴄᴛᴠ  ʙᴀʏᴀʀ sɪɴɪ 😉")
                                        cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        summon(op.param1, [op.param2])
                                    else:
                                        cl.sendText(op.param1, "ɴᴀʜ ᴋᴀɴ " + "☞ " + nick[1] + " ☜" + "\nᴋᴇᴛᴀᴜᴡᴀɴ ɴɢɪɴᴛɪᴘ 😏. . .\nMᴀsᴜᴋ sɪɴɪ ɢᴀʙᴜɴɢ ᴄʜᴀᴛ 😆😂😛")
                                        cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        summon(op.param1, [op.param2])
                                else:
                                    cl.sendText(op.param1, "ᴡᴏɪ..!! " + "☞ " + Name + " ☜" + "\nʙᴇᴛᴀʜ ᴀᴍᴀᴛ ᴊᴀᴅɪ sɪᴅᴇʀ \nʙɪɴᴛɪᴛᴀɴ ᴀᴡᴀs ʟᴏʜ 😝")
                                    cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    summon(op.param1, [op.param2])
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
#-------------------------------------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)