import os

# takes a encode string as args, decode it
# to meaningfull text commands
'''
def codeToCommand(_line):
   # system code definition as dict 
   # [key:code, value:command txt].
    M = {
            "Mpath" : "./src/main.cpp",
            "M101" : "[MCU I/O pin modes initiated]",
            "M102" : "[DS18B20 sensors initiated]",
            "M103" : "[unable to initiated DS18B20]",
            "M104" : "[Serial Communication initiated]"
        }

    P = {
            "Ppath" : "./lib/PCF8547_IOEXP/PCF8547_IOEXP.h",
            "P201" : "[*** NOT DEFINED ***]",
            "P202" : "[Successfully initialised I2C_RELAY module 1]",
            "P203" : "[I2C_RELAY 1 I/O pins initiated]",
            "P204" : "[I2C_RELAY 1 device error!]",
            "P205" : "[Successfully initialised I2C_RELAY module 2]",
            "P206" : "[I2C_RELAY 2 I/O pins initiated]",
            "P207" : "[I2C_RELAY 2 device error!] ",
            "P208" : "[I2C_RELAY 1 is Connected]",
            "P209" : "[I2C_RELAY 1 is Disconnected]",
            "P210" : "[I2C_RELAY 2 is Connected]",
            "P211" : "[I2C_RELAY 2 is Disconnected]"
        }

    S = {
            "Spath" : "./lib/Sensors/Sensors.h",
            "S101" : "[Auto initialised DS18B20 sensors]",
            "S102" : "[Preinitialised DS18B20 sensors]",
        }

    R = {
            "Rpath": "./lib/RelayControl/RelayControl.h",
            "R0"  : "[Undefined device]",
            "R11" : "[PELTIER 1]",
            "R12" : "[PELTIER 2]",
            "R13" : "[PELTIER 3]",
            "R14" : "[PELTIER 4]",
            "R15" : "[AC BLOWER FAN]",
            "R16" : "[RADIATOR FAN]",
            "R17" : "[HS WATER PUMP]",
            "R18" : "[CS WATER PUMP]",
            "R21" : "[CABIN EXHAUST1 IN]",
            "R22" : "[CABIN EXHAUST1 OUT]",
            "R23" : "[CABIN EXHAUST2 IN]",
            "R24" : "[CABIN EXHAUST2 OUT]",
            "R25" : "[CABIN2 LIGHT]",
            "R26" : "NOCP0",
            "R27" : "NOCP1",
            "R28" : "NOCP2",
            "An" : "[switched ON]",
            "Bn" : "[already switched ON]", 
            "Xf" : "[switched OFF]",
            "Yf" : "[already switched OFF]",
        }
    

    _line = _line.replace(" ", "").upper()
    print(_line)

    if _line[0] == 'M':
        if _line in M.keys(): return M[_line]
        else: print("key not found")
    elif _line[0] == 'P':
        if _line in P.keys(): return P[_line]
        else: print("key not found")
    elif _line[0] == 'S':
        if _line in S.keys(): return S[_line]
        else: print("key not found")
    elif _line[0] == 'R':
        if _line in R.keys(): return R[_line]
        else: print("key not found")
'''

class decode:
    # @debug.try [ex-args]
    code1 = "M101"
    code2 = "P210"
    #eof = "$EOF$"
    global path, msgClause
    path = f"{os.getcwd()}/codes.txt"
    msgClause = "%"
    
    # decode and return only message from a line/string
    def getMsg(self, _line):
        cmdSIndex = _line.index(msgClause)
        cmdEIndex = _line.index(msgClause, cmdSIndex+1)
        #print(cmdSIndex)
        #print(type(cmdSIndex))
        #print(cmdEIndex)
        #print(type(cmdEIndex))
        return _line[cmdSIndex+2:cmdEIndex-1]

    # decode and return only code from a line/string
    def getCode(self, _line):
        return _line[0:_line.index(msgClause)]

    # find and return respective message for input code 
    # as args, open file@_path and check for match
    def decodeCmd(self, _code, _path = path):
        lineNo = 0
        if os.path.exists(_path):
            with open(_path, 'r') as _filedet:
                while(True):
                    _line = _filedet.readline()
                    if _line == "#EOF": break
                    else:
                        if(self.getCode(_line) == _code):
                            return lineNo+1, self.getMsg(_line)
                    lineNo += 1
        else: print("NOT EXISTS")

    # detects code and message from each line respectively,
    # and returns seperately
    def printSep(self, _path = path):
        _lineNo = 0
        if os.path.exists(_path):
            with open(_path, 'r') as _file:
                while True:
                    line = _file.readline()
                    #print(line, end="\b")
                    if line == "#EOF#": break
                    else:
                        _lineNo+=1
                        print("Line No: ", _lineNo)
                        print("  Code: ", self.getCode(line))
                        print("  Message: ", self.getMsg(line))
                        print()
        else: 
            print("NOT EXISTS")
            

# main
if __name__ == "__main__":
    # codeIndex = ['M','m', 'P', 'p', 'S', 's', 'R', 'r']
    Decode = decode()
    cmd = int(input("Enter the command: "))
    if cmd == 1:
        Decode.printSep()
    elif cmd == 2:
        print(Decode.decodeCmd(input("Enter the code: ")))
        



