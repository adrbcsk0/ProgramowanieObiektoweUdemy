# class Transportation:
#     def transport_people(self):
#         pass
#
#     def display_info(self):
#         pass
#
# class Tram(Transportation):
#     def __init__(self, tram_type, capacity, max_speed):
#         self.tram_type = tram_type
#         self.capacity = capacity
#         self.max_speed = max_speed
#
#     def transport_people(self):
#         print(f"{} transported {self.capacity} people")
#
# class Bus(Transportation):
#     def __init__(self, brand, capacity, color):
#         self.brand = brand
#         self.capacity = capacity
#         self.color = color
#
# class MercedesBus(Bus):
#     def __init__(self, air_cond, *args, **kwargs):
#         self.air_cond = air_cond
#         super().__init__(*args, **kwargs)