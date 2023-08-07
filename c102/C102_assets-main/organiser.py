import os, shutil;
from_dir='C102_assets-main';
to_dir='C102_assets-main/files';

listOfFiles=os.listdir(from_dir);
print(listOfFiles)


for file in listOfFiles:
    name, ext=os.path.splitext(file);
    print (name,ext);
    if ext=='':
        continue
    if ext in['.gif','.png','.jfif','.jpg']:
        path1= from_dir + '/' + file
        path2= to_dir + '/' + 'files' + '/' + ext
        path3= to_dir + '/' + 'files' + '/' + ext +'/' + file

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)