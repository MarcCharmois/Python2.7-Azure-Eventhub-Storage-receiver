# Python2.7 Event Hub Events Storage Receiver

## Description 
get captures from Azure Event Hub stored in Storage Blob

## How to use
### Azure configuration
Create an Azure Event Hub (choose standard sku for enabling capture)   
Create an Azure Storage Account if needed   
Create a blob container in the Storage Account if needed   
Set the capture to post event to the container  

### Local configuration
Download or clone this repo   
Create a Python virtual Env for Python 2.7   
pip install avro   
pip install azure.storage   
add a storageconfig.py file   
set 3 varaible in this file : storageAccountName, storageAccountKey, storageContainerName



