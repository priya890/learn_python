class Restaurant:

    def order(self, amount):
        print("Order Food %.2f" % amount)

    def play(self, is_paid):
        if is_paid:
            print("PLay games by adding game pass")
        else:
            print("Free games")

    def pay(self):
        print("Pay Check")


class Chilis(Restaurant):

    def order(self, amount, discount=0):
        print("Order Food %.2f with discount of %.2f" % (amount, discount))

    def play(self, is_paid, is_loyalty_first_signup=False):
        if is_loyalty_first_signup:
            print("Congratulations you now have unlocked games for FREE")
        elif is_paid:
            print("PLay games by adding game pass of Chilis Resto")
        else:
            print("Free games")

    def pay(self, donation_amount=0):
        print("Pay Check %.2f" % donation_amount)


class Applebees(Restaurant):

    def order(self, amount, discount=0.0):
        print("Order Food %.2f with discount of %.2f" % (amount, discount))

    def play(self, is_paid):
        if is_paid:
            print("PLay games by adding game pass of Chilis Resto")
        else:
            print("Free games")

    def pay(self):
        print("Pay Check")


# rest = Restaurant()
# print('_'*20)
# rest.order(12.34)
#
#
# chilis = Chilis()
# print('_'*20)
# chilis.order(2.30, 1)
# chilis.play(is_paid=False, is_loyalty_first_signup=True)

applebees = Applebees()
print('_'*20)
applebees.order(3.46)
applebees.order(3.46, 2.90)
# applebees.play(is_paid=True)

