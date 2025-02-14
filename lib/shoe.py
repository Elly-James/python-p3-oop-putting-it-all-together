#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size= 9):
     
        if isinstance(brand, str) and 1 <= len(brand) <= 25:
            self._brand = brand
        else:
            print("Brand must be string between 1 and 100 characters.")
            self._brand = "Unknown"

        if isinstance(size, int) and size > 0:
            self._size = size
        else:
            print("size must be an integer")
            self._size = 6

        self.condition= "Used"

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str) and 1 <= len(brand) <= 25:
            self._brand = brand
        else:
             print("Brand must be string between 1 and 25 characters.")

    def get_size(self):
        return self._size

    def set_size(self, size):
       if isinstance(size, int) and size > 0:
            self._size = size
       else:
            print("size must be an integer")
            self.size = 6

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

   
    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)

shoe = Shoe()
print(shoe.brand)  
print(shoe.size)  

shoe.brand = "Air Force"
shoe.size = 7
print(shoe.brand)
print(shoe.size)

shoe.brand = "Nike"
shoe.size = -3
print(shoe.brand)
print(shoe.size)
