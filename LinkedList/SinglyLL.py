#  INSERT AT BEGINNING
#  INSERT AT END
#  INSERT VALUES (LIST)
#  INSERT AT INDEX
#  INSERT AFTER VALUE
#  REMOVE AT
#  REMOVE BY VALUE
#  GET LENGTH
#  PRINT

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def InsertAtBeginning(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def InsertAtEnd(self, val):
        new_node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.next  = None

    def InsertValues(self, val_list):
        for val in val_list:
            self.InsertAtEnd(val)

    def InsertAtIndex(self, val, index):
        new_node = Node(val)
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def InsertAfterValue(self, val, after_val):
        new_node = Node(val)
        curr = self.head
        while curr.data != after_val:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def RemoveAtIndex(self, index):
        curr = self.head
        for i in range(index-1):
            curr = curr.next
        curr.next = curr.next.next

    def RemoveByValue(self, val):
        curr = self.head
        if curr.data == val:
            self.head = curr.next
        while curr.next.data != val:
            curr = curr.next
        curr.next = curr.next.next

    def GetLength(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def Print(self):
        if self.head is None:
            print("List is empty")
            return
        
        curr = self.head
        sll = ""
        while curr:
            sll += str(curr.data) + "-->"
            curr = curr.next
        print(sll)

if __name__ == "__main__":
    ll = SinglyLL()
    ll.InsertAtBeginning(10)
    ll.InsertAtEnd(30)
    ll.InsertValues([35,45,25])
    ll.InsertAtIndex(100, 3)
    ll.InsertAfterValue(200,100)
    ll.Print()
    #ll.RemoveAtIndex(1)
    ll.RemoveByValue(200)
    ll.Print()
    print(f"Length is: {ll.GetLength()}")
    
