#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def sum_lists(list1, list2):
    num1 = ""
    num2 = ""

    current = list1.head
    while current != None:
        num1 = num1 + str(current.data)
        current = current.next
    
    current = list2.head
    while current != None:
        num2 = num2 + str(current.data)
        current = current.next
    
    sum = int(num1) + int(num2)

    li3 = LinkedList()
    for num in str(sum):
        li3.append_node(Node(int(num)))
    
    return li3

def main():
    li1 = LinkedList()
    li2 = LinkedList()

    li1.head = Node(6)
    li1.append_node(Node(1))
    li1.append_node(Node(7))

    li2.head = Node(2)
    li2.append_node(Node(9))
    li2.append_node(Node(5))

    sum_list = sum_lists(li1, li2)
    current = sum_list.head
    while current != None:
        print(current.data)
        current = current.next

if __name__ == "__main__":
    main()