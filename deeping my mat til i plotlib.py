import matplotlib as plt#
import csv




with open("programming_4_college_dsd1/deepweapons.csv","r") as deep:
    file = csv.reader(deep)
    x = deep["Damage"]
    y = deep["Swing Speed"]
    plt.style('classic')
    plt.scatter(x,y)
    plt.show