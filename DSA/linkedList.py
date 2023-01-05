'''linked list is Data structure containing many nodes. each node contains data and 
address of next node.
-Linear DS
-Dynamic DS
-insertion and deletion easy than array
ex:Singly linkedlist=>  [5|710]--> [6|810]--> [12|910]--> [14|null]'''
class Node:
    '''for each node'''
    def __init__(self,data=None) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return str(self.data)
    def __del__(self):
        value = self.data
        if value!= None:
            del self.next
            del self.data
        # print(f"memory freed for node with data: {value}")

class LinkedListS:
    '''represents start of the linked list'''
    def __init__(self,nodes = None) -> None:
        self.head = None
        self.tail = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data = nodes.pop(0))
            self.head  = node
            for ele in nodes:
                node.next = Node(ele)
                node = node.next
            self.tail = node
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    def __iter__(self):
        node = self.head
        while node is  not None:
            yield node
            node = node.next
    def __len__(self):
        length = 0
        node =self.head
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
        # create node
        node = Node(data=data)
        node.next = self.head
        self.head = node
    def insertAtTail(self,data):
        if self.tail == None:
            node = Node(data)
            self.head = node
            self.tail = node
            return
        node = Node(data=data)
        self.tail.next = node
        self.tail = self.tail.next
    def insertAtPos(self,position,data):
        if position == 1:
            self.insertAtHead(data)
            return
        # travere to position
        temp = self.head
        cnt = 1
        while cnt < position-1:
            temp = temp.next
            cnt+=1
        if temp.next == None:
            self.insertAtTail(data)
            return
        # new node
        node_new = Node(data)
        node_new.next = temp.next
        temp.next = node_new
    def deleteNodewithPos(self,position):
        if position==1:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            return
        else:
            prev = None
            current = self.head
            cnt = 1
            while cnt<position:
                prev = current
                current = current.next
                cnt+=1
            if current.next == None:
                self.tail = prev
            prev.next = current.next
            current.next = None
            del current 
            return
    def deleteNodewithData(self,target_data):
        if self.head.data == target_data:
            self.head = self.head.next
            return
        else:
            prev = self.head
            for node in self:
                if node.data == target_data:
                    prev.next = node.next
                    if node.next == None:
                        self.tail = prev
                    return
                prev = node
    def reverseIt(self):
        '''Iterative solution'''
        if self.head == None or self.head.next==None:
            return self
        else:
            prev = None
            curr = self.head
            self.tail = curr
            while curr!=None:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward
            self.head = prev
        return
    def solutionReverse(self,prev,curr):
        # base case
        if curr == None:
            self.head = prev
            return
        else:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            self.solutionReverse(prev,curr)
            return
    def ReverseIt(self):
        '''Recursive solution'''
        if self.head == None or self.head.next==None:
            return self
        prev = None
        curr = self.head
        self.tail = curr
        self.solutionReverse(prev,curr)
        return
    def MiddleOfIt(self):
        '''time complexity: O(n)'''
        n = len(self)
        mid = n//2
        node = self.head
        cnt = 1
        while cnt<=mid:
            node = node.next
            cnt+=1
        return node
    def MiddleOfItOptimised(self):
        if self.head ==None:
            return self
        elif self.head.next == None:
            return self.head
        elif self.head.next == self.tail:
            return self.tail
        else:
            '''fast moves 2 steps and slow moves 1 step with each iteration'''
            fast = self.head.next
            slow = self.head
            while fast != None:
                fast = fast.next
                if fast != None:
                    fast = fast.next
                slow = slow.next
            return slow
# ll = LinkedListS(["a","b","c","d","e","f"])
# print(ll)
ll = LinkedListS([1,2,3,4,5,6])
# ll.insertAtHead(1)
# ll.insertAtTail(3)
# ll.insertAtPos(2,2)
# ll.insertAtTail(4)
# ll.insertAtTail(5)
# ll.insertAtHead(0)
print(ll)
print("head: ",ll.head)
print("tail:",ll.tail)
# print("len: ",len(ll))
# print("after")
# ll.ReverseIt()
# ll.reverseIt()
print("mid:",ll.MiddleOfIt())
# print(ll)
# print("head: ",ll.head)
# print("tail:",ll.tail)
# print("len: ",len(ll))
# ll = LinkedListS()
# print(ll)
# ll.insertAtHead("A")
# ll.insertAtTail("B")
# ll.insertAtPos(2,"C")
# print(ll)
# print(ll.MiddleOfItOptimised())
# print("head: ",ll.head)
# print("tail: ",ll.tail)
# print(len(ll))
# print("After")
# ll.ReverseIt()
# print(ll)
# print("head: ",ll.head)
# print("tail: ",ll.tail)
# ll.deleteNodewithData("c")
# print(ll)
# print(ll.head)
# print(ll.tail)