#a udp server

from twisted.internet.defer import Deferred
from twisted.internet.protocol import DatagramProtocol

class CCDProtocol(DatagramProtol):
    
    def startProtocol(self):
        host = "127.0.0.0"
        port = 1000
        self.transport.connet(host, port)
        self.transport.write("this is ccd server")

    def datagramReceived(self, data, (host, port)):
        print "received %r from %s:%d" %(data, host, port)

    def connectionRefused(self):
        print "no one listening"


class CCDService(object):

    frameList= [] 
    def __int__(self, protocol):
        self.protocol = protocol
        self.frameWidth = 667
        self.frameHeight = 515
        self.frameSize = (self.frameWidth*3+3)/4*4*self.frameHeight 
        self.packageMaxSize = 60007
        self.packageHeadSize = 7
        self.lastPackageSize = self.frameSize%self.packageMaxSize + self.packageHeadSize
        if self.lastPackageSize > self.packageHeadSize 
            self.pacakgeNum = int(self.frameSize/self.packageMaxSize)+1
        else:
            self.pacakgeNum = int(self.frameSize/self.packageMaxSize)
        #first the value of id1 is 0, then if it is more than 255,set it as 1
        self.id1 = 0
        self.defferred  = None


    def getFrameInfo(self):
        frameInfo = []
        def trans(data, lenth):
            for i in range(0, length):
                n = 0xff&(m>>8*i)
                frameInfo.append(chr(n))

        #1 frame size
        frameInfo.append('F')
        trans(self.frameSize, 3)
        #2 width
        frameInfo.append('W')
        trans(self.frameWidth, 2)
        #3 height
        frameInfo.append('H')
        trans(self.frameHeight, 2)
        #4 package max size
        frameInfo.append('P')
        trans(self.packageMaxSize, 2)
        #5 last package size
        frameInfo.append('L')
        trans(self.lastPackageSize, 2)
        #6 package num
        frameInfo.append('N')
        trans(self.packageNum, 1)
        #conver list to string
        str1 = ''.join(frameInfo)
        return str1

    def accpetNewFrame (self, frame):
        self.frameList.append(frame)
        self.sendFrame()

    def parseCommand(self, res):
        if res is not None:
            date = res.split(';')
            if data[0] == 'requireFrameInfo':
                self.sendFrameInfo()
            elif data[0] == 'requireFrame':
                self.sendFrame()
            else:
                self.errCommand()

    def errCommand(self):
        return "err command"

    def sendFrameInfo(self):
        self.protocol.transport.write(getFremeInfo())

    def sendFrame(self):
        def getPackageInfo(id2):
            return 'ID'+chr(0xff)+chr(0xff&id1)+chr(0xff)+chr(0xff&id2)+chr(0xff)

        def sendPackage(id2):
            pac = getPackageInfo(id2)+frameList[0][id2 : (id2+1)*self.]
            id2 = id2 + 1
            self.protocol.transport.write(pac)
            if id2 == self.packageNum:
                self.id1 = self.id1 + 1
                if self.id1 == 256:
                    self.id1 = 1
                
            return id2

        def errHandle(err):
            log.msg("err: %s" %err)
            deferred, self.deferred = self.deferred, None
            deferred.cancel()
            pass

        def cancelerErr(err):
            log.msg("cancel err: %s" %err)
            pass

        if self.deferred is not None:
            deferred, self.deferred = self.deferred, None
            deferred.cancel()

        self.deferred = Deferred(cancelerErr)
        for i in range(0, self.packageNum):
            self.deferred.addCallbacks(sendPackage, errHandle)
        self.deferred.callback(0)

class ImageGenerator(object):
    """a virtrual ccd"""
    def __init__(self, ccdService):
        self.ccdService = ccdService
        """#file data format:
        imagefileName(including the dir);imagefilename2;imagefilename3;.....imagefileelneameN;
        """
        self.fileName = fileName

    def generatorImage(self):
        return image

    def getImageData(self):
        return
    
    def getImageFile(self):
        """base the file w












