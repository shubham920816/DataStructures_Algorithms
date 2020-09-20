class Node(object):

    def __init__(self, data):
        """

        Args:
            data:
        """
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        """

        """
        self.head = None

    def print_list(self):
        """

        Returns:

        """
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    def insert_at_head(self, node):
        """
        Brute Force Approach
        Args:
            node:

        Returns:

        """
        temp = self.head
        self.head = node
        self.head.next = temp

    def insert_at_tail(self, node):
        """
        Brute Force Approach
        Args:
            node:

        Returns:

        """
        temp = self.head
        while True:
            val = temp
            temp = temp.next
            if temp is None:
                val.next = node
                break

    def insert_node_at_position_opt(self, prev_node, node):
        """

        Args:
            prev_node:
            node:

        Returns:

        """

        node.next = prev_node.next
        prev_node.next = node


if __name__ == "__main__":

    single_list = LinkedList()
    single_list.head = Node(1)
    second = Node(89)
    third = Node(72)

    single_list.head.next = second
    second.next = third
    single_list.print_list()  # Traverse the Single Linked List
    print("##################")
    fourth = Node(2)
    single_list.insert_at_head(fourth)   # Adding node at the head of the Linked List
    single_list.print_list()          # Traverse updated Linked list
    fifth = Node(5)
    print("#############")
    single_list.insert_at_tail(fifth)
    single_list.print_list()
    print("##########")
    sixth = Node(1234)
    single_list.insert_node_at_position_opt(fifth, sixth)
    single_list.print_list()
    print("##########")

