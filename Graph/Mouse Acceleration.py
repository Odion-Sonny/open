import time
import pyautogui
import matplotlib.pyplot as plt

# Set the time interval for capturing mouse position
interval = 0.1  # in seconds

# Initialize lists to store time, velocity, and acceleration values
times = []
velocities = []
accelerations = []

# Capture mouse position and calculate acceleration for a certain duration
duration = 5  # in seconds
start_time = time.time()
end_time = start_time + duration

# Capture initial mouse position
prev_x, prev_y = pyautogui.position()

while time.time() < end_time:
    # Capture mouse position
    x, y = pyautogui.position()

    # Record time and calculate velocity
    current_time = time.time() - start_time
    times.append(current_time)

    distance = ((x - prev_x) ** 2 + (y - prev_y) ** 2) ** 0.5
    velocity = distance / interval
    velocities.append(velocity)

    # Store current position as previous for the next iteration
    prev_x, prev_y = x, y

    # Wait for the specified interval before capturing the next position
    time.sleep(interval)

# Calculate accelerations based on velocities
for i in range(1, len(velocities)):
    delta_velocity = velocities[i] - velocities[i-1]
    delta_time = interval
    acceleration = delta_velocity / delta_time
    accelerations.append(acceleration)

# Ensure times and accelerations have the same length
if len(times) > len(accelerations):
    times = times[:-1]

# Plot the acceleration graph
plt.plot(times, accelerations)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (pixels/s^2)')
plt.title('Mouse Acceleration Over Time')
plt.show()
# hopefully i remember to make updates to this tomorrow
