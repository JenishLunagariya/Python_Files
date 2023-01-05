class Node:
    '''for each node'''
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None
    def __repr__(self) -> str:
        return str(self.data)
    def __del__(self):
        value = self.data
        if value!= None:
            del self.next
            del self.data
            del self.prev
        # print(f"memory freed for node with data: {value}")

class LinkedListD:
    def __init__(self,nodes = None) -> None:
        self.head = None
        self.tail = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data = nodes.pop(0))
            self.head = node
            for ele in nodes :
                new_node = Node(ele)
                new_node.prev = node
                node.next = new_node
                node = node.next
            self.tail = node
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " <=> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def __len__(self):
        length =0
        node = self.head
        while node is not None:
            length+=1
            node = node.next
        return length
    def insertAtHead(self,data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node
    def insertAtTail(self,data):
        if self.tail==None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
        node = Node(data)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
    def insertAtPos(self,position,data):
        if position == 1:
            self.insertAtHead(data)
        # elif position>len(self): # when pos > len of list, insert data to tail
        #     self.insertAtTail(data)
        #     return
        else:
            previous = self.head
            cnt = 1
            while cnt < position-1:
                previous = previous.next
                cnt+=1
            if previous.next == None:
                self.insertAtTail(data)
                return
            later = previous.next
            #new node
            node = Node(data)
            previous.next = node
            node.next = later
            node.prev = previous
            later.prev = node
    def deleteNodewithPos(self,position):
        if position==1:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            del temp
        else:
            previous = None
            current = self.head
            cnt=1
            while cnt<position:
                previous = current
                current = current.next
                cnt+=1
            if current.next == None:
                self.tail = previous
                current.prev = None
                self.tail.next = None
                return
            later = current.next
            previous.next = later
            later.prev = previous
            current.next=None
            current.prev = None
            del current
            return
    def deleteNodewithData(self,target_data):
        if self.head.data == target_data:
            self.head = self.head.next
            self.head.prev = None
            return
        else:
            previous = self.head
            for node in self:
                if node.data == target_data:
                    if node.next == None:
                        self.tail = previous
                        self.tail.next = None
                        node.prev = None
                        return
                    later = node.next
                    previous.next = later
                    later.prev = previous
                    node.next = None
                    node.prev = None
                    return
                previous = node
    def modifyNodewithPos(self,position,data):
        self.deleteNodewithPos(position)
        self.insertAtPos(position,data)
        return
    def modifyNodewithData(self,target_data,updated_data):
        '''first get the position of target data, then use delete data function.
        after that use insert data function on that position'''
        cnt = 1
        node = self.head
        while (node.data != target_data):
            cnt+=1
            node = node.next
            if node == None:
                print("Not found")
                return
        self.deleteNodewithPos(position=cnt)
        self.insertAtPos(cnt,updated_data)
# ld = LinkedList(["a","b","c","d","e","f"])
ld = LinkedListD([1,3,4,5,6])
ld.insertAtHead(0)
ld.insertAtTail(7)
ld.insertAtPos(3,2)
print(ld)
# ld.insertAtPos(1,"A")
# ld.insertAtPos(2,"B")
# ld.insertAtPos(2,"C")
# ld.deleteNodewithData("D")
# print(ld)
print("head: ",ld.head)
print("tail: ",ld.tail)
print("len: ",len(ld))
# print(ld)
# ld.insertAtHead("0")
# ld.insertAtTail("1")
# ld.deleteNodewithPos(2)
# ld.deleteNodewithData("c")
# ld.modifyNodewithPos(2,"B")
# ld.modifyNodewithData("e","D")
# print(ld)
# print(len(ld))