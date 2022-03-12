#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def delete_middle_node(list, node):
    current = list.head
    while current.next != node and current.next != None:
        current = current.next
    if current.next == None:
        print("ERROR: Node not found")
        return
    current.next = current.next.next
    return

def main():
    # create linked list
    n = Node("emmett")
    l = LinkedList()
    l.head = n
    l.append_node(Node("amy"))
    l.append_node(Node("dave"))
    l.append_node(Node("emmett"))
    l.append_node(Node("anthony"))
    middle_node = Node("carlos")
    l.append_node(middle_node)
    l.append_node(Node("dave"))

    print("ORIGINAL")
    l.print_list()
    delete_middle_node(l, middle_node)
    print("\nUPDATED")
    l.print_list()

if __name__ == "__main__":
    main()