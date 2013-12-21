from Gate import logicGate
import Logic

class AND_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,1)
        
    def update(self):
        self.port[0].update_status(
            Logic.ANDG(self.port[1].status,self.port[2].status))

class OR_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,2)
        
    def update(self):
        self.port[0].update_status(
            Logic.ORG(self.port[1].status,self.port[2].status))

class NOT_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,7)
        
    def update(self):
        print(Logic.NOTG(self.port[1].status))
        self.port[0].update_status(Logic.NOTG(self.port[1].status))


