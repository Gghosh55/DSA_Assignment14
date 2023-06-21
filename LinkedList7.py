head = None

class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

def sizeOfLL(head):
	count = 0
	while (head != None):
		count = count + 1
		head = head.next

	return count


def nextLargerLL(head):

	count = sizeOfLL(head)

	ans = [None]*count

	k = 0

	j = None

	temp = 0

	while (head != None):

		if (head.next == None):
			ans[k] = 0
			break


		j = head.next

		if (head.val < j.val):
			ans[k] = j.val
			k += 1

		elif (head.val >= j.val):

			while (
					j != None and head.val >= j.val): # search j.val such

				j = j.next


			if (j != None):
				ans[k] = j.val
				k += 1

			else:
				ans[k] = 0
				k += 1

		else:
			ans[k] = 0
			k += 1

		head = head.next

	return ans


def push(new_data):
	global head

	new_node = ListNode(new_data)


	new_node.next = head


	head = new_node



def printList():
	print(nextLargerLL(head))


if __name__ == '__main__':
	push(9)
	push(8)
	push(7)
	push(4)
	push(2)

	nextLargerLL(head)
	printList()
