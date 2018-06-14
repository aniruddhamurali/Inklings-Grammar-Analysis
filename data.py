
links = []
dates = []
counts = []

with open('links.txt', 'r') as file:
    for line in file:
        links.append(line.strip())

with open('dates.txt', 'r') as file:
    for line in file:
        dates.append(line.strip())

with open('errorCounts.txt', 'r') as file:
    for line in file:
        counts.append(line.strip())

open('data.txt', 'w').close()
with open('data.txt', 'w') as file:
    for i in range(0, len(links)):
        file.write(links[i] + " " + dates[i] + " " + counts[i] + "\n")
