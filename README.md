# Python2.7 Event Hub Events Storage Receiver

## Description 
get captures from Azure Event Hub stored in Storage Blob

## How to use
### Azure configuration
Create an Azure Event Hub (choose standard sku for enabling capture)   
Create an Azure Storage Account if needed   
Create a blob container in the Storage Account if needed   
Set the capture in the Event Hub to post event to the Storage Blob Container  

### Local configuration
Download or clone this repo   
Create a Python virtual Env for Python 2.7   
pip install avro   
pip install azure.storage   
Add a storageconfig.py file   
Set 3 varaiales in this file : storageAccountName, storageAccountKey, storageContainerName
