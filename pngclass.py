#==============================================================#
import zlib

#==============================================================#
class pixel():
    def __init__(self, color = 1):
        self.color = 1

    def setcolor(self, color):
        self.color = color

    def getcolor(self):
        return self.color

#==============================================================#
class picture():
    def __init__(self, width, hieght):
        self.width = width
        self.hieght = hieght

        self.dict = {}

        for num in range(self.width * self.hieght):
            x = num % self.width
            y = num // self.width

            self.dict[x, y] = pixel()

    def __getitem__(self, key):
        return self.dict[key]

#==============================================================#
class png():
    def __init__(self, width, hieght):
        self.width = width
        self.hieght = hieght

        self.signature = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
        self.IEND = b'\x00\x00\x00\x00IEND\xaeB`\x82'
        
        self.pict = picture(width, hieght)

    def __getitem__(self, key):
        return self.pict[key]

    def create(self, filename):
        toCleanFile(filename)

        with open(filename, 'ab') as file:
            file.write(self.signature)
            addIHDR(self, file)
            addIDAT(self, file)
            file.write(self.IEND)

#==============================================================#
def toCleanFile(filename):
    with open(filename, 'w') as file:
        file.write('')

#==============================================================#
def bin2byte(string):
    result = 0
    string = string[::-1]
    for n in range(8):
        result += int(string[n]) * (2 ** n)

    return result.to_bytes(1, 'big')

#==============================================================#
def addIHDR(self, file):
    IHDRname = b'IHDR'
    IHDRdata = (
        self.width.to_bytes(4, 'big') +
        self.hieght.to_bytes(4, 'big') +
        b'\x01\x00\x00\x00\x00'
        )
    IHDRlen = len(IHDRdata).to_bytes(4, 'big')
    IHDRcrc = zlib.crc32(IHDRname + IHDRdata).to_bytes(4, 'big')
            
    file.write(IHDRlen)
    file.write(IHDRname)
    file.write(IHDRdata)
    file.write(IHDRcrc)

#==============================================================#
def addIDAT(self, file):
    IDATname = b'IDAT'
    IDATdata = b''

    tempstr = ''
    for y in range(self.hieght):
        for x in range(self.width):
            tempstr += str(self[x, y].getcolor())

            if x == 0:
                IDATdata += b'\x00'
                        
            if len(tempstr) == 8:
                IDATdata += bin2byte(tempstr)
                tempstr = ''

            elif x == self.width - 1:
                tempstr += (8 - len(tempstr)) * '0'
                IDATdata += bin2byte(tempstr)
                tempstr = ''
                    
    IDATdata = zlib.compress(IDATdata)
    IDATlen = len(IDATdata).to_bytes(4, 'big')
    IDATcrc = zlib.crc32(IDATname + IDATdata).to_bytes(4, 'big')

    file.write(IDATlen)
    file.write(IDATname)
    file.write(IDATdata)
    file.write(IDATcrc)
