import os,sys
sys.path.append("..")
from Module.Gate import Wire
from Module import Logic_Gates,input_module,output_module

def save(path,gate_group,wire_group):
    if len(gate_group) == 0:
        f = open(path,'w')
        f.write('E')
        f.close()
        return False
        
    save_list = []
    for g in gate_group:
        save_list.append(g)

    print_list = []
    #Add Gate Info
    for g in save_list:
        row = [str(g.gate_type),str(g.rect.x),str(g.rect.y)]
        if g.port[0].status:
            row.append('1')
        else:
            row.append('0')
        
        i = 0
        for p in g.port:
            if not(p.multi):
                i += 1
                
        row.append(str(i))
        for j in range(i):
            row.append('n')
            row.append('n')

        print_list.append(row)
        del row

    #Add Wire Info
    for w in wire_group:
        modu_s = save_list.index(w.start_module)
        port_s = w.start_port
        
        modu_e = save_list.index(w.end_module)
        port_e = w.end_port

        print_list[modu_e][(port_e*2+3)] = str(modu_s)
        print_list[modu_e][(port_e*2+4)] = str(port_s)
            
        
    del save_list
    #Write on the file
    f = open(path,'w')
    for i in print_list:
        s = ' '.join(i)
        f.write(s+'\n')
    f.close()
    del print_list

def load(path,gate_group,wire_group):
    gate_group.empty()
    wire_group.empty()
    f = open(path,'r')
    read_list = f.readlines()
    load_list = []
    f.close()
    #Convert string in the file to array
    for i in range(len(read_list)):
        
        li = read_list[i].rstrip().split(" ")
        for j in range(len(li)):
            if li[j] != 'n':
                li[j] = int(li[j])
        read_list[i] = li

    for i in read_list:
        module = get_module(i[0])
        module.rect.x = i[1]
        module.rect.y = i[2]
        if i[0] == 8:
            if i[3] == 1:
                module.status = True
        load_list.append(module)
        gate_group.add(module)

    for i in range(len(read_list)):
        for j in range(read_list[i][4]):
            j += 1
            mod_indx = read_list[i][(j*2+3)]
            if mod_indx != 'n':
                port = read_list[i][(j*2+4)]
                new_wire = Wire(load_list[i],j)
                wire_group.add(new_wire)
                new_wire.connect_module(load_list[mod_indx],port)
                new_wire.get_graphic_info()
                new_wire.draw_image()
                
    del read_list
    del load_list
            
def get_module(module_type):
    if module_type == 1:
        new_module = Logic_Gates.AND_Gate()
    elif module_type == 2:
        new_module = Logic_Gates.OR_Gate()
    elif module_type == 3:
        new_module = Logic_Gates.XOR_Gate()
    elif module_type == 4:
        new_module = Logic_Gates.NAND_Gate()
    elif module_type == 5:
        new_module = Logic_Gates.NOR_Gate()
    elif module_type == 6:
        new_module = Logic_Gates.XNOR_Gate()
    elif module_type == 7:
        new_module = Logic_Gates.NOT_Gate()
    elif module_type == 8:
        new_module = input_module.Input()
    elif module_type == 9:
        new_module = input_module.Button()
    elif module_type == 10:
        new_module = output_module.Output()
    elif module_type == 11:
        new_module = output_module.Hexdisplay()
        
    return new_module

def check_file():
    #check /Temp
    path = os.path.join('UI','Temp')
    if not(os.path.exists(path)):
        os.makedirs(path)
    #chek /Save
    path = os.path.join('UI','Save')
    if not(os.path.exists(path)):
        os.makedirs(path)
    for i in range(9):
        path = os.path.join('UI','Save',('logic%d.save'% i))
        if not(os.path.exists(path)):
            f = open(path,'w')
            f.write('E')
            f.close()
        else:
            f = open(path,'r')
            image_path = os.path.join('UI','Save',('shot%d.png'% i))
            if f.read(1) == '' or not(os.path.exists(image_path)):
                f.close()
                f = open(path,'w')
                f.write('E')
            f.close()
    
        

        
                
        
