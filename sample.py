# EDIT : KATOK_SUWEK
# ID : MY_KATOK
from function import *
import ast, time, json, codecs, re, subprocess
#=========================================================
login = codecs.open("token.json","r","utf-8")
Login = json.load(login)
appNya0="ANDROIDLITE\t2.17.0\tAndroid OS\t7.1.2"
appNya1="ANDROIDLITE\t2.17.0\tAndroid OS\t6.0.1"
appNya2="ANDROIDLITE\t2.17.0\tAndroid OS\t8.0.0"
appNya3="ANDROIDLITE\t2.17.0\tAndroid OS\t9.0"
appNya4="ANDROIDLITE\t2.17.0\tAndroid OS\t10"
appNya5="ANDROIDLITE\t2.17.0\tAndroid OS\t11"
appNya6="ANDROIDLITE\t2.16.0\tAndroid OS\t11"
#=========================================================
cl = Suwek(myToken=str(Login["CL"]), myApp=appNya0)
aa = Suwek(myToken=str(Login["AA"]), myApp=appNya1)
bb = Suwek(myToken=str(Login["BB"]), myApp=appNya2)
cc = Suwek(myToken=str(Login["CC"]), myApp=appNya3)
dd = Suwek(myToken=str(Login["DD"]), myApp=appNya4)
ee = Suwek(myToken=str(Login["EE"]), myApp=appNya5)
ff = Suwek(myToken=str(Login["FF"]), myApp=appNya6)
mid = cl.getProfile().mid;Amid = aa.getProfile().mid;Bmid = bb.getProfile().mid;Cmid = cc.getProfile().mid;Dmid = dd.getProfile().mid;Emid = ee.getProfile().mid;Fmid = ff.getProfile().mid
tiktik = codecs.open("warkia.json","r","utf-8")
katok = json.load(tiktik)
def backup():
    try:
        backup = katok
        f = codecs.open('warkia.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(error)
        return False
katok['list']['bot'] = [];katok['list']['bot'].remove(mid);katok['list']['bot'].remove(Amid);katok['list']['bot'].remove(Bmid);katok['list']['bot'].remove(Cmid);katok['list']['bot'].remove(Dmid);katok['list']['bot'].remove(Emid);katok['list']['bot'].remove(Fmid);backup()
print("LOGIN SUSKSES")
#=========================================================
helpM ="""
╔══════════════╗
║~ping
║~help
║~speed
║~cban
║~onpro
║~offpro
║~onjoin
║~offjoin
║~listpro
╚══════════════╝
"""
def worker(op):
    global time
    global ast
    global groupParam
    try:
        if op.type in [0]:
            return
#=========================================================
        if op.type in [11,122]:
            try:
                if op.param1 in katok['list']['protect']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            L = aa
                            L.deleteOtherFromChat(op.param1,[op.param2])
                            L.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket = True
                            L.updateChat(L.getChats([op.param1]).chats[0],4)
                        except:
                            try:
                                L = bb
                                L.deleteOtherFromChat(op.param1,[op.param2])
                                L.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket = True
                                L.updateChat(L.getChats([op.param1]).chats[0],4)
                            except:
                                try:
                                    L = cc
                                    L.deleteOtherFromChat(op.param1,[op.param2])
                                    L.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket = True
                                    L.updateChat(L.getChats([op.param1]).chats[0],4)
                                except:
                                    try:
                                        L = dd
                                        L.deleteOtherFromChat(op.param1,[op.param2])
                                        L.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket = True
                                        L.updateChat(L.getChats([op.param1]).chats[0],4)
                                    except:
                                        try:
                                            L = ee
                                            L.deleteOtherFromChat(op.param1,[op.param2])
                                            L.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket = True
                                            L.updateChat(L.getChats([op.param1]).chats[0],4)
                                        except:
                                            try:
                                                L = ff
                                                L.deleteOtherFromChat(op.param1,[op.param2])
                                                L.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket = True
                                                L.updateChat(L.getChats([op.param1]).chats[0],4)
                                            except:pass
            except:pass
#=========================================================
        if op.type in [13,124]:
            try:
                Sayang = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
                for pasukan in Sayang:
                    if pasukan in op.param3.split("\x1e"):
                        if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                            pass
                        else:
                            KKami = [cl,aa,bb,cc,dd,ee,ff]
                            for kawankuu in KKami:
                                try:
                                    if op.param1 not in kawankuu.getGroupIdsJoined():
                                        kawankuu.acceptChatInvitation(op.param1)
                                    else:pass
                                except:pass
                    else:pass
            except:pass

        if op.type in [13,124]:
            try:
                if op.param1 in katok['list']['protect']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        missu = op.param3.replace('\x1e',',').split(',')
                        katok["list"]["bleclist"][op.param2] = True
                        for absi in missu:
                            if absi not in katok['list']['owner'] and absi not in katok['list']['bot']:
                                katok["list"]["bleclist"][absi] = True
                                backup()
                                try:
                                    L = aa
                                    for target in katok["list"]["bleclist"]:
                                        if target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids):
                                            L.deleteOtherFromChat(op.param1,[target])
                                            L.cancelChatInvitation(op.param1,[target])
                                        else:pass
                                except:
                                    try:
                                        L = bb
                                        for target in katok["list"]["bleclist"]:
                                            if target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids):
                                                L.deleteOtherFromChat(op.param1,[target])
                                                L.cancelChatInvitation(op.param1,[target])
                                            else:pass
                                    except:
                                        try:
                                            L = cc
                                            for target in katok["list"]["bleclist"]:
                                                if target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids):
                                                    L.deleteOtherFromChat(op.param1,[target])
                                                    L.cancelChatInvitation(op.param1,[target])
                                                else:pass
                                        except:
                                            try:
                                                L = dd
                                                for target in katok["list"]["bleclist"]:
                                                    if target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids):
                                                        L.deleteOtherFromChat(op.param1,[target])
                                                        L.cancelChatInvitation(op.param1,[target])
                                                    else:pass
                                            except:
                                                try:
                                                    L = ee
                                                    for target in katok["list"]["bleclist"]:
                                                        if target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids):
                                                            L.deleteOtherFromChat(op.param1,[target])
                                                            L.cancelChatInvitation(op.param1,[target])
                                                        else:pass
                                                except:
                                                    try:
                                                        L = ff
                                                        for target in katok["list"]["bleclist"]:
                                                            if target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids):
                                                                L.deleteOtherFromChat(op.param1,[target])
                                                                L.cancelChatInvitation(op.param1,[target])
                                                            else:pass
                                                    except:pass
            except:pass
#=========================================================
        if op.type in [17,130]:
            try:
                if op.param1 in katok['list']['join']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:aa.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:bb.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:cc.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:dd.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:ee.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:ff.deleteOtherFromChat(op.param1,[op.param2])
                                            except:pass
                else:
                    if op.param2 in katok["list"]["bleclist"]:
                        try:aa.deleteOtherFromChat(op.param1,[op.param2])
                        except:
                            try:bb.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:cc.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:dd.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:ee.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:ff.deleteOtherFromChat(op.param1,[op.param2])
                                            except:pass
            except:pass
#=========================================================
        if op.type in [19,133]:
            try:
                if op.param1 in katok['list']['protect']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        if op.param3 not in katok['list']['owner'] and op.param3 not in katok['list']['bot']:
                            try:aa.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:bb.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:cc.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:dd.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:ee.deleteOtherFromChat(op.param1,[op.param2])
                                            except:
                                                try:ff.deleteOtherFromChat(op.param1,[op.param2])
                                                except:pass
                        else:pass
                if op.param3 in katok['list']['bot']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            L = aa
                            XYY = {}
                            for targets in katok['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        XYY[x] = True
                                    else:pass
                                else:pass
                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                        except:
                            try:
                                L = bb
                                XYY = {}
                                for targets in katok['list']['bot']:
                                    if targets not in L.getProfile().mid:
                                        if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                            XYY[x] = True
                                        else:pass
                                    else:pass
                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                            except:
                                try:
                                    L = cc
                                    XYY = {}
                                    for targets in katok['list']['bot']:
                                        if targets not in L.getProfile().mid:
                                            if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                XYY[x] = True
                                            else:pass
                                        else:pass
                                    L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                except:
                                    try:
                                        L = dd
                                        XYY = {}
                                        for targets in katok['list']['bot']:
                                            if targets not in L.getProfile().mid:
                                                if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                    XYY[x] = True
                                                else:pass
                                            else:pass
                                        L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                    except:
                                        try:
                                            L = ee
                                            XYY = {}
                                            for targets in katok['list']['bot']:
                                                if targets not in L.getProfile().mid:
                                                    if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                        XYY[x] = True
                                                    else:pass
                                                else:pass
                                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                        except:
                                            try:
                                                L = ff
                                                XYY = {}
                                                for targets in katok['list']['bot']:
                                                    if targets not in L.getProfile().mid:
                                                        if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                            XYY[x] = True
                                                        else:pass
                                                    else:pass
                                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                            except:pass
                if op.param3 in katok['list']['owner']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            L = aa
                            XYY = {}
                            for targets in katok['list']['owner']:
                                if targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    XYY[x] = True
                                else:pass
                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                        except:
                            try:
                                L = bb
                                XYY = {}
                                for targets in katok['list']['owner']:
                                    if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        XYY[x] = True
                                    else:pass
                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                            except:
                                try:
                                    L = cc
                                    XYY = {}
                                    for targets in katok['list']['owner']:
                                        if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                            XYY[x] = True
                                        else:pass
                                    L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                except:
                                    try:
                                        L = dd
                                        XYY = {}
                                        for targets in katok['list']['owner']:
                                            if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                XYY[x] = True
                                            else:pass
                                        L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                    except:
                                        try:
                                            L = ee
                                            XYY = {}
                                            for targets in katok['list']['owner']:
                                                if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                    XYY[x] = True
                                                else:pass
                                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                        except:
                                            try:
                                                L = ff
                                                XYY = {}
                                                for targets in katok['list']['owner']:
                                                    if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                        XYY[x] = True
                                                    else:pass
                                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                            except:pass
            except:pass
#=========================================================
        if op.type in [32,126]:
            try:
                if op.param1 in katok['list']['protect']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        if op.param3 not in katok['list']['owner'] and op.param3 not in katok['list']['bot']:
                            try:aa.deleteOtherFromChat(op.param1,[op.param2])
                            except:
                                try:bb.deleteOtherFromChat(op.param1,[op.param2])
                                except:
                                    try:cc.deleteOtherFromChat(op.param1,[op.param2])
                                    except:
                                        try:dd.deleteOtherFromChat(op.param1,[op.param2])
                                        except:
                                            try:ee.deleteOtherFromChat(op.param1,[op.param2])
                                            except:
                                                try:ff.deleteOtherFromChat(op.param1,[op.param2])
                                                except:pass
                        else:pass
                if op.param3 in katok['list']['bot']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            L = aa
                            XYY = {}
                            for targets in katok['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        XYY[x] = True
                                    else:pass
                                else:pass
                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                        except:
                            try:
                                L = bb
                                XYY = {}
                                for targets in katok['list']['bot']:
                                    if targets not in L.getProfile().mid:
                                        if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                            XYY[x] = True
                                        else:pass
                                    else:pass
                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                            except:
                                try:
                                    L = cc
                                    XYY = {}
                                    for targets in katok['list']['bot']:
                                        if targets not in L.getProfile().mid:
                                            if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                XYY[x] = True
                                            else:pass
                                        else:pass
                                    L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                except:
                                    try:
                                        L = dd
                                        XYY = {}
                                        for targets in katok['list']['bot']:
                                            if targets not in L.getProfile().mid:
                                                if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                    XYY[x] = True
                                                else:pass
                                            else:pass
                                        L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                    except:
                                        try:
                                            L = ee
                                            XYY = {}
                                            for targets in katok['list']['bot']:
                                                if targets not in L.getProfile().mid:
                                                    if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                        XYY[x] = True
                                                    else:pass
                                                else:pass
                                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                        except:
                                            try:
                                                L = ff
                                                XYY = {}
                                                for targets in katok['list']['bot']:
                                                    if targets not in L.getProfile().mid:
                                                        if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                            XYY[x] = True
                                                        else:pass
                                                    else:pass
                                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                            except:pass
                if op.param3 in katok['list']['owner']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            L = aa
                            XYY = {}
                            for targets in katok['list']['owner']:
                                if targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    XYY[x] = True
                                else:pass
                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                        except:
                            try:
                                L = bb
                                XYY = {}
                                for targets in katok['list']['owner']:
                                    if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        XYY[x] = True
                                    else:pass
                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                            except:
                                try:
                                    L = cc
                                    XYY = {}
                                    for targets in katok['list']['owner']:
                                        if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                            XYY[x] = True
                                        else:pass
                                    L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                except:
                                    try:
                                        L = dd
                                        XYY = {}
                                        for targets in katok['list']['owner']:
                                            if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                XYY[x] = True
                                            else:pass
                                        L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                    except:
                                        try:
                                            L = ee
                                            XYY = {}
                                            for targets in katok['list']['owner']:
                                                if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                    XYY[x] = True
                                                else:pass
                                            L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                        except:
                                            try:
                                                L = ff
                                                XYY = {}
                                                for targets in katok['list']['owner']:
                                                    if targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.inviteeMids) or targets not in list(L.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                                        XYY[x] = True
                                                    else:pass
                                                L.deleteOtherFromChat(op.param1,[op.param2]);L.inviteIntoChat(op.param1, XYY)
                                            except:pass
            except:pass
#==============================
        if op.type in [25, 26]:
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            msg.from_ = msg._from
            sender = msg._from
            cmd = text.lower()
            if msg.toType == 0 and sender != cl.profile.mid: to = sender
            else: to = receiver
            if msg._from in katok['list']['owner']:
                if cmd == "ping":
                    aa.sendMessage(to,'pong')
                    bb.sendMessage(to,'pong')
                    cc.sendMessage(to,'pong')
                    dd.sendMessage(to,'pong')
                    ee.sendMessage(to,'pong')
                    ff.sendMessage(to,'pong')

                if cmd == "help":
                    cl.sendMessage(to,helpM)

                if cmd == "speed":
                    start = time.time()
                    cl.getProfile()
                    total = time.time()-start
                    cl.sendMessage(to,str(total))

                if cmd == "cban":
                    katok["list"]["bleclist"] = []
                    cl.sendMessage(to,'done clear BL')
                    backup()

                if cmd == "onpro":
                    if to not in katok['list']['protect']:
                        katok['list']['protect'].append(to)
                        cl.sendMessage(to,"Group sudah diamankan")
                        backup()
                    else:
                        cl.sendMessage(to,"Semua Akses telah di tutup")

                if cmd == "offpro":
                    if to not in katok['list']['protect']:
                        cl.sendMessage(to,"Semua Akses telah di buka")
                    else:
                        katok['list']['protect'].remove(to)
                        cl.sendMessage(to,"Group sudah di buka")
                        backup()

                if cmd == "onjoin":
                    if to not in katok['list']['join']:
                        katok['list']['join'].append(to)
                        cl.sendMessage(to,"Group sudah diamankan")
                        backup()
                    else:
                        cl.sendMessage(to,"Semua Akses telah di tutup")

                if cmd == "offjoin":
                    if to not in katok['list']['join']:
                        cl.sendMessage(to,"Semua Akses telah di buka")
                    else:
                        katok['list']['join'].remove(to)
                        cl.sendMessage(to,"Group sudah di buka")
                        backup()

                if cmd == "listpro":
                    ma = ""
                    mb = ""
                    a = 0
                    b = 0
                    gid = settings["list"]["protect"]
                    for group in gid:
                        a = a + 1
                        end = '\n║'
                        ma += str(a) + ". " +cl.getChats([group]).chats[0].chatName + "\n║"
                    gid = settings["list"]["join"]
                    for group in gid:
                        b = b + 1
                        end = '\n║'
                        mb += str(b) + ". " +cl.getChats([group]).chats[0].chatName + "\n║"
                    cl.sendMessage(to,"╔═╬LIST PROTECT ╬═╗\n║\n║PRO ALL :\n║"+ma+"\n║PRO JOIN :\n║"+mb+"\n╚╬ Total [%s] aktif ╬╝" %(str(len(katok["list"]["protect"])+len(katok["list"]["join"]))))


    except Exception as catch:
        trace = catch.__traceback__
        print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    while True:
        try:
            ops = cl.fetchOps()
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    cl.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                    cl.individualRev = int(op.param1.split("\x1e")[0])
                cl.localRev = max(op.revision, cl.localRev)
                executor.submit(worker,op)
        except:
            pass
            
