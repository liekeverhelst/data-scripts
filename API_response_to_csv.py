# python 3.7 64 bit
# dit script maakt losse CSV bestanden van API responses

import requests, json
from pandas import DataFrame
import pandas as pd


url_short = input("Geef basisadres van de API: ")
urlpart = input( "Geef datagroep uit API: " )
headers = {"Accept": "application/json"}
key=input("geef API key: ")
user = input("geef userid: ")
csv_path = input("geef outputdirectory CVS bestand: ")
fieldname = input("geef naam van field: ")

try:

    url = url_short + urlpart + "/"
    print(url)
    res_file = csv_path +  urlpart + ".csv"
            
    f = open(res_file, "a")
            
    resp = requests.get(url, auth=(user, key), headers = headers)

    if resp.status_code == 200:
        # returns a dictionary with a single key 'data' and a list of dictionaries as value of that key.
        jsondata = json.loads(resp.content.decode('utf-8'))
        df = pd.DataFrame(data=jsondata['data'],columns=jsondata['data'][0].keys())
        
               
        df[fieldname].to_csv(path_or_buf = res_file, mode='a', header = False, index = False)
        
    else:
        print ("HTTP response code for " + url +  " is: " + str(resp.status_code)) 
    f.close()

except Exception as e:
    if hasattr(e, 'message'):
        print(e.message)
    else:
        print(e)
