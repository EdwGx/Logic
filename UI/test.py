import os.path,sys

def load():
    path = os.path.join('Save','logic.save')
    f = open(path,'r')
    read_list = f.readlines()
    load_list = []
    f.close()
    #Convert string in the file to array
    for i in range(len(read_list)):
        li = read_list[i].split(" ")
        print(li)
        for j in range(len(li)):
            print li[j]
            #if li[j] != 'n':
                #li[j] = int(li[j])
        read_list[i] = li

load()
