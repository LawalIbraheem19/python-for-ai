class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        self.email = email
        if '@' not in self.email:
            self.errors.append(f"Inavlid email: {self.email}")
            return False
        return True
    def validate_age(self, age):
        self.age = age
        if self.age < 0 or self.age > 150:
            self.errors.append(f"Invalid age: {self.age}")
            return False
        return True
    def get_errors(self):
        return self.errors

# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']



class Animal:
    def __init__(self, name, is_pet = True):
        self.name = name
        self.is_pet = is_pet
    
class Dog(Animal):
    def __init__(self, name, breed, is_pet=True):
        super().__init__(name, is_pet)
        self.breed = breed

    def describe(self):
      return f"{self.name} is a breed of {self.breed}"



# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)      # True (inherited from Animal)
    