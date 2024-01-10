class queue:
    def __init__(self):
        self.mQueue = []

    def appendItem(self, item):
        self.mQueue.append(item)

    def deleteItem(self, item):
        if item in self.mQueue:
            self.mQueue.remove(item)
        else:
            print("Item not in queue.")
        
    def displayQueue(self):
        print(self.mQueue)

def main():
    cars = queue()
    cars.appendItem("Mustang")
    cars.appendItem("Corvette")
    cars.appendItem("Charger")
    cars.deleteItem("Charger")
    cars.displayQueue()

if __name__ == "__main__":
    main()