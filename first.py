class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    # 1. Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Сортування злиттям
    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return merge_sorted_lists(left, right)

    def _get_middle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


# 3. Об’єднання двох відсортованих однозв’язних списків
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


# Приклад використання
list1 = SinglyLinkedList()
for v in [3, 1, 5, 2]:
    list1.append(v)

list2 = SinglyLinkedList()
for v in [4, 6, 0]:
    list2.append(v)

list1.sort()
list2.sort()

merged_head = merge_sorted_lists(list1.head, list2.head)

merged_list = SinglyLinkedList()
merged_list.head = merged_head

print("Відсортований список 1:", list1.to_list())
print("Відсортований список 2:", list2.to_list())
print("Об'єднаний список:", merged_list.to_list())

list1.reverse()
print("Реверсований список 1:", list1.to_list())
