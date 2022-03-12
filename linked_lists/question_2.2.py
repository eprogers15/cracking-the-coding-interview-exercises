#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def return_kth_element(list, k):
    current = list.head
    length = 0
    while current != None:
        length += 1
        current = current.next
    if k > length:
        return "ERROR: k is greater than the length of list"
    current = list.head
    i = 1
    while i != length - (k - 1):
        i += 1
        current = current.next
    return current

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

    print(return_kth_element(l, 7).data)

if __name__ == "__main__":
    main()