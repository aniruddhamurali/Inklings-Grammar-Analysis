
dates = []

# Receive dates from the links
with open('links.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if "20" in line :
            index = line.find("20")
            dates.append(line[index:index + 10])

# Write the dates to a new file called "data.txt"
with open('dates.txt', 'w') as file:
    for date in dates:
        file.write(date + "\n")
