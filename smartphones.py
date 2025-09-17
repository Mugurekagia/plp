class SmartDevice:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self._battery_capacity = battery_capacity
        self.battery_level = 100
        
    def charge(self, amount):
            self.battery_level = min(100, self.battery_level + amount)
            print(f"{self.model} charged to {self.battery_level}%.")
            
    def use_battery(self, amount):
            if self.battery_level - amount >=0:
                self.battery_level -= amount
                print(f"{self.model} battery now at {self.battery_level}%.")
            else:
                print(f"{self.model} battery too low! Please charge.")
                
class Smartphone(SmartDevice):
    def __init__(self, brand, model, battery_capacity, os):
        super().__init__(brand, model, battery_capacity)
        self.os = os
        self.apps = []
        
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed on {self.model}.")
        
    def use_battery(self, amount):
        print(f"Using {self.model} for normal tasks..")
        super().use_battery(amount)
        
class GamingPhone( Smartphone):
    def __init__(self, brand, model, battery_capacity, os, cooling_system):
        super().__init__(brand, model, battery_capacity, os)
        self.cooling_system = cooling_system
        
    def use_battery(self, amount):
        print(f" Using {self.model} for heavy gaming..")
        super().use_battery(amount * 2)
        
phone1 = Smartphone("Samsung", "Galaxy S24", 5000, "Android")
phone2 = GamingPhone("Asus", "ROG Phone 8", 6000, "Android", "Liquid Cooling")
        
phone1.install_app("WhatsApp")
phone1.use_battery(20)
        
phone2.install_app("PUBG Mobile")
phone2.use_battery(20) 
            
            
        
        
        
             
                        
                
        