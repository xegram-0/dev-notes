class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def main():
    list1:ListNode = ListNode()
    list2:ListNode = ListNode()
    list1.append(6)
    print(list1, list2)

if __name__ == "__main__":
    main()