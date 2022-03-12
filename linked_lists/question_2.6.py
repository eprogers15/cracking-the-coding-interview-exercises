#!/usr/bin/env python3

from Node import Node
from LinkedList import LinkedList

def palindrome_check(list):
    word = []
    current = list.head
    while current != None:
        word.append(current.data)
        current = current.next
    
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    word = LinkedList()
    word.append_node(Node("s"))
    word.append_node(Node("e"))
    word.append_node(Node("s"))
    word.append_node(Node("s"))
    print(palindrome_check(word))

if __name__ == "__main__":
    main()