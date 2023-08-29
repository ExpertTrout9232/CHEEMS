import mcschematic
import os

#Made by ExpertTrout9232 for CHEEMS - An 8 bit 1.25 Hz redstone cpu by TosinV1

machine_code = open("input.bin").read().splitlines() #Formatting the machine code
machine_code = list(filter(None, machine_code))
machine_code = list(map(str.strip, machine_code))
schem = mcschematic.MCSchematic() #Initialization
final_schem = mcschematic.MCSchematic()
x = 0
z = 0
y = -1
byte = 0
bit = 0
instruction = 0

while byte < len(machine_code): #Preparation loop
    instruction = machine_code[byte]
    y = -1
    bit = 0
    while bit < 8:
        if instruction[bit:bit + 1] == "1":
            schem.setBlock((x, y, z), "minecraft:black_concrete")
        else:
            schem.setBlock((x, y, z), "minecraft:stone")
        y -= 2
        bit += 1
    byte += 1
    x += 2
    if x == 32:
        x = 0
        z -= 2

lines = abs(z) #Initialization for main loop
z = 0
zi = 0
x = 0
y = -1
instruction1 = 0
instruction2 = 0
instruction3 = 0
instruction4 = 0
ss = 0
barrels = [
            'minecraft:stone', 'minecraft:barrel[facing=up]{CustomName:"1",Items:[{id:"minecraft:golden_axe",Count:1}]}',
            'minecraft:barrel[facing=up]{CustomName:"2",Items:[{id:"minecraft:golden_axe",Count:2}]}', 'minecraft:barrel[facing=up]{CustomName:"3",Items:[{id:"minecraft:golden_axe",Count:4}]}',
            'minecraft:barrel[facing=up]{CustomName:"4",Items:[{id:"minecraft:golden_axe",Count:6}]}', 'minecraft:barrel[facing=up]{CustomName:"5",Items:[{id:"minecraft:golden_axe",Count:8}]}',
            'minecraft:barrel[facing=up]{CustomName:"6",Items:[{id:"minecraft:golden_axe",Count:10}]}', 'minecraft:barrel[facing=up]{CustomName:"7",Items:[{id:"minecraft:golden_axe",Count:12}]}',
            'minecraft:barrel[facing=up]{CustomName:"8",Items:[{id:"minecraft:golden_axe",Count:14}]}', 'minecraft:barrel[facing=up]{CustomName:"9",Items:[{id:"minecraft:golden_axe",Count:16}]}',
            'minecraft:barrel[facing=up]{CustomName:"10",Items:[{id:"minecraft:golden_axe",Count:18}]}', 'minecraft:barrel[facing=up]{CustomName:"11",Items:[{id:"minecraft:golden_axe",Count:20}]}',
            'minecraft:barrel[facing=up]{CustomName:"12",Items:[{id:"minecraft:golden_axe",Count:22}]}', 'minecraft:barrel[facing=up]{CustomName:"13",Items:[{id:"minecraft:golden_axe",Count:24}]}',
            'minecraft:barrel[facing=up]{CustomName:"14",Items:[{id:"minecraft:golden_axe",Count:26}]}', 'minecraft:barrel[facing=up]{CustomName:"15",Items:[{id:"minecraft:golden_axe",Count:27}]}'
            ]
while lines != 0: #Main loop
    y = -1
    while y > -16:
        ss = 0
        instruction1 = schem.getBlockDataAt((x, y, z))
        instruction2 = schem.getBlockDataAt((x, y, z - 2))
        instruction3 = schem.getBlockDataAt((x, y, z - 4))
        instruction4 = schem.getBlockDataAt((x, y, z - 6))
        if instruction1 == "minecraft:black_concrete": 
            ss += 1
        else:
            ss += 0
        if instruction2 == "minecraft:black_concrete": 
            ss += 2
        else:
            ss += 0        
        if instruction3 == "minecraft:black_concrete": 
            ss += 4
        else:
            ss += 0
        if instruction4 == "minecraft:black_concrete": 
            ss += 8
        else:
            ss += 0
        final_schem.setBlock((x, y, zi), barrels[ss])
        y -= 2
    x += 2
    if x == 32:
        x = 0
        z -= 8
        zi -= 2
        lines = int(lines / 8)

if not os.path.exists("schematics"):
    os.mkdir("schematics")
final_schem.save("schematics", "output", mcschematic.Version.JE_1_18_2) #Saving the schematic
