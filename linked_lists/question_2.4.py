#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def partition_list(list, p):
    new_list = LinkedList()
    new_list.head = Node(list.head.data)
    new_list.tail = new_list.head
    current = list.head.next
    while current != None:
        if current.data < p:
            previous_head = new_list.head
            new_list.head = Node(current.data)
            new_list.head.next = previous_head
        else:
            new_tail = Node(current.data)
            new_list.tail.next = new_tail
            new_list.tail = new_tail
        current = current.next
    return new_list

def main():
    l = LinkedList()
    l.head = Node(3)
    l.append_node(Node(5))
    l.append_node(Node(8))
    l.append_node(Node(5))
    l.append_node(Node(10))
    l.append_node(Node(2))
    l.append_node(Node(1))

    print("ORIGINAL")
    l.print_list()
    print("\nUPDATED")
    new_list = partition_list(l, 5)
    new_list.print_list()

if __name__ == "__main__":
    main()