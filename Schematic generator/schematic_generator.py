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

lines = int(abs(z) / 8) + 1 #Initialization for main loop
linesi = 0
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
            'minecraft:stone', 'minecraft:barrel{Items:[{Slot:0,Slot:0,id:"minecraft:totem_of_undying",Count:1}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:2}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:4}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:6}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:8}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:10}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:12}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:14}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:16}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:18}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:20}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:22}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:24}]}',
            'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:26}]}', 'minecraft:barrel{Items:[{Slot:0,id:"minecraft:totem_of_undying",Count:27}]}'
            ]
while lines > linesi: #Main loop
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
        linesi += 1 

if not os.path.exists("schematics"):
    os.mkdir("schematics")
final_schem.save("schematics", "output", mcschematic.Version.JE_1_18_2) #Saving the schematic
