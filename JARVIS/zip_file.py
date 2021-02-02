# importing required modules 
from zipfile import ZipFile 
from pyttsx3 import speak
def locationerrorfixer(address):
    address=str(address)
    return address.replace('\\','\\\\')
print('Enter the location of zip file')
speak('Enter the location of zip file')    
# specifying the zip file name 
file_name = str(input())
#file_name = locationerrorfixer(file_name)  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    speak('Extracting all the files now...') 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!') 
    speak('Done sir.You can check it in same folder where the zip file is saved')