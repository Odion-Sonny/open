import time
import pyautogui
import matplotlib.pyplot as plt

# Set the time interval for capturing mouse position
interval = 0.1  # in seconds

# Initialize lists to store time and speed values
times = []
speeds = []

# Capture mouse position and calculate speed for a certain duration
duration = 5  # in seconds
start_time = time.time()
end_time = start_time + duration

while time.time() < end_time:
    # Capture mouse position
    x, y = pyautogui.position()

    # Record time and calculate speed
    current_time = time.time() - start_time
    times.append(current_time)

    if len(times) > 1:
        distance = ((x - prev_x) ** 2 + (y - prev_y) ** 2) ** 0.5
        speed = distance / interval
        speeds.append(speed)

    # Store current position as previous for the next iteration
    prev_x, prev_y = x, y

    # Wait for the specified interval before capturing the next position
    time.sleep(interval)

# Ensure times and speeds have the same length
if len(times) > len(speeds):
    times = times[:-1]

# Plot the speed graph
plt.plot(times, speeds)
plt.xlabel('Time (s)')
plt.ylabel('Speed (pixels/s)')
plt.title('Mouse Speed Over Time')
plt.show()
