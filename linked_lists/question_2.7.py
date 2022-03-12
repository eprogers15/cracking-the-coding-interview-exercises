#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def check_intersection(list1, list2):
    a1 = []
    current = list1.head
    while current != None:
        a1.append(current)
        current = current.next
    a2 = []
    current = list2.head
    while current != None:
        a2.append(current)
        current = current.next
    
    for i in a1:
        if i in a2:
            return i

def main():
    li1 = LinkedList()
    li2 = LinkedList()

    a = Node("a")
    b = Node("b")
    c = Node("c")

    li1.append_node(a)
    li1.append_node(b)

    li2.append_node(b)
    li2.append_node(c)

    print(check_intersection(li1, li2).data)

if __name__ == "__main__":
    main()