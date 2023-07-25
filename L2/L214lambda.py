#We can see nexting of lists within data structures
people = [     
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#def f(person):
#    return person["house"]

people.sort(key=lambda person: person["name"]) #Shortcut to funtion using lambda, same as commented out area

print(people)

