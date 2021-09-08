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
BACOK =[aa,bb,cc,dd,ee,ff]
def backup():
    try:
        backup = katok
        f = codecs.open('warkia.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(error)
        return False
katok['list']['bot'] = [];katok['list']['bot'].append(mid);katok['list']['bot'].append(Amid);katok['list']['bot'].append(Bmid);katok['list']['bot'].append(Cmid);katok['list']['bot'].append(Dmid);katok['list']['bot'].append(Emid);katok['list']['bot'].append(Fmid);backup()
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
║~kick @
║~masuk
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
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            L.deleteOtherFromChat(op.param1,[op.param2])
                            chat = L.getChats([op.param1])
                            if chat.chats[0].extra.groupExtra.preventedJoinByTicket == False:
                                chat.chats[0].extra.groupExtra.preventedJoinByTicket = True
                                L.updateChat(chat.chats[0],4)
                            else:pass
                        except:pass
            except:pass
#=========================================================
        if op.type in [13,124]:
            try:
                Sayang = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
                for pasukan in Sayang:
                    if pasukan in op.param3.split("\x1e"):
                        if op.param2 not in katok['list']['owner'] and op.param2 not in katok['list']['bot']:
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
                        katok["list"]["bleclist"][op.param2] = True
                        missu = op.param3.replace('\x1e',',').split(',')
                        if len(missu) >= 10:
                            missu = missu[0:10]
                        for absi in missu:
                            if absi not in katok['list']['owner'] and absi not in katok['list']['bot']:
                                katok["list"]["bleclist"][absi] = True
                                backup()
                                try:
                                    if op.param1 not in katok['list']['join']:
                                        katok['list']['join'].append(op.param1);backup()
                                        LSB = []
                                        for bobot in BACOK:
                                            if op.param1 in bobot.getGroupIdsJoined():
                                                LSB.append(bobot)
                                        L = random.choice(LSB)
                                        XYY = {}
                                        chat = cl.getChats([op.param1]).chats[0]
                                        for targets in katok['list']['bot']:
                                            if targets not in L.getProfile().mid:
                                                if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                                    if targets not in L.getAllContactIds():
                                                        L.findAndAddContactsByMid(targets)
                                                        XYY[targets] = True
                                                    else:
                                                        XYY[targets] = True
                                                else:pass
                                            else:pass
                                        for target in katok["list"]["bleclist"]:
                                            if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(chat.extra.groupExtra.inviteeMids):
                                                L.cancelChatInvitation(op.param1,[target])
                                                L.deleteOtherFromChat(op.param1,[target])
                                            else:pass
                                        L.inviteIntoChat(op.param1, XYY)
                                    else:
                                        LSB = []
                                        for bobot in BACOK:
                                            if op.param1 in bobot.getGroupIdsJoined():
                                                LSB.append(bobot)
                                        L = random.choice(LSB)
                                        XYY = {}
                                        chat = cl.getChats([op.param1]).chats[0]
                                        for targets in katok['list']['bot']:
                                            if targets not in L.getProfile().mid:
                                                if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                                    if targets not in L.getAllContactIds():
                                                        L.findAndAddContactsByMid(targets)
                                                        XYY[targets] = True
                                                    else:
                                                        XYY[targets] = True
                                                else:pass
                                            else:pass
                                        for target in katok["list"]["bleclist"]:
                                            if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids) or target in list(chat.extra.groupExtra.inviteeMids):
                                                L.cancelChatInvitation(op.param1,[target])
                                                L.deleteOtherFromChat(op.param1,[target])
                                            else:pass
                                        L.inviteIntoChat(op.param1, XYY)
                                except:pass
            except:pass
#=========================================================
        if op.type in [17,130]:
            try:
                if op.param1 in katok['list']['join']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in katok['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in katok["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                        except:pass
                else:
                    if op.param2 in katok["list"]["bleclist"]:
                        try:
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in katok['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in katok["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                        except:pass
            except:pass
#=========================================================
        if op.type in [19,133]:
            try:
                if op.param3 in katok['list']['bot']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in katok['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in katok["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                        except:pass
                if op.param1 in katok['list']['protect']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            if op.param3 not in katok['list']['owner'] and op.param3 not in katok['list']['bot']:
                                LSB = []
                                for bobot in BACOK:
                                    if op.param1 in bobot.getGroupIdsJoined():
                                        LSB.append(bobot)
                                L = random.choice(LSB)
                                chat = cl.getChats([op.param1]).chats[0]
                                for target in katok["list"]["bleclist"]:
                                    if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        L.deleteOtherFromChat(op.param1,[target])
                            else:pass
                        except:pass
                if op.param3 in katok['list']['owner']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in katok['list']['owner']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in katok["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                        except:pass
            except:pass
#=========================================================
        if op.type in [32,126]:
            try:
                if op.param3 in katok['list']['bot']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in katok['list']['bot']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in katok["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
                        except:pass
                if op.param1 in katok['list']['protect']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            if op.param3 not in katok['list']['owner'] and op.param3 not in katok['list']['bot']:
                                LSB = []
                                for bobot in BACOK:
                                    if op.param1 in bobot.getGroupIdsJoined():
                                        LSB.append(bobot)
                                L = random.choice(LSB)
                                chat = cl.getChats([op.param1]).chats[0]
                                for target in katok["list"]["bleclist"]:
                                    if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                        L.deleteOtherFromChat(op.param1,[target])
                            else:pass
                        except:pass
                if op.param3 in katok['list']['owner']:
                    if op.param2 not in katok['list']['owner'] and op.param2 not in  katok['list']['bot']:
                        katok["list"]["bleclist"][op.param2] = True
                        backup()
                        try:
                            LSB = []
                            for bobot in BACOK:
                                if op.param1 in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            XYY = {}
                            chat = cl.getChats([op.param1]).chats[0]
                            for targets in katok['list']['owner']:
                                if targets not in L.getProfile().mid:
                                    if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                        if targets not in L.getAllContactIds():
                                            L.findAndAddContactsByMid(targets)
                                            XYY[targets] = True
                                        else:
                                            XYY[targets] = True
                                    else:pass
                                else:pass
                            for target in katok["list"]["bleclist"]:
                                if target in list(cl.getChats([op.param1]).chats[0].extra.groupExtra.memberMids):
                                    L.deleteOtherFromChat(op.param1,[target])
                                else:pass
                            L.inviteIntoChat(op.param1, XYY)
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
                    if to in aa.getGroupIdsJoined():
                        aa.sendMessage(to,'~pong~')
                    else:pass
                    if to in bb.getGroupIdsJoined():
                        bb.sendMessage(to,'~pong~')
                    else:pass
                    if to in cc.getGroupIdsJoined():
                        cc.sendMessage(to,'~pong~')
                    else:pass
                    if to in dd.getGroupIdsJoined():
                        dd.sendMessage(to,'~pong~')
                    else:pass
                    if to in ee.getGroupIdsJoined():
                        ee.sendMessage(to,'~pong~')
                    else:pass
                    if to in ff.getGroupIdsJoined():
                        ff.sendMessage(to,'~pong~')
                    else:pass

                if cmd == "help":
                    cl.sendMessage(to,helpM)

                if cmd == "speed":
                    start = time.time()
                    cl.getProfile()
                    total = time.time()-start
                    cl.sendMessage(to,str(total))

                if cmd == "cban":
                    cl.sendMessage(to, "Hapus %s mantan"%(str(len(katok["list"]["bleclist"]))))
                    katok["list"]["bleclist"] = {}
                    katok['list']['join'] = []
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
                    gid = katok["list"]["protect"]
                    for group in gid:
                        a = a + 1
                        end = '\n║'
                        ma += str(a) + ". " +cl.getChats([group]).chats[0].chatName + "\n║"
                    gid = katok["list"]["join"]
                    for group in gid:
                        b = b + 1
                        end = '\n║'
                        mb += str(b) + ". " +cl.getChats([group]).chats[0].chatName + "\n║"
                    cl.sendMessage(to,"╔═╬LIST PROTECT ╬═╗\n║\n║PRO ALL :\n║"+ma+"\n║PRO JOIN :\n║"+mb+"\n╚╬ Total [%s] aktif ╬╝" %(str(len(katok["list"]["protect"])+len(katok["list"]["join"]))))

                if cmd.startswith("kick "):
                    try:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            katok["list"]["bleclist"][target] = True
                            LSB = []
                            for bobot in BACOK:
                                if to in bobot.getGroupIdsJoined():
                                    LSB.append(bobot)
                            L = random.choice(LSB)
                            L.deleteOtherFromChat(to,[target])
                    except:pass

                if cmd == "masuk":
                    try:
                        L = cl
                        XYY = {}
                        chat = cl.getChats([to]).chats[0]
                        for targets in katok['list']['bot']:
                            if targets not in L.getProfile().mid:
                                if targets not in list(chat.extra.groupExtra.inviteeMids) and targets not in list(chat.extra.groupExtra.memberMids):
                                    if targets not in L.getAllContactIds():
                                        L.findAndAddContactsByMid(targets)
                                        XYY[targets] = True
                                    else:
                                        XYY[targets] = True
                                else:pass
                            else:pass
                        L.inviteIntoChat(to, XYY)
                        KKami = [aa,bb,cc,dd,ee,ff]
                        for kawankuu in KKami:
                            try:
                                if to not in kawankuu.getGroupIdsJoined():
                                    kawankuu.acceptChatInvitation(to)
                                else:pass
                            except:pass
                    except:pass

    except Exception as catch:
        trace = catch.__traceback__
        print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
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
            
