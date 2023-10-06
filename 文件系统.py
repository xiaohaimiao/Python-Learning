import os
import shutil

def findFile(path, keyword, mode = "FilenameAndExt"):
    modes = ["FilenameAndExt".lower(), "Filename".lower(), "Extension".lower()]
    modeLower = mode.lower()
    if( modeLower not in modes): 
        mode = "FilenameAndExt"

    for folder, dirs, files in os.walk(path):
        print("Folder:", folder)
        print("\tSubFolders:", dirs)
      
        for file in files:
            a = os.path.splitext(file)  # 拆成名字和后缀，得到一个list
            #print("file", file, a)
            text = file
            if (modeLower == modes[0]):
                text = file
            elif(modeLower == modes[1]):
                text = a[0]
            elif(modeLower == modes[2]):
                text = a[1]
                
            if keyword in text:
                print("找到文件：", file, a)
                return (True, os.path.join(folder, file))
    return (False, "")

path = r'E:\_软件备份_\photo\家庭相册\家庭合影-20190915'  # 目标文件所在路径
#path = r'E:\_软件备份_\photo\家庭相册'  # 目标文件所在路径
key_word = '5760' # 需要查找的文件名中包含的关键词
new_name = '222'  # 替换后的文件名
foundFile = findFile(path, key_word, "FilenameAndExt")
if (foundFile[0]):
    print(foundFile[1])
    newFilename = foundFile[1] + ".t"
    shutil.copy(foundFile[1], newFilename)
    #os.rename(newFilename, newFilename + ".tt") #注意要更名的文件、更名后的文件是否已经存在
    #os.remove(newFilename + ".tt") #注意要删除的文件是否存在
    