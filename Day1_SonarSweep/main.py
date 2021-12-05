# Day 1 Sonar Sweep

# Read all file data into a list and convert from strings to int
depth_measurements = open("input.txt", 'r').readlines()
depth_measurements = list(map(int, depth_measurements))

measurement_count = len(depth_measurements)

# Part 1
increase_count = 0
for i in range(measurement_count-1):
    delta = depth_measurements[i+1] - depth_measurements[i]
    if delta > 0:
        increase_count = increase_count + 1

# Print Answer
print(increase_count)

# Part 2 - Three Measurement Window Increase Count
three_measurement_window_sums = []
for m in range(measurement_count):
    if m < (measurement_count - 2):
        window_sum = depth_measurements[m] + depth_measurements[m+1] + depth_measurements[m+2]
        three_measurement_window_sums.append(window_sum)
    else:
        break

window_increase_count = 0
for i in range(len(three_measurement_window_sums)-1):
    delta = three_measurement_window_sums[i+1] - three_measurement_window_sums[i]
    if delta > 0:
        window_increase_count = window_increase_count + 1

print(window_increase_count)

