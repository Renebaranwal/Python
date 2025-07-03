class Dog:
    breed = "bulldog"  # class variable

    def __init__(self):  # constructor method with correct syntax
        print("dog class")

d1 = Dog()
d2 = Dog()

print(d1.breed)
print(Dog.breed)  # Note: 'Dog', not 'dog' (case-sensitive)
print(d2.breed)
