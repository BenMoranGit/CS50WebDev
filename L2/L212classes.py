class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): #If not == 0 pythonic way of writing it
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(2)

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight succesfully.")
    else:
        print(f"No seat available for {person}")