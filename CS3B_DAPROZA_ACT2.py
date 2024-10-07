#Daproza, Abegail BSCS3B
#Python Activity that prinnts out info

FirstName= "Abegail"
MiddleName= "Antolin"
LastName= "Daproza"
Address= "Burgos Ilocos Sur"
Age= 23
FavNumberOne= 10
FaveNumberTwo= 11

print (FirstName, MiddleName, LastName, Address, Age, FavNumberOne, FaveNumberTwo)

#Collection
Animals= ["birds", "fish","dog"]
print (Animals)
print (Animals[1])

actor_one = "Ang gwapo gwapo ko diba? friend 'Makmak'"
actor_two = 'Thank you! "Macayan-puyot"'

print (actor_one, actor_two)
print (actor_two [6])

#get the length of actor 1, actor 2, address
#add two lengths of actor then minus the length of address
print (len(actor_one))
print (len(actor_two))
print (len(Address))
add = len(actor_one) + len(actor_two)
print (add)
sub= add - len(Address)
print (sub)
