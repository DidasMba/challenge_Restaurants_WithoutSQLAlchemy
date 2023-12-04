class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        # Return a list of all reviews for this restaurant
        pass

    def customers(self):
        # Return a unique list of all customers who have reviewed this restaurant
        pass

    def average_star_rating(self):
        # Return the average star rating for this restaurant based on its reviews
        pass


