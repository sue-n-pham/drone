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

# Note: The above code assumes that you have the necessary permissions and environment to run it.
# Make sure to run this code in an environment where you can safely control the drone.
# This code is for educational purposes and should be used responsibly.
# Ensure you have the necessary libraries installed
# and that your drone is compatible with the codrone_edu library.
