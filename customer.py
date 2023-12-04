class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        # Return a unique list of all restaurants this customer has reviewed
        pass

    def add_review(self, restaurant, rating):
        # Given a restaurant object and a star rating, create a new review
        # and associate it with this customer and the given restaurant
        pass

    def num_reviews(self):
        # Return the total number of reviews authored by this customer
        pass

    @classmethod
    def find_by_name(cls, name):
        # Given a full name, return the first customer whose full name matches
        pass

    @classmethod
    def find_all_by_given_name(cls, name):
        # Given a given name, return a list containing all customers with that given name
        pass
