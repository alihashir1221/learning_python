# Distance in kilometers
distance_km = 10.0

# Time in minutes and seconds
time_minutes = 43
time_seconds = 30

# Convert time to total minutes
total_minutes = time_minutes + time_seconds / 60

# Convert distance to miles (1 kilometer = 0.621371 miles)
distance_miles = distance_km * 0.621371

# Calculate average time per mile
average_time_per_mile = total_minutes / distance_miles

# Calculate average speed in miles per hour
average_speed_mph = distance_miles / (total_minutes / 60)

# Print results
print(f"Average Time per Mile: {average_time_per_mile:.2f} minutes/mile")
print(f"Average Speed: {average_speed_mph:.2f} miles/hour")
