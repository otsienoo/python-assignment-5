# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number}...")

    def check_battery(self):
        print(f"Battery life remaining: {self.battery_life} hours")

# Child Class: Smartphone with Camera (Inheritance and Polymorphism)
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_quality):
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality

    # Overriding the check_battery method to add additional functionality
    def check_battery(self):
        print(f"Battery life remaining: {self.battery_life} hours. Don't forget to charge before using the camera!")

    # New method specific to the subclass
    def take_picture(self):
        print(f"Taking a picture with {self.camera_quality} camera!")

# Create an object of the Smartphone class
my_phone = Smartphone("Samsung", "Galaxy S21", 24)
my_phone.make_call("123-456-7890")
my_phone.check_battery()

# Create an object of the SmartphoneWithCamera class
my_camera_phone = SmartphoneWithCamera("Apple", "iPhone 13", 18, "12MP")
my_camera_phone.make_call("0727653210")
my_camera_phone.check_battery()
my_camera_phone.take_picture()
