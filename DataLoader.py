import csv
import sys
from collections import Set, OrderedDict, defaultdict
from QueueElement import QueueElement
from HeapWrapper import HeapWrapper

def calculateLengthToPercentile(writerToTalesList):
    percentile = set()

    for key, value in writerToTalesList:
        percentile.add(len(value))
    percentile = sorted(percentile)

    maxIndex = len(percentile) - 1
    lengthToPercentile = defaultdict()
    for i in range(0, len(percentile)):
        lengthToPercentile[percentile[i]] = (float(i) / maxIndex)
    return lengthToPercentile

storiesPerDay = 10
days = 30
totalStoriesCount = 0
verbose = False
writerToTalesMap = OrderedDict()
with open('data.csv', 'rb') as csvFile:
    spamReader = csv.reader(csvFile)
    for row in spamReader:
        if row[0] not in writerToTalesMap:
            writerToTalesMap[row[0]] = []
        writerToTalesMap[row[0]].append(row[1])
        totalStoriesCount = max(
            totalStoriesCount, len(writerToTalesMap[row[0]]))

writerToTalesList = writerToTalesMap.items()
lengthToPercentile = calculateLengthToPercentile(writerToTalesList)

doneElements = []
heap = HeapWrapper(key=lambda element: element.get_priority())
for key, value in writerToTalesList:
    heap.push(QueueElement(key, value, storiesPerDay, lengthToPercentile[len(value)]))

for i in range(0, days):
    print "\n\nDay " + str(i + 1) + ":"
    for j in range(0, storiesPerDay):
        queueElement = heap.pop()
        storyId = queueElement.get_story_id()
        sys.stdout.write("Writer: " + str(queueElement.writer_id) + ", Tale: " + str(storyId) + "   ")
        if queueElement.get_remaining_stories_count() > 0:
            heap.push(queueElement)
        else:
            doneElements.append(queueElement)
    
    sys.stdout.flush()
    remainingElements = []
    for queueElement in heap._data:
        queueElement[1].reset_for_day_start()
        remainingElements.append(queueElement[1])
    heap = HeapWrapper(initial=remainingElements,
                       key=lambda element: element.get_priority())

if verbose == True:
    totalCount = len(heap._data) + len(doneElements)

    sumPercentage = 0
    sumAvgDaysWaited = 0

    for doneElement in doneElements:
        print str(doneElement)
        sumPercentage += doneElement.get_percentage_completed()
        sumAvgDaysWaited += doneElement.get_average_wait_time()

    for queueElement in heap._data:
        print str(queueElement[1])
        sumPercentage += queueElement[1].get_percentage_completed()
        sumAvgDaysWaited += queueElement[1].get_average_wait_time()

    print "Average Percentage: " + str(float(sumPercentage) / totalCount) + \
        "\nAverage Days: " + str(float(sumAvgDaysWaited) / totalCount)
