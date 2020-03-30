# Reads JSON file and extracts values from keys idfield and datafield and sends datafield values to TextRazor 
# to extract categories, entities and topics and stores the results in a csvfile

import pandas as pd
import json, os, textrazor
import numpy

# Global vars
NaN = numpy.nan
key = input('enter API key')
rootdir = input("rootdirectory van te extraheren bestanden: ")

textrazor.api_key = key

# TextRazor global vars
client = textrazor.TextRazor(extractors=["entities", "topics"])
# TextRazor init
client.set_language_override("dut")

# Other vars 
outfile_entities = input('outfile for entities')
outfile_topics = input('outfile for topics')

# Vars for the pandas dataframe and series
idfield = input('ID field: ')
datafield = input('Field that holds txt for extraction: ')
columns_topics=["at-id","label", "score" ,"wikipedia link" , "wikidata id"]
columns_entities = ["at-id", "id", "custom entity id" , "confidence score"  , "dbpedia types" ,     "freebase id" ,"wikidata id" ,"matched positions" , "matched words" ,"matched text","data" ,  "relevance score" ,"wikipedia link"]
    
# Functions
def store_topics(df, columns_topics):
    if len(topics) == 0 :                    
        emptyrow = {"at-id": x ,"label": NaN , "score" : NaN , "wikipedia link" : NaN , "wikidata id": NaN}
        dsempty = pd.Series( data=emptyrow, index = columns_topics)
        df= df.append(dsempty ,  ignore_index=True)
    else:
        dfdata = pd.DataFrame(columns=columns_topics)
        for topic in topics:
            tseen = set() 
            if topic not in tseen:
                data = {"at-id": x ,"label": topic.label , "score" : topic.score , "wikipedia link" : topic.wikipedia_link , "wikidata id": topic.wikidata_id}
                dsdata=pd.Series( data=data, index = columns_topics)
                dfdata = dfdata.append(dsdata ,  ignore_index=True)
                tseen.add(topic.label)
        df=df.append(dfdata)
    return(df)

def store_entities(df, columns_entities):
    if len(entities) == 0 :                    
        emptyrow = {"at-id": x , "id"  : NaN ,                  "custom entity id": NaN  ,                 "confidence score" : NaN , "dbpedia types": NaN ,                 "freebase id" : NaN ,"wikidata id": NaN ,                 "matched positions": NaN , "matched words" : NaN ,                 "matched text": NaN ,"data" : NaN , "relevance score": NaN ,                 "wikipedia link": NaN }
        dsempty = pd.Series( data=emptyrow, index = columns_entities)
        df= df.append(dsempty ,  ignore_index=True)
    else:
        dfdata = pd.DataFrame(columns=columns_entities)
        for entity in entities:
            eseen = set() 
            if entity not in eseen:
                data =  {"at-id": x, "id"  : entity.id ,                 "custom entity id": entity.custom_entity_id ,                 "confidence score" : entity.confidence_score , "dbpedia types": entity.dbpedia_types ,                 "freebase id" : entity.freebase_id ,"wikidata id": entity.wikidata_id ,                 "matched positions": entity.matched_positions , "matched words" : entity.matched_words ,                 "matched text": entity.matched_text ,"data" : entity.data , "relevance score": entity.relevance_score ,                 "wikipedia link": entity.wikipedia_link }
                dsdata=pd.Series( data=data, index = columns_entities)
                dfdata = dfdata.append(dsdata ,  ignore_index=True)
                eseen.add(entity.id)
        df=df.append(dfdata)
    return(df)

# START                

# Get the all the JSON files that need to be extracted
for dirpath, dirs, files in os.walk(rootdir): 
    for filename in files:
        #get the JSON source file
        fname = os.path.join(dirpath,filename)
        if fname.endswith('.json'):
            cname = fname.title().split(".", 1)[0] # this is for naming the CSV output file
            with open(fname, encoding='utf-8') as f:
                # get the JSON data
                jsondata = json.loads(f.read())
                datalist = jsondata["data"]
                df_topics = pd.DataFrame(columns=columns_topics)
                df_entities = pd.DataFrame(columns=columns_entities)

                for recorddict in datalist:
                    x= recorddict[idfield]
                    txt = recorddict[datafield]
                    response = client.analyze(txt)
                    topics = list(response.topics())
                    entities = list(response.entities())
                    df_topics=store_topics(df_topics,columns_topics)
                    df_entities=store_entities(df_entities,columns_entities)
    
    df_topics.to_csv(path_or_buf= cname + "_" + outfile_topics, mode='a', header = True, index = False )
    df_entities.to_csv(path_or_buf= cname + "_" + outfile_entities, mode='a', header = True, index = False )

    