
import time

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    def print_list_in_str(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        return output

    def is_palindrome(self):
        vals = []
        current = self.head
        if current is None:
            return 'There is no nodes in linked list'
        while current is not None:
            vals.append(current.get_data())
            current = current.get_next()
        if vals == vals[::-1]:
            return True
        else:
            return False


linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(8)
linked_list.add_node(8)
linked_list.add_node(2)
linked_list.add_node(1)
print(linked_list.print_list_in_str())

start_time = time.time()
print(linked_list.is_palindrome())
end_time = time.time()
print("Time:", end_time - start_time, "seconds")