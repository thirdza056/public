from Katok.THttpClientLite import THttpClient
from thrift.protocol.TCompactProtocol import TCompactProtocol
from Katok import TalkService
from Katok.ttypes import *
from thrift.Thrift import *
from thrift.TSerialization import *
from thrift.TMultiplexedProcessor import *
from random import randint
import concurrent.futures
import time, json, livejson, requests, threading, os, random, ast, datetime, sys, re, shutil, pytz, tempfile, urllib.parse, base64

class Suwek:
    def __init__(self, myToken, myApp, pool=False):
        self.myToken = myToken
        self.lineServerPoll =  "https://legy-jp-addr-long.line.naver.jp/P4"
        self.lineServerTalk =  "https://legy-jp-addr-long.line.naver.jp/S4"
        self.LINE_OBS_DOMAIN = 'https://obs-tw.line-apps.com'
        self._session = requests.session()
        self.thisHeadersPoll = {}
        self.thisHeadersTalk = {}
        splited = myApp.split("\t")
        self.thisHeadersPoll["x-line-access"] = myToken
        self.thisHeadersPoll["x-line-application"] = myApp
        self.thisHeadersPoll["x-lal"] = "en_id"
        self.thisHeadersPoll["x-las"] = "F"
        self.thisHeadersPoll["x-lam"] = "w"
        self.thisHeadersPoll["x-lac"] = "51089"
        if splited[0] == "ANDROIDLITE":
            self.thisHeadersPoll["user-agent"] = 'LLA/{} Redmi {}'.format(splited[1], splited[3])
        self.thisHeadersTalk["x-line-access"] = myToken
        self.thisHeadersTalk["x-line-application"] = myApp
        self.thisHeadersTalk["x-lal"] = "en_id"
        splited = myApp.split("\t")
        if splited[0] == "ANDROIDLITE":
            self.thisHeadersTalk["user-agent"] = 'LLA/{} Redmi {}'.format(splited[1], splited[3])
        self.talk = self.openTransportTalk()
        self.polling = self.openTransportPoll()
        self.profile = self.getProfile()
        self.serverTime = self.getServerTime()
        self.localRev = -1
        self.globalRev = 0
        self.individualRev = 0
        print("[ Login ] Auth Token: " + myToken)
    
    def openTransportPoll(self):
        transport = THttpClient(self.lineServerPoll)
        transport.setCustomHeaders(self.thisHeadersPoll)
        protocol = TCompactProtocol(transport)
        return TalkService.Client(protocol)
    
    def openTransportTalk(self):
        transport = THttpClient(self.lineServerTalk)
        transport.setCustomHeaders(self.thisHeadersTalk)
        protocol = TCompactProtocol(transport)
        return TalkService.Client(protocol)

    def acceptChatInvitation(self, chatMid):
        return self.talk.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))
    
    def acceptChatInvitationByTicket(self, chatMid, ticketId):
        return self.talk.acceptChatInvitationByTicket(AcceptChatInvitationByTicketRequest(0,chatMid,ticketId))

    def blockContact(self, mid):
        return self.talk.blockContact(0,mid)
    
    def cancelChatInvitation(self,chatMid, targetUserMids):
        return self.talk.cancelChatInvitation(CancelChatInvitationRequest(0,chatMid,targetUserMids))
    
    def createChat(self, name, targetUserMids, picturePath=""):
        return self.talk.createChat(CreateChatRequest(0,0,name,targetUserMids,picturePath))

    def deleteSelfFromChat(self, chatMid):
        return self.talk.deleteSelfFromChat(DeleteSelfFromChatRequest(0,chatMid,0,None,0,""))
                                     
    def deleteOtherFromChat(self, chatMid, targetUserMids):
        return self.talk.deleteOtherFromChat(DeleteOtherFromChatRequest(0,chatMid,targetUserMids))
    
    def fetchOperations(self, deviceId, offsetFrom):
        return self.polling.fetchOperations(FetchOperationsRequest(deviceId,offsetFrom))

    def leaveGroup(self, groupId):
        return self.talk.leaveGroup(0, groupId)

    def fetchOps(self):
        return self.polling.fetchOps(self.localRev,15,self.globalRev,self.individualRev)

    def findAndAddContactsByMid(self, mid, reference=""):
        return self.talk.findAndAddContactsByMid(0,mid,0,reference)
    
    def findAndAddContactsByUserid(self, searchId, reference=""):
        return self.talk.findAndAddContactsByUserid(0,searchId,reference)
    
    def findContactByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    def findChatByTicket(self, ticketId):
        return self.talk.findChatByTicket(FindChatByTicketRequest(ticketId))

    def getGroup(self, groupId):
        return self.talk.getGroup(groupId)
    
    def getGroupIdsInvited(self):
        return self.talk.getGroupIdsInvited()
    
    def getGroupIdsJoined(self):
        return self.talk.getGroupIdsJoined()

    def getAllChatMids(self, withMemberChats=True, withInvitedChats=True, syncReason=0):
        return self.talk.getAllChatMids(GetAllChatMidsRequest(withMemberChats,withInvitedChats),syncReason)

    def getProfile(self, syncReason=0):
        return self.talk.getProfile(syncReason)

    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    def getContact(self, mid):
        return self.talk.getContact(mid)

    def getCountryWithRequestIp(self):
        return self.talk.getCountryWithRequestIp()

    def getServerTime(self):
        return self.talk.getServerTime()

    def getContacts(self, mids):
        return self.talk.getContacts(mids)

    def getAllContactIds(self, syncReason=0):
        return self.talk.getAllContactIds(syncReason)

    def getChats(self, chatMids, withMembers=True, withInvitees=True):
        return self.talk.getChats(GetChatsRequest(chatMids,withMembers,withInvitees))

    def inviteIntoChat(self, chatMid, targetUserMids=[]):
        return  self.talk.inviteIntoChat(InviteIntoChatRequest(0,chatMid,targetUserMids))
    
    def reissueChatTicket(self, chatMid):
        return self.talk.reissueChatTicket(ReissueChatTicketRequest(0,chatMid))
    
    def rejectChatInvitation(self, chatMid):
        return self.talk.rejectChatInvitation(RejectChatInvitationRequest(0,chatMid))
    
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        return self.talk.sendMessage(0,msg)
    
    def sendMessageReply(self, to, text, msgId):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = 0, {}
        msg.relatedMessageId = msgId
        msg.messageRelationType = 3
        msg.relatedMessageServiceCode = 1
        return self.talk.sendMessage(0,msg)
    
    def sendMention(self, to, mid, text):
        mentiones = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x  {}'.format(text)
        return self.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+mentiones+']}'}, contentType=0)

    def unsendMessage(self, messageId):
        return self.talk.unsendMessage(0,messageId)

    def updateChat(self, chat, updatedAttribute):
        return self.talk.updateChat(UpdateChatRequest(0,chat,updatedAttribute))
    
    def updateProfileAttribute(self, attr, value):
        return self.talk.updateProfileAttribute(0,attr,value)

    def postContent(self, url, data=None, files=None, headers=None):
        if headers is None:
            headers=self.thisHeadersTalk
        return self._session.post(url, headers=headers, data=data, files=files)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.thisHeadersTalk
        return self._session.get(url, headers=headers, stream=True)

    def saveFile(self, path, raw):
        with open(path, 'wb') as f:
            shutil.copyfileobj(raw, f)

    def urlEncode(self, url, path, params=[]):
        return url + path + '?' + urllib.parse.urlencode(params)

    def genTempFile(self, returnAs='path'):
        try:
            if returnAs not in ['file','path']:
                raise Exception('Invalid returnAs value')
            fName, fPath = 'linepy-%s-%i.bin' % (int(time.time()), randint(0, 9)), tempfile.gettempdir()
            if returnAs == 'file':
                return fName
            elif returnAs == 'path':
                return os.path.join(fPath, fName)
        except:
            raise Exception('tempfile is required')
    
    def genOBSParams(self, newList, returnAs='json'):
        oldList = {'name': self.genTempFile('file'),'ver': '1.0'}
        if returnAs not in ['json','b64','default']:
            raise Exception('Invalid parameter returnAs')
        oldList.update(newList)
        if 'range' in oldList:
            new_range='bytes 0-%s\/%s' % ( str(oldList['range']-1), str(oldList['range']) )
            oldList.update({'range': new_range})
        if returnAs == 'json':
            oldList=json.dumps(oldList)
            return oldList
        elif returnAs == 'b64':
            oldList=json.dumps(oldList)
            return base64.b64encode(oldList.encode('utf-8'))
        elif returnAs == 'default':
            return oldList

    def downloadObjectMsg(self, messageId, returnAs='path', saveAs=''):
        if saveAs == '':
            saveAs = self.genTempFile('path')
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        params = {'oid': messageId}
        url = self.urlEncode(self.LINE_OBS_DOMAIN, '/talk/m/download.nhn', params)
        r = self.getContent(url)
        if r.status_code == 200:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download object failure.')

    def updateGroupPicture(self, groupId, path):
        files = {'file': open(path, 'rb')}
        data = {'params': self.genOBSParams({'oid': groupId,'type': 'image'})}
        r = self.postContent(self.LINE_OBS_DOMAIN + '/talk/g/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update group picture failure.')
        return True

    def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.postContent(self.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True

