    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def rec_copy(head, visited):
            if head == None: return None
            if head in visited: return visited[head]

            node = Node(head.val, None, None)
            visited[head] = node

            node.next   = rec_copy(head.next, visited)
            node.random = rec_copy(head.random, visited)

            return node

        visited = {}

        return rec_copy(head, visited)

    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head): return head
        new_head = Node(head.val, Node(0), Node(head.random and head.random.val or 0))
        new_node = new_head
        while(head):
            head = head.next

            if(head):
                aux = Node(head.val, Node(-10000), Node(head.random and head.random.val or 0))
                new_node.next = aux
                new_node = aux
            else:
                if new_node.next.val == -10000:
                    new_node.next = None


        head = new_head
        while head:
            count = 0
            find_node = new_head
            if head.random and head.random.val > 0:
                while find_node and find_node.val != head.random.val:
                    find_node = find_node.next
            else:
                find_node = None
            head.random = find_node
            head = head.next
        test = new_head
        while(test):
            test = test.next
        return new_head