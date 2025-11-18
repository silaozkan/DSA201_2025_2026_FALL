#from person import Person
import person as p

p1 = p.Person(id="1111", myName="Ayse")
print(p1.id)
print(p1.age)
print(p1.name)
print("==============")
p2 = p.Person("2222", "Ali", 25)
#p2.age = 24
p2.changeAge(24)
print(p2.id)
#print(p2.age)
print(p2.getAge())
print(p2.name)
print("================")
print(p1)
print(p2)

society = []
society.append(p1)
society.append(p2)
print(society)