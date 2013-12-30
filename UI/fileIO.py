import os.path
def save(gate_group,wire_group):
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
    path = os.path.join('UI','Save','logic.save')
    f = open(path,'w')
    for i in print_list:
        s = ' '.join(i)
        f.write(s+'\n')
    f.close()
    del print_list

        
                
        
