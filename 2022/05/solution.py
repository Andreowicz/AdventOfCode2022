f = open(r"c:\Users\u-45886\AdventOfCode2022\2022\05\input", "r")
liste = f.read().split("\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Stack:
 
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
 
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "<-"
            cur = cur.next
        return out[:-2] + '|'
 
    # Get the current size of the stack
    def getSize(self):
        return self.size
 
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
 
    # Get the top item of the stack
    def peek(self):
 
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
 
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
 
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

 
# Driver Code
if __name__ == "__main__":
    stack1 = Stack()
    stack1.push('S')
    stack1.push('L')
    stack1.push('W')

    stack2 = Stack()
    stack2.push('J')
    stack2.push('T')
    stack2.push('N')
    stack2.push('Q')

    stack3 = Stack()
    stack3.push('S')
    stack3.push('C')
    stack3.push('H')
    stack3.push('F')
    stack3.push('J')

    stack4 = Stack()
    stack4.push('T')
    stack4.push('R')
    stack4.push('M')
    stack4.push('W')
    stack4.push('N')
    stack4.push('G')
    stack4.push('B')

    stack5 = Stack()
    stack5.push('T')
    stack5.push('R')
    stack5.push('L')
    stack5.push('S')
    stack5.push('D')
    stack5.push('H')
    stack5.push('Q')
    stack5.push('B')

    stack6 = Stack()
    stack6.push('M')
    stack6.push('J')
    stack6.push('B')
    stack6.push('V')
    stack6.push('F')
    stack6.push('H')
    stack6.push('R')
    stack6.push('L')

    stack7 = Stack()
    stack7.push('D')
    stack7.push('W')
    stack7.push('R')
    stack7.push('N')
    stack7.push('J')
    stack7.push('M')

    stack8 = Stack()
    stack8.push('B')
    stack8.push('Z')
    stack8.push('T')
    stack8.push('F')
    stack8.push('H')
    stack8.push('N')
    stack8.push('D')
    stack8.push('J')

    stack9 = Stack()
    stack9.push('H')
    stack9.push('L')
    stack9.push('Q')
    stack9.push('N')
    stack9.push('B')
    stack9.push('F')
    stack9.push('T')

#sol1
    # for element in liste:
    #     (_, mv, _, src, _, dst) = element.split(' ')
    #     i = 0
    #     hstack = Stack()
    #     while i < int(mv):
    #         cstring = 'hstack.push(stack' + src + '.pop())'
    #         eval(cstring)
    #         cstring = 'stack' + dst + '.push(hstack.pop())'
    #         eval(cstring)
    #         i += 1

#sol2
    for element in liste:
        (_, mv, _, src, _, dst) = element.split(' ')
        i = 0
        hstack = []
        while i < int(mv):
            cstring = 'hstack.append(stack' + src + '.pop())'
            eval(cstring)
            i += 1
        i = 0
        hstack.reverse()
        while i < int(mv):
            cstring = 'stack' + dst + '.push(hstack[i])'
            eval(cstring)
            i += 1
    
    print(stack1.peek())
    print(stack2.peek())
    print(stack3.peek())
    print(stack4.peek())
    print(stack5.peek())
    print(stack6.peek())
    print(stack7.peek())
    print(stack8.peek())
    print(stack9.peek())
