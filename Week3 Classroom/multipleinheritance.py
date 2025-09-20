class employee:
    def __init__(self,name):
        self.name=name

class automationskills:
    def writescript(self):
        print("Writing Selenium Scripts")

class automationtester(employee,automationskills):
    def __init__(self, name):
        employee.__init__(self,name)
      
       

    def executescript(self):
        print("Execute Scripts")

at1=automationtester("hari")
at1.writescript()
at1.executescript()
