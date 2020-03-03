# python 3.7
# to import multiple files in nested directories on local machine into MongoDB

import os

rootdir = input("geef directory: ")
databasename = input("databasenaam: ")
outfile = input("geef outputfile naam: ")
f_out=open(outfile, "a")

for dirpath, dirs, files in os.walk(rootdir): 
    for filename in files:
        fname = os.path.join(dirpath,filename).replace("\\","//")
        if fname.endswith('.json'):
            fshortname = os.path.splitext(filename)[0]
            commandstr = "mongoimport --db " + databasename + " --collection "+  fshortname + " --file "+ fname + " --jsonArray --upsertFields=\"id\" " 
            
            f_out.write(commandstr)
            f_out.write("\n")
f_out.close()