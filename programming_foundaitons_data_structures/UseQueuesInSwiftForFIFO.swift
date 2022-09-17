class Queue {
    var queueArray = [String]()

    // enqueue 
    func enqueue(item:String) {
        self.queueArray.append(item)
    }

    // dequeue
    func dequeue()->String? {
        if self.queueArray.first != nil {
            let firstString = self.queueArray.first
            self.queueArray.removeFirst()
            return firstString!
        } else {
            return nil
        }
    }

    // peek
    func peek() -> String? {
        if self.queueArray.first != nil {
            return self.queueArray.first
        } else {
            return nil
        }
    }
}

// creating a queue object 
var myQueue = Queue()

// adding items to the Queue using the enqueue() method 
myQueue.enqueue(item: "Peggy")
myQueue.enqueue(item: "Larry")
myQueue.enqueue(item: "Serena")


// printing items from myQueue
print(myQueue.peek()!)
print(myQueue.peek()!)

// removing an item from myQueue using the dequeue() method
var fistToLeave = myQueue.dequeue()

// printing items from myQueue
print(myQueue.peek()!)