import threading
import time

# Taxi Class to hold taxi details, location, earnings and availability
class Taxi:
    def __init__(self, id, location='A'):
        self.id = id
        self.location = location
        self.earnings = 0
        self.available = True

class TaxiBookingSystem:
    def __init__(self):
        # Assisgning ID's To Taxi (4 Taxi)
        self.taxis = [Taxi(i) for i in range(1,5)]
        # Defining positions with their km apart from starting point
        self.position = {'A':0, 'B':15, 'C':30, 'D':45, 'E':60, 'F':75}
    
    def get_earnings(self):
        earnings = {taxi.id:taxi.earnings for taxi in self.taxis}
        return earnings
    
    def get_distance(self, start, end):
        # Returns distance in km between two locations A,B,C,D,E,F (Absolute value)
        return abs(self.position[end] - self.position[start])
    
    def get_fare(self, distance):
        if distance < 5:
            return 100
        else:
            return 100 + (distance-5)*10
        
    
    def get_nearest_taxi(self, pickup):
        near = None
        min_distance = float('inf')
        for taxi in self.taxis:
        # Check availability of taxi
            if taxi.available:
                # getting distance of taxis from the point
                distance = self.get_distance(taxi.location, pickup)
                # when taxi is near / with lower fee
                if (distance < min_distance) or (distance==min_distance and taxi.earnings< (near.earnings if near else float('inf'))):
                        near = taxi
                        min_distance = distance
        # Returning the nearest taxi id
        return near
    def change_status(self, taxi_id):
            taxi = next((i for i in self.taxis if i.id == taxi_id), None)
            if taxi:
                taxi.available = True
                print(f"Taxi {taxi_id} is Now Available\n")

    def book_taxi(self, pickup, drop):
        # Check if any taxi is available
        taxi = self.get_nearest_taxi(pickup)
        if taxi is None:
           print("Oops! Booking is Rejected, No Taxi is Available at the moment\n")
           return
        distance = self.get_distance(pickup, drop)
        fare = self.get_fare(distance)
        taxi.earnings += fare
        taxi.location = drop
        taxi.available = False
        # print(taxi)
        print(f"Your Booking has been Successful, Your Taxi ID is {taxi.id}, Your Fare is {fare}\n")
        threading.Timer(15, self.change_status, [taxi.id]).start()

        

booking = TaxiBookingSystem()

booking.book_taxi('A', 'D')  # Booking 1
time.sleep(3)
booking.book_taxi('A', 'C')  # Booking 2
time.sleep(3)
booking.book_taxi('A', 'B')  # Booking 3
time.sleep(3)
booking.book_taxi('B', 'D')  # Booking 4
print(booking.get_earnings())
time.sleep(3)
booking.book_taxi('D', 'E')  # Booking 5 (this may get rejected if no taxis are free)
time.sleep(4)
booking.book_taxi('D', 'E')
time.sleep(10)
# booking.change_status(1)  # Changing the availability of Taxi id 1 manually
booking.book_taxi('E', 'F')
time.sleep(3)
# booking.change_status(2)
# booking.change_status(3) 
booking.book_taxi('B', 'D')
time.sleep(3)
booking.book_taxi('C', 'E')
print(booking.get_earnings())


