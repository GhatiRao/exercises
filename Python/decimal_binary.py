"""
Problem : By using stacks, convert a decimal number to binary number
"""

# Create a Stack Class
class Stack():
    def __init__(self):
        self.items = [ ]

    def push(self, element):
        return self.items.append(element)

    def is_empty(self):
        return self.items.is_empty()

    def remove(self):
        return self.items.remove(-1)

    def pop(self):
        return self.items.pop(-1)

    def peek(self):
         print("picked element is: ",self.items[-1])

    def size(self):
        return len(self.items)

class DecimalBinary():
    def __init__(self, number):
        self.number = number

    def quo_rem(self):
        return [int(self.number / 2),int(self.number % 2)]

def main_process(number):
    s = Stack()
    i=0
    while number > 1:
        print(number)
        decObject = DecimalBinary(number)
        q, r = decObject.quo_rem()
        print(q, r)
        s.push(r)
        number = q
        i+=1
        if i == 10: break
    s.push(q)
    return s

def unstackToList(s):
    binaryList = [ ]
    while s.size():
        s.peek()
        pick = s.pop()
        binaryList.append(pick)

    return binaryList

number = 57
stack_created = main_process(number)
size = stack_created.size()
print("size of stack is: ", size)
FinalList = unstackToList(stack_created)
print("Final list is: ", FinalList)
