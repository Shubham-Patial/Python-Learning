from random import randint
class Train:
    def __init__(self, train_No):
        self.train_No = train_No
    def book(self, start_loc, destination):
        print(f"The booking for train No {self.train_No} running from {start_loc} to {destination} is booked")
    def status(self, start_loc, destination):
        print(f"The booking for train No {self.train_No} running from {start_loc} to {destination} is on time")   
    def fare(self, start_loc, destination):
        print(f"The fare for train No {self.train_No} running from {start_loc} to {destination} is {randint(1000, 5000)}")

t = Train(4535)
t.book("Hoshiarpur", "Patiala")
t.status("Hoshiarpur", "Patiala")
t.fare("Hoshiarpur", "Patiala")