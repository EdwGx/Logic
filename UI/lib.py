def get_distance(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

def get_dis_nsqrt(pos1,pos2):
    return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2

def in_radius(pos1,pos2):
    ax2 = (pos1[0]-pos2[0])**2
    if (ax2 <= 1764) :
        by2 = (pos1[1]-pos2[1])**2
        if (by2 <= 1764) :
            dis = ax2 + by2
            if (dis <= 1764):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
                

def snap_to_port(gates_group,wire,pos):
    #Get wire info
    if wire.end_module == None:
        find_end = True
    else:
        find_end = False

    closest_gate = None
    closest_port = None
    closest_distance = 100 #10^2
    #Find the closest port
    for gate in gates_group:
        if in_radius(pos,(gate.rect.centerx,gate.rect.centery)):
            if find_end and gate != wire.start_module:
                dis = get_dis_nsqrt(pos,gate.port_pos(1))
                if dis < closest_distance and gate.port[1].is_enough_wire():
                    closest_gate = gate
                    closest_port = 1
                    closest_distance = dis

                if gate.dual_in:
                    dis = get_dis_nsqrt(pos,gate.port_pos(2))
                    if dis < closest_distance and gate.port[2].is_enough_wire():
                        closest_gate = gate
                        closest_port = 2
                        closest_distance = dis
                        
            elif find_end == False and gate != wire.end_module:
                dis = get_dis_nsqrt(pos,gate.port_pos(0))
                if dis < closest_distance and gate.port[0].is_enough_wire():
                    closest_gate = gate
                    closest_port = 0
                    closest_distance = dis
    #Got the closest port
    if closest_gate == None:
        wire.kill()
    else:
        #Tell wire the port
        wire.connect_module(closest_gate,closest_port)

def select_sprite (gates_group,pos,controller):
    select_sprites = gates_group.get_sprites_at(pos)
    number = len(select_sprites)-1
    if number >= 0:
        module = select_sprites[number]
        port_number = module.number_of_ports()
        for i in range(port_number):
            dis = get_dis_nsqrt(pos,module.port_pos(i))
            if dis < 50 and module.port[i].conn_wire:
                controller.click_on_port(module,i)
                return True
        rel_pos = (pos[0] - module.rect.x,pos[1] - module.rect.y)
        controller.click_on_module(module,rel_pos)
        return True
    return False
