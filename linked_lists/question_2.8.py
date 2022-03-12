#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def loop_detection(list):
    visited = []
    current = list.head
    while current != None:
        if current in visited:
            return current.data
        visited.append(current)
        current = current.next

def main():
    li = LinkedList()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    li.append_node(a)
    li.append_node(b)
    li.append_node(c)
    li.append_node(d)
    li.append_node(c)

    print(loop_detection(li))

if __name__ == "__main__":
    main()