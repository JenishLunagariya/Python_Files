class Node:
    '''create node'''
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return str(self.data)
    def __del__(self):
        value = self.data
        if value!=None:
            del self.data
            del self.next
class LinkedListCS:
    def __init__(self,nodes = None) -> None:
        self.tail = None
        if nodes is not None and len(nodes) != 0:
            node = Node(nodes.pop(0))
            temp = node
            for ele in nodes:
                node.next = Node(ele)
                node = node.next
            self.tail = node
            self.tail.next = temp
    def __repr__(self) -> str:
        if self.tail == None:
            return "None"
        node = self.tail.next
        target = self.tail
        nodes = []
        while node != target:
            nodes.append(str(node.data))
            node = node.next
        nodes.append(str(self.tail.data))
        nodes.append("To_Head")
        return "->".join(nodes)
    def __iter__(self):
        node = self.tail.next
        while node!= self.tail:
            yield node
            node = node.next
        yield node
    def __len__(self):
        if self.tail == None:
            return 0
        length = 0
        node = self.tail.next
        while node!=self.tail:
            length+=1
            node = node.next
        return length+1
    def insertAtTail(self,data):
        if self.tail == None:
            node = Node(data)
            self.tail = node
            node.next = node
            return
        else:
            node = Node(data)
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
            return
    def insertAtNode(self,element,data):
        if self.tail == None:
            self.insertAtTail(data)
            return
        else:
            current = self.tail
            while current.data != element:
                current = current.next
            # create new node
            node = Node(data)
            node.next = current.next
            current.next = node
    def insertAtPos(self,position,data):
        if self.tail == None:
            self.insertAtTail(data)
            return
        else:
            cnt = 1
            previous = self.tail
            current = self.tail.next
            while cnt<position:
                if current==self.tail:
                    '''when pos > len, insert node to tail'''
                    self.insertAtTail(data)
                    return
                cnt+=1
                previous = previous.next
                current = current.next
            node = Node(data)
            previous.next = node
            node.next = current
            return
    def deleteNodewithData(self,target_data):
        if self.tail == None:
            print("LinkedList is empty")
            return
        elif self.tail.next == self.tail:
            if self.tail.data == target_data:
                self.tail = None
                return
            else:
                print("No matching Data")
                return
        else:
            prev = self.tail
            curr = self.tail.next
            while curr.data != target_data:
                if curr == self.tail:
                    print("No match found")
                    return
                prev = prev.next
                curr = curr.next
            prev.next = curr.next
            if self.tail == curr:
                self.tail = prev
            curr.next = None
            del curr
            return
    def deleteNodewithPos(self,position):
        if self.tail == None:
            print("LinkedList is empty")
            return
        elif self.tail == self.tail.next:
            self.tail = None
            return
        else:
            prev = self.tail
            curr = self.tail.next
            cnt=1
            while cnt<position:
                prev = prev.next
                curr = curr.next
                cnt+=1
                if prev == self.tail:
                    print("Position Out of Bound")
                    return
            if curr == self.tail:
                self.tail = prev
            prev.next = curr.next
            curr.next = None
            del curr
            return
    def reverseIt(self):
        '''Iterative solution'''
        if self.tail == None or self.tail == self.tail.next:
            return self
        head = self.tail.next
        prev = self.tail
        curr = self.tail.next
        while curr != self.tail:
            print(curr)
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        curr.next = prev
        self.tail = head
        return
    def solutionReverse(self,prev,curr):
        # base case
        if curr == self.tail:
            curr.next = prev
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
        if self.tail == None or self.tail == self.tail.next:
            return self
        else:
            prev = self.tail
            curr = self.tail.next
            head = self.tail.next
            self.solutionReverse(prev,curr)
            # curr.next = prev
            self.tail = head
            return
    def MiddleOfIt(self):
        if self.tail == None:
            return self
        n = len(self)
        mid = n//2
        node = self.tail.next
        cnt=1
        while cnt<=mid:
            node = node.next
            cnt+=1
        return node
    def MiddleOfItOptimised(self):
        if self.tail == None:
            return self
        elif self.tail.next == self.tail:
            return self.tail
        else:
            fast = self.tail.next.next
            slow = self.tail.next
            while fast!=self.tail.next:
                fast = fast.next
                if fast!= self.tail.next:
                    fast = fast.next
                slow = slow.next
            return slow

    def isCircular(self,head,head_next):
        '''check LL is circular or not, return true/false'''
        if head == None:
            return True
        else:
            temp = head_next
            while temp!=None and temp!= head:
                temp = temp.next
            if temp == head:
                return True
            elif temp == None:
                return False
    
# lc = LinkedListCS(["a","b","c"])
lc = LinkedListCS([1,2,3,4,5,6])
print(lc)
# lc.ReverseIt()
# print(lc)
# lc.insertAtTail(5)
# lc.insertAtNode(2,22)
# lc.deleteNodewithData(22)
# lc.deleteNodewithPos(7)
# lc.insertAtPos(6,5)
# print(lc.MiddleOfItOptimised())
# print("Head: ",lc.tail.next)
# print("tail: ",lc.tail)
# print(lc.tail.next.next.next.next.next.next.next)
# print("len: ",len(lc)
print(lc.isCircular(lc.tail.next,lc.tail.next.next))