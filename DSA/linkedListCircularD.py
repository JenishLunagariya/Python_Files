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
        return " <=> ".join(nodes)
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
            pass

lc = LinkedListCD()
lc.insertAtTail(1)
lc.insertAtTail(2)
print(lc)
print("head: ",lc.tail.next)
print("tail: ",lc.tail)
print(lc.tail.next.next)
# print(lc.tail.next.next.next.prev.prev.prev)
print('len: ',len(lc))