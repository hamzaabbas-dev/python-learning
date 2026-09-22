class Train:

    def __init__(self,name,seat,ticket):
        self.name = name
        self.seat = seat
        self.ticket = ticket


    def get_status(self):
     print(f"Available seats:  {self.seat}")

    def get_fare(self):
       print(f"Fare: {self.ticket}")

    def book_tickets(self):
        if self.seat > 0 :
            self.seat -= 1
            print("Seat reserved!")
        else:
          print("NO seats Available")

train = Train("Mansehra Express",3,500)

train.get_status()
train.get_fare()

train.book_tickets()
train.book_tickets()
train.book_tickets()
train.book_tickets()

train.get_status()
 