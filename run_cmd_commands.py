# python 3.7
# leest bestand met regels met commands die van windows cmd prompt gerund moeten worden
# en voert deze achtereenvolgens uit

import os, subprocess

filename=input("geef lijst met commands: ")


with open(filename, encoding='utf-8') as f:
    cmdlist = f.read().splitlines()

    for cmd in cmdlist:
        try:
            return_code = subprocess.call(cmd, shell=True)
            print(return_code)
        
        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
