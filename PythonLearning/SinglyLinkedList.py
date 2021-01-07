# Node Class
class Node:
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class 
class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                return('Empty linkedList')
            print(currentNode.data)
            currentNode = currentNode.next

if __name__ == '__main__':

    firstNode = Node('Ganesh')
    linkedList = LinkedList()
    linkedList.insertEnd(firstNode)
    SecondNode = Node('Singh')
    linkedList.insertEnd(SecondNode)
    thirdNode = Node('TCS')
    linkedList.insertEnd(thirdNode)
    linkedList.printList()


