#  INSERT AT BEGINNING
#  INSERT AT END
#  INSERT VALUES (LIST)
#  INSERT AT INDEX
#  INSERT VALUE AFTER
#  REMOVE AT INDEX
#  REMOVE BY VALUE
#  PRINT FORWARD
#  PRINT BACKWORD
#  GET LENGTH


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLL:
    def __init__(self):
        self.head = None

    def InsertAtBeginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def InsertAtEnd(self, val):
        new_node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node.next = None
        curr.next = new_node
        new_node.prev = curr

    def InsertValues(self, val_list):
        for val in val_list:
            self.InsertAtEnd(val)

    def InsertAtIndex(self, val, index):
        new_node = Node(val)
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node

    def InsertAfter(self, val, AfterValue):
        new_node = Node(val)
        curr = self.head
        while curr.data != AfterValue:
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        curr.next.prev = new_node
        curr.next = new_node

    def RemoveAtIndex(self, index):
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        curr.next.next.prev = curr.next.prev
        curr.next = curr.next.next

    def RemoveByValue(self, value):
        curr = self.head
        while curr.next.data != value:
            curr = curr.next
        curr.next.next.prev = curr
        curr.next = curr.next.next

    def PrintForward(self):
        curr = self.head
        dll = ""
        while curr:
            dll += str(curr.data) + "-->"
            curr = curr.next
        print(dll)

    def PrintBackword(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        dll = ""
        while curr:
            dll += "<--" + str(curr.data)
            curr = curr.prev
        print(dll)

    def GetLength(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

if __name__ == "__main__":
    ll = DoublyLL()
    ll.InsertAtBeginning(10)
    ll.InsertAtBeginning(20)
    ll.InsertAtEnd(30)
    ll.InsertValues([15,25,35])
    ll.InsertAtIndex(100,3)
    ll.InsertAfter(200,100)
    #ll.PrintForward()
    #ll.RemoveAtIndex(3)
    #ll.RemoveByValue(15)
    ll.PrintForward()
    ll.PrintBackword()
    print(f"Length is: {ll.GetLength()}")
