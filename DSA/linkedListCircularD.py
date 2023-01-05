class Node:
    '''create node'''
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self) -> str:
        return str(self.data)
    def __del__(self):
        value = self.data
        if value!=None:
            del self.data
            del self.next
            del self.prev

class LinkedListCD:
    def __init__(self,nodes = None) -> None:
        self.tail = None
        if nodes is not None and len(nodes) != 0:
            node = Node(nodes.pop(0))
            temp = node
            for ele in nodes:
                new_node = Node(ele)
                new_node.prev = node
                node.next = new_node
                node = node.next
            self.tail = node
            self.tail.next = temp
            temp.prev = self.tail
    def __repr__(self) -> str:
        if self.tail == None:
            return "None"
        node = self.tail.next
        nodes = []
        while node != self.tail:
            nodes.append(str(node.data))
            node = node.next
        nodes.append(str(self.tail.data))
        nodes.append("To_Head")
        return "<=>".join(nodes)
    def __iter__(self):
        node = self.tail.next
        while node != self.tail:
            yield node
            node = node.next
        yield node
    def __len__(self):
        if self.tail == None:
            return 0
        length = 0
        node = self.tail.next
        while node != self.tail:
            length+=1
            node = node.next
        return length+1
    def insertAtTail(self,data):
        if self.tail == None:
            node = Node(data)
            self.tail = node
            self.tail.prev = self.tail.next = self.tail
            return
        else:
            node = Node(data)
            node.next = self.tail.next
            node.prev = self.tail
            self.tail.next.prev = node
            self.tail.next = node
            self.tail = node
            return
    def insertAtNode(self,element,data):
        if self.tail == None:
            self.insertAtTail(data)
            return
        else:
            previous = self.tail
            current = self.tail.next
            while current.data != element:
                if current == self.tail:
                    print("No element found")
                    return
                previous = previous.next
                current = current.next
            if current == self.tail:
                self.insertAtTail(data)
                return
            # new node
            node = Node(data)
            previous.next = node
            node.prev = previous
            node.next = current
            current.prev = node
    def insertAtPos(self,position,data):
        if self.tail==None:
            self.insertAtTail(data)
            return
        else:
            cnt = 1
            previous = self.tail
            current = self.tail.next
            while cnt < position:
                if current == self.tail:
                    self.insertAtTail(data)
                    return
                cnt+=1
                previous = previous.next
                current = current.next
            # new node
            node = Node(data)
            previous.next = node
            node.prev = previous
            node.next = current
            current.prev = node
            return
    def deleteNodewithData(self,target_data):
        if self.tail == None:
            return self
        elif self.tail.next == self.tail:
            self.tail = None
            return
        else:
            previous = self.tail
            current = self.tail.next
            while current.data != target_data:
                previous = previous.next
                current = current.next
            later = current.next
            previous.next = later
            if current ==self.tail:
                self.tail = previous
            later.prev = previous
            current.next = None
            current.prev = None
            del current
            return
    def deleteNodewithPos(self,position):
        if self.tail == None:
            print("LinkedList is empty")
            return
        elif self.tail == self.tail.next and self.tail == self.tail.prev:
            self.tail = None
            return
        else:
            previous = self.tail
            current = self.tail.next
            cnt = 1
            while cnt < position:
                previous = previous.next
                current = current.next
                cnt+=1
                if previous == self.tail:
                    print("Position Out of Bound")
                    return
            if current == self.tail:
                self.tail = previous
            previous.next = current.next
            current.next.prev = previous
            current.prev = None
            current.next = None
            del current
            return

lc = LinkedListCD([1,2,3,4,5,6])
# lc.insertAtTail(1)
# lc.insertAtTail(3)
# lc.insertAtNode(3,2)
# lc.insertAtNode(6,7)
# lc.deleteNodewithData(7)
# lc.insertAtPos(1,0)
# lc.insertAtPos(3,2)
# lc.insertAtPos(6,7)
# lc.deleteNodewithPos(7)
print(lc)
print("head: ",lc.tail.next)
print("tail: ",lc.tail)
# print(lc.tail.next.next.next.next.next.next.next)
# print(lc.tail.prev.prev.prev.prev.prev.prev.prev)
# print('len: ',len(lc))