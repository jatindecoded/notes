class Node:
    def __init__(self, key, val, nextPtr=None, prevPtr=None):
        self.key = key
        self.val = val 
        self.next = nextPtr
        self.prev = prevPtr


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {} # cache will store pointers to linked list nodes
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.right.prev = self.left
        self.left.next = self.right
        

    def appendNode(self, keyNode):
        keyNode.next = self.right
        keyNode.prev = self.right.prev
        self.right.prev = keyNode
        keyNode.prev.next = keyNode
    
    def removeNode(self, keyNode):
        keyNode.next.prev = keyNode.prev
        keyNode.prev.next = keyNode.next
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        keyNode = self.cache[key]
        
        self.removeNode(keyNode)
        self.appendNode(keyNode)

        return keyNode.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            keyNode = self.cache[key]
            keyNode.val = value
            self.removeNode(keyNode)
        else:
            keyNode = Node(key, value)
            self.cache[key] = keyNode
            self.size += 1
            
        self.appendNode(keyNode)


        if self.size > self.capacity:
            self.cache.pop(self.left.next.key)
            self.removeNode(self.left.next)
            self.size -= 1
        

        




# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.values = {}
#         self.requests = []
#         self.size = 0

#         self.time = 0
        

#     def get(self, key: int) -> int:
#         self.time +=1
#         if key not in self.values:
#             return -1
#         heapq.heappush(self.requests, (self.time, key))
#         self.values[key][1] = self.time
#         return self.values[key][0]
        

#     def put(self, key: int, value: int) -> None:
#         self.time +=1
#         heapq.heappush(self.requests, (self.time, key))
#         if key not in self.values:
#             self.size += 1

#         self.values[key] = [value, self.time]

#         if self.size > self.capacity:
#             while self.requests:
#                 time, key = heapq.heappop(self.requests)
#                 if key in self.values and self.values[key][1] == time : # if last used time != request time
#                     self.values.pop(key)
#                     self.size-=1
#                     break
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)