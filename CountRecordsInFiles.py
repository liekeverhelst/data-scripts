# python 3.7 64 bit
# From all files in a folder and subfolder count all records and display filename and number of records. 
import os, json

csv_dir = input("Geef brondirectory: ")
count = 0
try:
    for dirpath, dirs, files in os.walk(csv_dir): 
        
        
        for filename in files:
            fname = os.path.join(dirpath,filename)
            
            if fname.endswith('.csv'):
                with open(fname) as f:
                    rows=sum(1 for line in f)
                    print (filename +" - " + str(rows))
                    count = count + rows
            elif fname.endswith('.json'):
                jsondata = json.load(open(fname,encoding='utf-8'))
                rec = len(jsondata['data'])
                print (filename +" - " + str(rec))
                count = count + rec
            else:
                pass
    print("Totaal is " + str(count) + " records.")
                
                
except Exception as e:
    if hasattr(e, 'message'):
       
        print(e.message)
    else:
        print(e)