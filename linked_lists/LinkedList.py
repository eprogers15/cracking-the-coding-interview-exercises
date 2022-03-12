#!/usr/bin/env python3

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append_node(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
    
    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next