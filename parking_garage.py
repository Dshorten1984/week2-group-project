class Garage():  #daniel
    def __init__(self, tickets, parking = ['1','2','3','4','5','6','7','8','9','10'], current = {}):
        self.tickets = tickets
        self.parking = parking
        self.current = current
    
    def takeTicket(self):
        x = input("Enter yes to park DBD garage\n")
        if x.lower() == "yes":
            self.tickets.append('1')
            parking = input('Pick parking spot 1-10\n')
            self.parking.remove(parking)   #daniel


    


car = Garage([])
car.takeTicket()
print(car.parking)
print(car.tickets)


# chevy = Garage([])
# chevy.takeTicket()
# print(chevy.parking)
# print(chevy.tickets)