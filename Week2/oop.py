class person :

    def __init__(self, name) :
       self.name= name

    def invite(self):
      print('Welcome', self.name)

p1=person('Jon')
p2=person('sam')

p1.invite()
p2.invite()