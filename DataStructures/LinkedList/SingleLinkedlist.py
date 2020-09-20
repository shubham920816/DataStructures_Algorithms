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
        Args:
            node:

        Returns:

        """
        temp = self.head
        self.head = node
        self.head.next = temp

    def insert_at_tail(self, node):
        """

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

    def insert_at_position(self, position, node):
        """

        Args:
            position:
            node:

        Returns:

        """
        i = 0
        temp = self.head
        while temp:

            if i == position - 1:
                val = temp.next
                temp.next = node
                temp = temp.next
                temp.next = val
                i = i+1

            else:
                i += 1
                temp = temp.next


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
    single_list.insert_at_position(2, sixth)
    single_list.print_list()
    print("##########")

