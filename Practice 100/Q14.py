H, M = map(int, input("Enter hour and minute in {12 30} format: ").split())

# Calculate angles
hour = 30 * H + 0.5 * M
minute = 6 * M

# Find difference
angle = abs(hour - minute)

print(f"Angle between hour and minute hand = {angle}°")