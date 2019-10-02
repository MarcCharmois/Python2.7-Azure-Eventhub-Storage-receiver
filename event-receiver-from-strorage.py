import os
import string
import json
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from azure.storage.blob import BlockBlobService
import storageconfig as cfg

def processBlob(filename):
    reader = DataFileReader(open(filename, 'rb'), DatumReader())
    dict = {}
    readingNb = 0
    for reading in reader:
        readingNb +=1
        try:
            parsed_json = json.loads(reading["Body"])
            #print parsed_json 
            print "-----------------------------"
            print "id:"
            print parsed_json[0]["id"]
            #print parsed_json[0]
            if not 'id' in parsed_json[0]:
                print "no id found..."
                return
            if not dict.has_key(parsed_json[0]['id']):
                list = [parsed_json[0]]
                dict[parsed_json[0]['id']] = list
            else:
                list = dict[parsed_json[0]['id']]
                list.append(parsed_json[0])
            print "id:"
            print dict[parsed_json[0]['id']][0]["id"]   
            print "eventTime:"
            print dict[parsed_json[0]['id']][0]["eventTime"]  
            print "eventType:"
            print dict[parsed_json[0]['id']][0]["eventType"]  
            print "resourceUri:"
            print dict[parsed_json[0]['id']][0]["data"]["resourceUri"]
            print "operationName:"
            print dict[parsed_json[0]['id']][0]["data"]["operationName"] 
            print "resourceProvider:"
            print dict[parsed_json[0]['id']][0]["data"]["resourceProvider"]   
            print "status:"
            print dict[parsed_json[0]['id']][0]["data"]["status"]  
            print "subject:"
            print dict[parsed_json[0]['id']][0]["subject"]  
        except:
            print "exception in converting blob to json"
    reader.close()
    print readingNb
    '''
    for device in dict.keys():
        deviceFile = open(device + '.csv', "a")
        for r in dict[device]:
            print r
            deviceFile.write(", ".join([str(r[x]) for x in r.keys()])+'\n')
    '''
def startProcessing(accountName, key, container):
    print 'Processor started using path: ' + os.getcwd()
    block_blob_service = BlockBlobService(account_name=accountName, account_key=key)
    generator = block_blob_service.list_blobs(container)
    blobNb=0
    for blob in generator:
        blobNb+=1
        #content_length == 508 is an empty file, so only process content_length > 508 (skip empty files)
        if blob.properties.content_length > 508:
            print('Downloaded a non empty blob: ' + blob.name)
            cleanName = string.replace(blob.name, '/', '_')
            block_blob_service.get_blob_to_path(container, blob.name, cleanName)
            processBlob(cleanName)
            os.remove(cleanName)
        block_blob_service.delete_blob(container, blob.name)
    print "blob nb:"
    print blobNb
startProcessing(cfg.storageAccountName, cfg.storageAccountKey, cfg.storageContainerName)