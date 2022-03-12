#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

# Question 2.1 Algorithm
def delete_dups1(linked_list):
    current = linked_list.head
    while current.next != None:
        neighbor = current
        while neighbor.next != None:
            if neighbor.next.data == current.data:
                neighbor.next = neighbor.next.next
            if neighbor.next != None:
                neighbor = neighbor.next
        current = current.next

def main():
    # create linked list
    n = Node("emmett")
    l = LinkedList()
    l.head = n
    l.append_node(Node("amy"))
    l.append_node(Node("dave"))
    l.append_node(Node("emmett"))
    l.append_node(Node("anthony"))
    l.append_node(Node("carlos"))
    l.append_node(Node("dave"))

    print("original")
    l.print_list()
    delete_dups1(l)
    print("\nupdated")
    l.print_list()

if __name__ == "__main__":
    main()