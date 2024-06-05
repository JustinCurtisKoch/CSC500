# Creates the initial class stereo-speakers
class StereoSpeakers:
    def __init__(self, make, model, year, color, cost):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.__cost = cost

    def display_info(self):
        print(f"The {self.make} {self.model}, circa {self.year} in {self.color}")

# Creates instances of the stereo-speakers class
current_speakers = StereoSpeakers("JBL", "4130", 1970, "Walnut", "N/A")
next_speakers = StereoSpeakers("Focal", "Aria EVO", 2023, "Paino Black", 3200)
dream_speakers = StereoSpeakers("Sonus Faber", "Amati", 2020, "Ash", 36000)

# Calling the instances
current_speakers.display_info()
next_speakers.display_info()

# Hiding an attribute
print(dream_speakers.__cost)



