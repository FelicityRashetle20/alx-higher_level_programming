#!/usr/bin/python3
"""The documentation as required by ALX program
"""


class Node:
    """The documentation as required by ALX program
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The documentation as required by ALX program
    """
    def __str__(self):
        return_data = ""
        node_pointer = self.__head

        while node_pointer is not None:
            return_data += str(node_pointer.data)
            if node_pointer.next_node is not None:
                return_data += "\n"
            node_pointer = node_pointer.next_node

        return return_data

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        node_pointer = self.__head

        while node_pointer is not None:
            if node_pointer.data > value:
                break
            node_pointer_prev = node_pointer
            node_pointer = node_pointer.next_node

        newNode = Node(value, node_pointer)
        if node_pointer == self.__head:
            self.__head = newNode
        else:
            node_pointer_prev.next_node = newNode
