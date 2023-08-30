from typing import Self


class FibHeap:
    class Node:
        def __init__(self, key, value) -> None:
            self.key = key
            self.value = value
            self.degree = 0
            self.mark = False
            self.parent = self.child = None
            self.previous = self.next = self

        def is_single(self: Self) -> bool:
            return self == self.next

        def insert(self: Self, node: Self) -> None:
            if node == None:
                return

            self.next.previous = node.previous
            node.previous.next = self.next
            self.next = node
            node.previous = self

        def remove(self: Self) -> None:
            self.previous.next = self.next
            self.next.previous = self.previous
            self.next = self.previous = self

        def add_child(self: Self, node: Self) -> None:
            if self.child == None:
                self.child = node

            else:
                self.child.insert(node)

            node.parent = self
            node.mark = False
            self.degree += 1

        def remove_child(self: Self, node: Self):
            if node.parent != self:
                raise AssertionError(
                    "Cannot remove child from a node that is not its parent"
                )

            if node.is_single():
                if self.child != node:
                    raise AssertionError("Cannot remove a node that is not a child")
                self.child = None

            else:
                if self.child == node:
                    self.child = node.next
                node.remove()

            node.parent = None
            node.mark = False
            self.degree -= 1

    def __init__(self) -> None:
        self.min_node = None
        self.count = 0
        self.max_degree = 0

    def is_empty(self) -> bool:
        return self.count == 0

    def insert(self, node: Self):
        self.count += 1
        self._insert_node()

    def _insert_node(self, node: Self):
        if self.min_node == None:
            self.min_node = node
        else:
            self.min_node.insert(node)
            if node.key < self.min_node.key:
                self.min_node = node

    def minimum(self):
        if self.min_node == None:
            raise AssertionError("Cannot return minimum of empty heap")

        return self.min_node

    def merge(self, heap: Self):
        self.min_node.insert(heap.min_node)
        if self.min_node == None or (
            heap.min_node != None and heap.min_node.key < self.min_node.key
        ):
            self.min_node = heap.min_node
        self.count += heap.count

    def remove_minimum(self):
        if self.min_node == None:
            raise AssertionError("Cannot remove from an empty heap")

        removed_node = self.min_node
        self.count -= 1

        # Assign all old root children as new roots
        if self.min_node.child != None:
            c = self.min_node.child

            while True:
                c.parent = None
                c = c.next
                if c == self.min_node.child:
                    break

            self.min_node.child = None
            self.min_node.insert(c)

        # if we have rmeoved the last key
        if self.min_node.next == self.min_node:
            if self.count != 0:
                raise AssertionError(
                    "Heap Error: expected 0 keys, count is " + str(self.count)
                )
            self.min_node = None
            return removed_node

        # Merge any roots with the same degree
        log_size = 100
        degree_roots = [None] * log_size
        self.max_degree = 0
        current_pointer = self.min_node.next

        while True:
            current_degree = current_pointer.degree
            current = current_pointer
            current_pointer = current_pointer.next
            while degree_roots[current_degree] != None:
                other = degree_roots[current_degree]

                # swap
                if current.key > other.key:
                    temp = other
                    other = current
                    current = temp

                other.remove()
                current.add_child(other)
                degree_roots[current_degree] = None
                current_degree += 1

            degree_roots[current_degree] = current
            if current_pointer == self.min_node:
                break

        # Remove current root and find new min node
        self.min_node = None
        new_max_degree = 0
        for d in range(0, log_size):
            if degree_roots[d] != None:
                degree_roots[d].next = degree_roots[d].previous = degree_roots[d]
                self._insert_node(degree_roots[d])
                if d > new_max_degree:
                    new_max_degree = d

        max_degree = new_max_degree

        return removed_node

    def decrease_key(self, node, new_key):
        if new_key > node.key:
            raise AssertionError("Cannot decrease a key to a greater value")

        elif new_key == node.key:
            return

        node.key = new_key
        parent = node.parent
        if parent == None:
            if new_key < self.min_node.key:
                self.min_node = node
            return
        elif parent.key <= new_key:
            return

        while True:
            parent.remove_child(node)
            self._insert_node(node)

            if parent.parent == None:
                break
            elif parent.mark == False:
                parent.mark
                break
            else:
                node = parent
                parent = parent.parent
                continue
