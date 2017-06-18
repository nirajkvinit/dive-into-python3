#!/usr/bin/python3

tempF = input("Enter fahrenheit: ")
tempC = (float(tempF) - 32) / 180*100
tempK = tempC + 273.15

print("tempF: " + str(float(tempF)))
print("tempC: " + str(float(tempC)))
print("tempK: " + str(float(tempK)))
