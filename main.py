from customer import Customer
from restaurant import Restaurant
from review import Review

# Create sample instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = Restaurant("Great Food Place")
restaurant2 = Restaurant("Awesome Eats")

# Add reviews
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Test methods
print(customer1.full_name())  # Should print "John Doe"
print(customer2.restaurants())  # Should print a list of restaurants reviewed by customer2
print(restaurant1.average_star_rating())  # Should print the average star rating for restaurant1

