import human

a = human.Human("David",48,160)
print(a.name,'bmi:',a.bmi())

b=human.Woman("Jenny",55,150,30,36,34)
print(b.name,'bmi:',b.bmi())
b.BWH()

c=human.Man('Alex',24,104,True)
print(c.name,'bmi:',c.bmi())
c.description()
