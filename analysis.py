# Equation: y = 3.52074 - 0.00066x
# r = -0.31257
# r^2 = 0.09770

import math
from datetime import date

def diff_dates (d1, d2):
    return abs(d2-d1).days

def format_date(date):
    date = date.split('-')
    return int(date[0]), int(date[1]), int(date[2])

counts = []
days = []
d1 = date(2008,8,25) # Date of first article
firstLine = False

with open('data2.txt', 'r') as file:
    for line in file:
        if firstLine == False:
            firstLine = True
            continue
        line = line.strip().split('\t')
        days.append(diff_dates(d1, date(format_date(line[1])[0],
                                        format_date(line[1])[1],
                                        format_date(line[1])[2])))
        counts.append(int(line[2]))
        
x = days
y = counts
yInt = None
s = None


def mean(ints):
    return sum(ints)/len(ints)

def stdev(ints):
    diff = 0
    average = mean(ints)
    for n in ints:
        diff += (n - average)**2
    return math.sqrt(diff/(len(ints)-1))

def zscore(x,ints):
    average = mean(ints)
    sd = stdev(ints)
    return (x-average)/sd

def r(xInts, yInts):
    zScoreTotal = 0
    for i in range(0,len(xInts)):
        zScoreTotal += zscore(xInts[i], xInts) * zscore(yInts[i], yInts)
    r = zScoreTotal/(len(xInts)-1)
    print("r = " + str(r))
    print("r^2 = " + str(r**2))
    return r

def equation(xInts, yInts):
    slope = r(xInts,yInts) * stdev(yInts)/stdev(xInts)
    yIntercept = mean(yInts) - slope*mean(xInts)
    print("y = " + str(yIntercept) + " + " + str(slope) + "x")
    s = slope
    yInt = yIntercept

equation(x, y)

