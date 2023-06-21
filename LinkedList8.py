
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None


def getNode(data):
	temp = ListNode(data)
	temp.next = None
	return temp


def printList(head):
	while (head.next):
		print(head.val, end=' -> ')
		head = head.next
	print(head.val, end='')


def removeZeroSum(head, K):


	root = ListNode(0)


	root.next = head

	umap = dict()

	umap[0] = root

	sum = 0

	while (head != None):

		sum += head.val

		if ((sum - K) in umap):

			prev = umap[sum - K]
			start = prev

			aux = sum

			sum = sum - K

			while (prev != head):
				prev = prev.next
				aux += prev.val
				if (prev != head):
					umap.remove(aux)


			start.next = head.next

		else:
			umap[sum] = head

		head = head.next

	return root.next

if __name__ == '__main__':


	head = getNode(1)
	head.next = getNode(3)
	head.next.next = getNode(-3)
	head.next.next.next = getNode(2)
	head.next.next.next.next = getNode(1)


	K = 5

	head = removeZeroSum(head, K)


	if(head != None):
		printList(head)


