

class OrderQueue:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def addOrder(self, teaOrder):
        self.heapList.append(teaOrder)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i].getDistance() > self.heapList[i // 2].getDistance():
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i].getDistance() < self.heapList[mc].getDistance():
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2].getDistance() > self.heapList[i * 2 + 1].getDistance():
                return i * 2
            else:
                return i * 2 + 1


    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval



    def processNextOrder(self):
        if self.currentSize == 0:
            raise QueueEmptyException
        value = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return value.getOrderDescription()

class QueueEmptyException(Exception):
    pass


'''from TeaOrder import TeaOrder
queue = OrderQueue()
tea_order1 = TeaOrder(100)
tea_order2 = TeaOrder(300)
tea_order3 = TeaOrder(200)
queue.addOrder(tea_order1)
queue.addOrder(tea_order2)
queue.addOrder(tea_order3)

print(queue.processNextOrder())'''
