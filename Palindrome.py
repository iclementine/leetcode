def palindrome_num(num):
	reverse = 0
	original = num
	while num > 0 :
		reverse = reverse*10 + num%10
		num = num/10
		print(num, reverse)
	print(original, reverse)
	if original == reverse:
		return True
	else:
		return False

print(palindrome_num(123321))

def palindrome_str(string):
	length = int(len(string)/2)
	for i in range(length):
		if string[i] != string[len(string)-1-i]:
			return False
	return True

print("abcba", palindrome_str("abcba")) #odd
print("abccba", palindrome_str("abccba")) #even
print("abccbaa", palindrome_str("abccbaa")) 

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    def add(self, val):
        if self.next is None:
            self.next = Node(val)
        else:
            self.next.add(val)
    def printTree(self):
        print(self.value)
        if self.next:
            self.next.printTree()

def palindrome_linkedlist(node):
	stack = []
	curr = node
	runner = node
	while runner != None and runner.next != None:
		stack.append(curr.value)
		# print(stack)
		runner = runner.next.next
		curr = curr.next
	if runner != None: curr = curr.next # if length is odd,, 
	while curr != None:
		if stack.pop() != curr.value: return False
		curr = curr.next
	return True
    
c = Node(1)
c.add(2)
c.add(3)
c.add(2)
c.add(1)
#c.printTree()
print(palindrome_linkedlist(c))


