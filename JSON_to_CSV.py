#python 3.7 64 bit
import os, json, pandas as pd

json_dir = input("Geef brondirectory - json: ")
csv_dir = input("Geef doeldirectory - csv: ")


try:
    for dirpath, dirs, files in os.walk(json_dir): 
        
        
        for filename in files:
            fname = os.path.join(dirpath,filename)
            part = os.path.splitext(filename)[0]
            
            csv_file = csv_dir + "//" + part + ".csv"
            
            if fname.endswith('.json'):
                jsondata = json.load(open(fname,encoding='utf-8'))
                df = pd.DataFrame(data=jsondata,columns=jsondata.keys())
                df.to_csv(path_or_buf = csv_file, mode='a', header = False, index = False)
                
                    
            else:
                pass



except Exception as e:
    if hasattr(e, 'message'):
        print(e.message)
    else:
        print(e)