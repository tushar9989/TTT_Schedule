import csv
from collections import defaultdict
from QueueElement import QueueElement
from MyHeap import MyHeap

writerToTalesMap = defaultdict(list)
with open('data.csv', 'rb') as csvFile:
    spamReader = csv.reader(csvFile)
    for row in spamReader:
        writerToTalesMap[row[0]].append(row[1])

elements = []
heap = MyHeap()
for key, value in writerToTalesMap.iteritems():
    elements.append(QueueElement(key, value, 10))
    heap.push(QueueElement(key, value, 10))

for element in elements:
    #print str(element)
    print str(heap.pop())
