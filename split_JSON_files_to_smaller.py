#python 3.7 
# modified from https://stackoverflow.com/questions/7052947/split-huge-95mb-json-array-into-smaller-chunks


import json, os, shutil

rootdir = input("Type rootdir: ")
outdir = input("Type outdir: ")
skip_file = input("Type location of log file: ")
try:
    chunkSize = int(input("Set chunk size: "))
except ValueError:
    print("Chunksize not an integer value...")    

try:
    cutoffsize = int(input("Set cut off size: "))
except ValueError:
    print("Cutoff size not an integer value...")

try:
    for dirpath, dirs, files in os.walk(rootdir): 
        for filename in files:
            fname = os.path.join(dirpath,filename)
            fsize = os.path.getsize(fname)
            if fname.endswith('.json'):
                
                if ((fsize/cutoffsize) < 200):
                    f_skip = open(skip_file, "a")
                    f_skip.write(str(fsize/cutoffsize) +" kb " + fname + "\n")
                else:
                    with open(fname,'r', encoding='UTF-8') as infile:
                        o = json.load(infile)
                        
                        for i in range(0, len(o), chunkSize):
                            with open( fname + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
                                json.dump(o[i:i+chunkSize], outfile)
                                outfile.close() 
                                f_out=outfile.name
                                os.makedirs(os.path.dirname(f_out.replace( rootdir, outdir)), exist_ok=True)
                                shutil.move(f_out, f_out.replace( rootdir, outdir) ) 

                            
except Exception as e:
    if hasattr(e, 'message'):
        print(e.message)
    else:
        print(e)