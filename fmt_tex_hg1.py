from inc_noesis import *

#registerNoesisTypes is called by Noesis to allow the script to register formats.
#Do not implement this function in script files unless you want them to be dedicated format modules!
def registerNoesisTypes():
    handle = noesis.register("Heavy Gear 1 Image", ".tex")
    noesis.setHandlerTypeCheck(handle, texCheckType)
    noesis.setHandlerLoadRGBA(handle, texLoadRGBA)
    return 1

class TEXImage:
    def __init__(self, reader):
        self.reader = reader

    def parseHeader(self):
        bs = self.reader
        bs.seek(0, NOESEEK_ABS)
        magic = bs.readUInt()
        if magic != 842149425:
            return -1
        self.reader.seek(2, NOESEEK_REL)    
        self.imageWidth = bs.readUShort()
        self.imageHeight = bs.readUShort()
        self.paletteSize = bs.readUShort()
        self.paletteOffset = bs.tell()
        self.indexesOffset = self.paletteOffset + 4*self.paletteSize
        return 0
        
    def getData(self):
        bs = self.reader
        palBuffer = bs.getBuffer()[self.paletteOffset:self.indexesOffset]
        indBuffer = bs.getBuffer()[self.indexesOffset:] 
        imageData = noesis.allocBytes(self.imageWidth*self.imageHeight*4)
        for i in range(0, self.imageWidth*self.imageHeight):
            imageData[i*4] = palBuffer[indBuffer[i]*4]
            imageData[i*4 + 1] = palBuffer[indBuffer[i]*4 + 1]
            imageData[i*4 + 2] = palBuffer[indBuffer[i]*4 + 2]
            imageData[i*4 + 3] = palBuffer[indBuffer[i]*4 + 3]
        noesis.logPopup()  
        print(palBuffer[indBuffer[i]*4])        
        return imageData       
	
def texCheckType(data):
    tex = TEXImage(NoeBitStream(data))
    if tex.parseHeader() != 0:
        return 0
    return 1

def texLoadRGBA(data, texList):
    tex = TEXImage(NoeBitStream(data))
    if tex.parseHeader() != 0:
        return 0
    texList.append(NoeTexture("textex", tex.imageWidth, tex.imageHeight, tex.getData(), noesis.NOESISTEX_RGBA32))
    return 1

