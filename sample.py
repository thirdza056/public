from function import *
import ast, time, json, codecs, re, subprocess

appNya = "ANDROIDLITE\t2.16.0\tAndroid OS\t10.0"

cl = Suwek(myToken="Token kamu", myApp=appNya)

clProfile = cl.getProfile()
mid = cl.getProfile().mid

Owner = ["u7368e7f90b05bd883d538f4248ee5a6b"]
Bots = [mid]

settings = {
    "autojoin": True
    }

helpM ="""
╔══════════════╗
║~ping
║~help
║~speed
╚══════════════╝
"""

def worker(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 13 or op.type == 124:
            if settings["autojoin"] == True:
                if mid in op.param3.split("\x1e"):
                    if op.param2 not in Owner and op.param2 not in Bots:
                        pass
                    else:
                        cl.acceptChatInvitation(op.param1)

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
            if msg._from in Owner:
                if cmd == "ping":
                    cl.sendMessage(to,'pong')

                if cmd == "help":
                    cl.sendMessage(to,helpM)

                if cmd == "speed":
                    start = time.time()
                    cl.getProfile()
                    total = time.time()-start
                    cl.sendMessage(to,str(total))

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
            
