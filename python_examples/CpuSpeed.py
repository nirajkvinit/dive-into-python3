#!/usr/bin/python3
import time

print("Adding 1 million elements to a list")
list = []
begin = time.time()
for i in range(1000000):
    list.append(i)
end = time.time()
print("That took " + str(end - begin) + " seconds")
