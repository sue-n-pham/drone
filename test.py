from codrone_edu.drone import *

print("Hello, world!")

drone = Drone()
drone.pair()

# Make the drone lift off
drone.takeoff()

# Wait for a few seconds (optional)
drone.hover(2)  # Hover for 2 seconds

# Land the drone safely
drone.land()

# Close the connection to the drone
drone.close()

