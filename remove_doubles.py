# python 3.7

def remove_doubles(x):
  # create dict from list and back - dicts do not have doubles)  
  return list(dict.fromkeys(x))


f=open(input("bestand met dubbele waarden: "), encoding='utf-8')
f_out = open(input("resultaatbestand met unieke waarden: "), "a", encoding='utf-8')
lineList = f.read().splitlines()
uniqueList = remove_doubles(lineList)


for item in uniqueList:
    f_out.write("%s\n" % item)