# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 19:36:58 2019

@author: YASHA
"""
import os, shutil
print(os.getcwd())
print(os.listdir())
print(os.chdir('E:\\theme dark'))
print(os.getcwd())
print(os.chdir('C:\\Users\\YASHA\\.spyder-py3'))
print(os.getcwd())
folder_name = (r'E:\Newfolderyash')
print(folder_name)

My program is to filter the file in the folder and same type of file in one
folder
dict_exten = {'audio_exten' : ('mp3','wav','m4a'),
               'video_exten' : ('mp4','mkv','3gp','flv','avi','mpge','MKV'),
               'document_exten' : ('dotm','txt','docx','xlsb'),
               'pictures_exten' : ('img','jpg','png')}

folderpath = input("Enter the folder name:")


def file_finder(folder_path, file_exten):
    files = []
    
    for file in os.listdir(folder_path):
        for exten in file_exten:
            if file.endswith(exten):
               files.append(file)
    return files

for file_exten, exten_pulp in dict_exten.items():
    folder_name = file_exten.split('_')[0] 
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for items in file_finder(folderpath, exten_pulp):
        items_path = os.path.join(folderpath, items)
        items_new_path = os.path.join(folder_path, items)
        shutil.move(items_path,items_new_path)

