import pandas

df = pandas.read_csv("hotels.csv",dtype={"id":str})

class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id,"name"].squeeze()
    def book(self):
        """Book a hotel by changing its availability"""
        availibility = df.loc[df["id"] == self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv",index=False)
    def available(self):
        availability =df.loc[df["id"] == self.hotel_id,"available"].squeeze()
        if availability == "yes":
            return  True
        else:
            return False

class ReservationTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel =hotel_object

    def generate(self):
        content =f"""
        Thank you for your reseervation!
        here are your bookung data:
        Name:{self.customer_name} 
        Hotel name:-{self.hotel.name}"""
        return content


class CreditCard:
    pass
print(df)
hotel_ID = input("Enter the id of the Hotel:")
hotel = Hotel(hotel_ID)


if hotel.available():
    credit_card = CreditCard(number="1234567890123456",expiration="12/26",holder="JOhn smith",cvc="123")
    if credit_card.validate():
        hotel.book()
        name = input("Enter your name:")
        reservation_ticket = ReservationTicket(customer_name=name,hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("There was a problem with your payment")

else:
    print("Hotel is not free.")
