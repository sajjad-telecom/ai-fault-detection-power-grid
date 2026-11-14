
import csv
import random

random.seed(42)

# Number of samples for each operating condition
samples_per_class = 250

data = []

# Generate normal operating data
for _ in range(samples_per_class):
    voltage = random.uniform(215, 235)
    current = random.uniform(10, 40)
    data.append([voltage, current, "Normal"])

# Generate overload data
for _ in range(samples_per_class):
    voltage = random.uniform(205, 225)
    current = random.uniform(65, 100)
    data.append([voltage, current, "Overload"])

# Generate short-circuit data
for _ in range(samples_per_class):
    voltage = random.uniform(20, 150)
    current = random.uniform(150, 400)
    data.append([voltage, current, "Short Circuit"])

# Generate ground-fault data
for _ in range(samples_per_class):
    voltage = random.uniform(150, 210)
    current = random.uniform(45, 90)
    data.append([voltage, current, "Ground Fault"])

# Shuffle dataset
random.shuffle(data)

# Save dataset as CSV
with open("electrical_fault_dataset.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Voltage", "Current", "Fault_Type"])
    writer.writerows(data)

print("Dataset created successfully!")
print("Total samples:", len(data))
