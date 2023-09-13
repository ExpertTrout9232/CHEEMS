import os
import re

#Made by ExpertTrout9232 for CHEEMS - An 8 bit 1.25 Hz redstone cpu by TosinV1

code = open("input.cheems").read().splitlines() #Formatting file
code = list(map(str.strip, code))
for i in range(len(code)):
    code[i] = code[i].split("//")[0]
code = list(map(str.strip, code))
code = list(filter(None, code))
index = 0 #Initialization
instruction = 0
opcode = 0
argument = 0
if not os.path.exists("machine codes"):
    os.mkdir("machine codes")
if os.path.exists("machine codes\output.bin") == True:
    os.remove("machine codes\output.bin")
open("machine codes\output.bin", 'a').close()
opcodes = {
    "NO-OP":"00000000\n",
    "CND":"00001",
    "ADD":"00010",
    "ADD-REG":"00011",
    "ADDC":"00100",
    "SUB":"00101",
    "SUB-ACC":"00110",
    "INC":"00111000\n",
    "DEC":"01000000\n",
    "RSH":"01001",
    "LSH":"01010",
    "XOR":"01011",
    "NOR":"01100",
    "AND":"01101",
    "CMP":"01110",
    "LDI":"01111",
    "LIA":"10000000\n",
    "JMPI":"10001000\n",
    "JMP":"10010",
    "JIF":"10011",
    "SWC":"10100",
    "SWCI":"10101000\n",
    "RET":"10110000\n",
    "CALL":"10111000\n",
    "RLD":"11000",
    "RST":"11001",
    "PST":"11010",
    "PLD":"11011",
    "PUSH":"11100000\n",
    "POP":"11101000\n",
    "MST":"11110",
    "MLD":"11111"
}
other = {
    "R0":"000\n",
    "R1":"001\n",
    "R2":"010\n",
    "R3":"011\n",
    "R4":"100\n",
    "R5":"101\n",
    "R6":"110\n",
    "R7":"111\n",
    "$0":"000\n",
    "$1":"001\n",
    "$2":"010\n",
    "$3":"011\n",
    "$4":"100\n",
    "$5":"101\n",
    "$6":"110\n",
    "$7":"111\n",
    "HALT":"000\n",
    "RESET":"001\n",
    "DISFLAG":"010\n",
    "EQ":"000\n",
    "GE":"001\n",
    "CF":"010\n",
    "NE":"011\n",
    "!EQ":"100\n",
    "LT":"101\n",
    "!CF":"110\n",
    "PO":"111\n"
}
while index < len(code): #Preparation loop
    instruction = code[index]
    if instruction.upper()[0:7] == "@DEFINE":
        instruction = instruction.split(' ')
        for i in range(len(code)):
            code[i] = re.sub(r'\b{}\b'.format(re.escape(instruction[1])), instruction[2], code[i])
        del code[index]
        index -= 1        
    if instruction[0:1] == ".":
        for i in range(len(code)):
            code[i] = code[i].replace("$" + instruction[1:] + "$", str(index))
        del code[index]
        index -= 1
    if instruction[0:1] == "~":
        code[index] = str(index + int(instruction[1:]))
    index += 1
index = 0
while index < len(code): #Main loop
    instruction = code[index].split(' ')
    if len(instruction) == 1:
        if not re.match("^[0-9]+$", instruction[0]):
            opcode = opcodes.get(instruction[0].upper())
            argument = ""
        else:
            opcode = format(int(instruction[0]), '08b') + "\n"
            argument = ""
    else:
        opcode = opcodes.get(instruction[0].upper())
        argument = other.get(instruction[1].upper())
    with open("machine codes\output.bin", 'a') as file: #File saving
        file.write(str(opcode) + str(argument))
    index += 1 
