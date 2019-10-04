# Python2.7 Event Hub Events Storage Receiver

## Description 
Gets the events of an Azure Event Hub captured and stored in Storage Blob   
This a rework of the <a href="https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-capture-python">original Microsoft version: Read captured data from Python app - Azure Event Hubs | Microsoft Docs</a>

## How to use
### Azure configuration
Create an Azure Event Hub (choose standard sku for enabling capture)   
Create an Azure Storage Account if needed   
Create a blob container in the Storage Account if needed   
Set the capture in the Event Hub to post events to the Storage Blob Container  

### Local configuration
Download or clone this repo   
Create a Python virtual Env for Python 2.7   
pip install avro   
pip install azure.storage   
Add a storageconfig.py file   
Set 3 variables in this file : storageAccountName, storageAccountKey, storageContainerName
