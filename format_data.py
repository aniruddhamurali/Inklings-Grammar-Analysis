from datetime import date

def diff_dates (d1, d2):
    return abs(d2-d1).days

def format_date(date):
    i1 = 0
    i2 = 0
    for i in range(0,len(date)):
        if date[i] == "/":
            if i1 == 0:
                i1 = i
            else:
                i2 = i
                
    month = date[0:i1]
    day = date[i1+1:i2]
    year = "20" + date[i2+1:]
    if len(month) == 1: month = "0" + month
    if len(day) == 1: day = "0" + day
    return year + "-" + month + "-" + day
    
links = []
dates = []
counts = []
d1 = date(2008,8,25) # Date of first article - would be the y-intercept

with open('data.txt', 'r') as file:
    for line in file:
        line = line.strip().split('\t')
        links.append(line[0])
        dates.append(format_date(line[1]))
        counts.append(line[2])

open('data2.txt', 'w').close()
with open('data2.txt', 'w') as file:
    for i in range(0, len(links)):
        file.write(links[i] + "\t" + dates[i] + "\t" + counts[i] + "\n")
    

#print(dates[0])
