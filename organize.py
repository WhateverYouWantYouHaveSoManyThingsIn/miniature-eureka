import os
import shutil

source="C:/Users/Aarav/Downloads"
destination="C:/Users/Aarav/Documents/DownloadedFiles/"

list_of_files=os.listdir(source)


for fileName in list_of_files:
    name,extention = os.path.splitext(fileName)
    if extention == '':
         continue
    
    #moving image files
    if extention in ['.jpg', '.GIF', '.png', '.jpeg', '.jfif']:
        path1=source+'/'+fileName
        path2=destination+'/'+"image_files"
        path3=destination+'/'+"image_files"+'/'+"fileName"

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path3)


            #moving document files
    if extention in ['.doc', '.pdf', '.docx']:
        path1=source+'/'+fileName
        path2=destination+'/'+"doc_files"
        path3=destination+'/'+"doc_files"+'/'+"fileName"

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)