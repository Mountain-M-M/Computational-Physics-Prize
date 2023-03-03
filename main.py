# Importing Files

from Planet import Planet
from Sun import Sun
from LatitudeBelt import LatitudeBelt


# Global Variables

number_of_latitude_belts = 10000
array_of_latitude_belts = []
albedo = 0.3
stefan = 5.670e-8
radius_of_planet = 6.4e6
distance_between_planet_and_sun = 1.50e11
luminosity = 3.8e26

# Instantiating Objects

planet = Planet(radius_of_planet, number_of_latitude_belts)
sun = Sun(distance_between_planet_and_sun, luminosity)

for index in range(number_of_latitude_belts):
  latitude_belt = LatitudeBelt(index, albedo, 288, 0.6, 0)
  latitude_belt.area = latitude_belt.calculate_area(index, number_of_latitude_belts, planet.radius)
  array_of_latitude_belts.append(latitude_belt)
  
# Calculating Energy Input

index = 0
for latitude_belt in array_of_latitude_belts:
  latitude_belt.power = latitude_belt.calculate_power(planet.radius, sun.luminosity, sun.distance_from_planet, number_of_latitude_belts)
  index += 1

# Calculating Emitted Energy

for latitude_belt in array_of_latitude_belts:
  latitude_belt.energy_emitted = latitude_belt.calculate_energy_emitted(stefan)

testtotal = 0
for l in array_of_latitude_belts:
  testtotal += l.power

print("total", testtotal)








# # Define the function that will update the energy absorbed label
# def update_energy(val):
#     energy = float(val) ** 2
#     energy_label.config(text=f"Energy Absorbed: {energy}")

# # Create the Tkinter window
# window = tk.Tk()
# window.title("Albedo Dashboard")

# # Create the albedo slider and label
# albedo_label = tk.Label(window, text="Albedo:")
# albedo_label.pack(side="left")
# albedo_slider = tk.Scale(window, from_=0, to=10, resolution=1, orient="horizontal", command=update_energy)
# albedo_slider.pack(side="left")
# energy_label = tk.Label(window, text="Energy Absorbed: 0")
# energy_label.pack(side="left")

# # Run the Tkinter event loop
# window.mainloop()
