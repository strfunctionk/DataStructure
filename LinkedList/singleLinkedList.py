class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node()
        new_node.data = data

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        current = self.head
        if current is None:
            print("리스트가 비어 있습니다.")
            return
        while current is not None:
            print(current.data, end=" -> " if current.next else " -> 끝")
            current = current.next
        print("")

    def insert(self, index, data):
        new_node = Node()
        new_node.data = data

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        if index < 0:
            print("잘못된 인덱스입니다.")
            return
        current = self.head
        for i in range(index - 1):
            if current is None:
                print("잘못된 인덱스입니다.")
                return
            current = current.next

        if current is None:
            print("잘못된 인덱스입니다.")
            return

        new_node.next = current.next
        current.next = new_node

    def delete(self, index):
        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(index - 1):
            if current is None or current.next is None:
                print("잘못된 인덱스입니다.")
                return
            current = current.next

        if current.next is None:
            print("잘못된 인덱스입니다.")
            return

        current.next = current.next.next

    def search(self, data):
        count = 0
        current = self.head
        while current is not None:
            if current.data == data:
                return count
            current = current.next
            count += 1
        return -1  # 찾지 못한 경우

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def swap(self, a, b):
        if a == b:
            return

        index = 0
        node_a = node_b = None
        current = self.head

        while current:
            if index == a:
                node_a = current
            if index == b:
                node_b = current
            current = current.next
            index += 1

        if node_a is None or node_b is None:
            print("잘못된 인덱스입니다.")
            return

        node_a.data, node_b.data = node_b.data, node_a.data

    def values(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values


def appends(vals, linked):
    if isinstance(vals, list):
        for i in vals:
            linked.append(i)
    else:
        print("list 타입이 아닙니다.")


def diff(value, list):
    if len(value) != len(list.values()):
        print("길이가 다릅니다.")
        return
    for i in range(len(value)):
        if value[i] != list.values()[i]:
            print(
                f"값이 다릅니다: array[{i}]: {value[i]}, list[{i}]: {list.values()[i]}"
            )
            print(f"array: {value}")
            print(f"list : {list.values()}")
            return
    print("값이 같습니다.")
    return True


linkedList = LinkedList()

value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test = value
appends(value, linkedList)

# test
linkedList.traverse()

# append
linkedList.append(11)
test.append(11)
diff(test, linkedList)

# insert
linkedList.insert(2, 0)
test.insert(2, 0)
diff(test, linkedList)

# delete
linkedList.delete(2)  # n번째 인덱스를 삭제
test.remove(0)  # n 값을 삭제
diff(test, linkedList)

# search
print(linkedList.search(5) == test.index(5))

# reverse
linkedList.reverse()
test.reverse()
diff(test, linkedList)

# swap
linkedList.swap(0, 1)
test[0], test[1] = test[1], test[0]
diff(test, linkedList)
