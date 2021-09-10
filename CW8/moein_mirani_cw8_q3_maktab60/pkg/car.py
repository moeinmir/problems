class Car:


    def __init__(self,model,brand,details):
        self.model=model
        self.brand=brand
        self.details=details

    def get_brand(self):
        print(self.brand)

    def get_details(self):
        print(self.details)

    def get_model(self):
        print(self.model)
