import os
import glob
import shutil
from os import path



filename3=glob.glob("C:/Users/marco/Videos/*")
mp4=['.mp4']
mov=['.mov']
wmw=['.wmw', '.WMW']
flv=['.flv']
mkw=['.mkv', '.MKV']
avi=['.avi']
mp4Location=("C:/Users/marco/Videos/mp4")
movLocation=("C:/Users/marco/Videos/mov")
wmwLocation=("C:/Users/marco/Videos/wmw")
flvLocation=("C:/Users/marco/Videos/flv")
mkwLocation=("C:/Users/marco/Videos/mkw")
aviLocation=("C:/Users/marco/Videos/avi")

for file in filename3:
    if os.path.splitext(file)[1] in mp4:
        if(path.exists(mp4Location)):
            shutil.move(file,mp4Location)
        else:
            os.mkdir(mp4Location)
            shutil.move(file,mp4Location)
    if os.path.splitext(file)[1] in mov:
        if(path.exists(movLocation)):
            shutil.move(file,movLocation)
        else:
            os.mkdir(movLocation)
            shutil.move(file,movLocation)
    if os.path.splitext(file)[1] in wmw:
        if(path.exists(wmwLocation)):
            shutil.move(file,wmwLocation)
        else:
            os.mkdir(wmwLocation)
            shutil.move(file,wmwLocation)
    if os.path.splitext(file)[1] in flv:
        if(path.exists(flvLocation)):
            shutil.move(file,flvLocation)
        else:
            os.mkdir(flvLocation)
            shutil.move(file,flvLocation)
    if os.path.splitext(file)[1] in mkw:
        if(path.exists(mkwLocation)):
            shutil.move(file,mkwLocation)
        else:
            os.mkdir(mkwLocation)
            shutil.move(file,mkwLocation)
    if os.path.splitext(file)[1] in avi:
        if(path.exists(aviLocation)):
            shutil.move(file,aviLocation)
        else:
            os.mkdir(aviLocation)
            shutil.move(file,aviLocation)
    
    

filename2=glob.glob("C:/Users/marco/Pictures/*")
png=['.png', '.PNG']
jpg=['.jpg', '.jpeg']
ico=['.ico']
pngLocation='C:/Users/marco/Pictures/png'
jpgLocation='C:/Users/marco/Pictures/jpg'
icoLocation='C:/Users/marco/Pictures/ico'

for file in filename2:
    if os.path.splitext(file)[1] in png:
        if(path.exists(pngLocation)):
            shutil.move(file,pngLocation)
        else:
            os.mkdir(pngLocation)
            shutil.move(file,pngLocation)
    if os.path.splitext(file)[1] in jpg:
        if(path.exists(jpgLocation)):
            shutil.move(file,jpgLocation)
        else:
            os.mkdir(jpgLocation)
            shutil.move(file,jpgLocation)
    if os.path.splitext(file)[1] in ico:
        if(path.exists(icoLocation)):
            shutil.move(file,icoLocation)
        else:
            os.mkdir(icoLocation)
            shutil.move(file,icoLocation)
            


filename=glob.glob("C:/Users/marco/Downloads/*")
documents=['.pdf','.docx','.doc','.txt', '.log']
media=['.jpeg','.jpg','.svg','.png','.PNG','.mp4','.mp3',]
setupFiles=['.exe','.msi']
compressedFiles=['.zip', '.rar', '.7z']
files=['.apk', '.jar', '.fdmdownload', '.vbox-extpack']
DocumentsLocation='C:/Users/marco/Downloads/documents'
mediaLocation='C:/Users/marco/Downloads/media'
setupFilesLocation='C:/Users/marco/Downloads/setupFiles'
compressedFilesLocation='C:/Users/marco/Downloads/compressedFiles'
FilesLocation='C:/Users/marco/Downloads/Files'

for file in filename:
    if os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file,DocumentsLocation)
    if os.path.splitext(file)[1] in media:
        if(path.exists(mediaLocation)):
            shutil.move(file,mediaLocation)
        else:
            os.mkdir(mediaLocation)
            shutil.move(file,mediaLocation)
    if os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file,setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file,compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
    if os.path.splitext(file)[1] in files:
        if(path.exists(FilesLocation)):
            shutil.move(file,FilesLocation)
        else:
            os.mkdir(FilesLocation)
            shutil.move(file,FilesLocation)