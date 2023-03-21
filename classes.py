# Devonne Le, CIS 440

class BookHotel:

    # def __init__(self, name, hotel, rooms, guests, addons=0, price=0.00):
    def __init__(self, name, hotel, rooms, guests, roomtype, destination, price=0.00):
        # self.name = name
        try:
            fname = name.split()[0]
            self.name = fname
        except:
            pass
        self.hotel = hotel
        self.rooms = rooms
        # self.addons = addons
        self.guests = guests
        self.roomtype = roomtype
        self.price = price
        self.destination = destination

    def custom_confirmation(self):
        return f'{self.name}, your booking is confirmed!'

    def order_details(self):
        return f'Booking: Staying at {self.hotel}, {self.rooms} room(s) with {self.guests} guest(s) with {self.roomtype}'

    def final_confirmation(self):
        return f'Booking by: {self.name}\n' \
               f'Destination: {self.destination}\n' \
               f'{self.hotel}\n' \
               f'{self.rooms} room(s)\n' \
               f' {self.guests} guest(s) with {self.roomtype}\n' \
               f'Total: ${self.price:.2f}'

    def __str__(self):
        return f'Booking by: {self.name}, Destination: {self.destination}, {self.hotel}, {self.rooms} room(s), {self.guests} guest(s) with {self.roomtype} ' \
               f'Total: ${self.price:.2f}'

