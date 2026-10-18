# Same Direction
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def middle_of_LinkedList(self) -> int:
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.val

bro = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
current = bro.head
while current:
    print(current.val, end=" ")
    current = current.next

print(bro.middle_of_LinkedList())
    


# Opposite Direction
def is_palindrome(s: str) ->bool:
    l,r = 0, len(s)-1
    while l<r:
        while l<r and not s[l].isalnum():
            l+=1
        while l<r and not s[r].isalnum():
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l+=1
        r-=1
    return True

bro = "A man, a plan, a canal: Panama"
print(is_palindrome(bro))

