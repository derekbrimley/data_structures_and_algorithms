class Tree(object):
    
    def __init__(self):
        self.root = None
        
    def set(self, key, value):
        '''store key-value pair'''
        if self.root == None:
            self.root = Node(key, value, Node('-'))
        else:
           self._add(key, value, self.root)
    
    def _add(self, key, value, node):
        if key < node.key:
            if node.left is not None:
                self._add(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        else:
            if node.right is not None:
                self._add(key, value, node.right)
            else:
                node.right = Node(key, value, node)
        
    def get(self, key):
        '''return value at key'''
        if self.root is not None:
            return self._get_value(key, self.root)
        else:
            return None
        
    def _get_value(self, key, node):
        if key == node.key:
            print 'equal: ' + node.value
            return node.value
        elif node.left is not None and key < node.key:
            print 'left'
            self._get_value(key, node.left)
        elif node.right is not None and key > node.key:
            print 'right'
            self._get_value(key, node.right)
        else:
            return None
            
    def remove(self, key):
        '''remove node at key'''
        node = self._find(key)
        if node.left is None and node.right is None:
            node = None
            print node
        elif node.left is not None:
            node = node.left
        elif node.right is not None:
            node = node.right
            
    def _find(self, key):
        if self.root is not None:
            q = Queue()
            q.enqueue(self.root)
            
            while not q.is_empty():
                current = q.dequeue()
                if key == current.key:
                    return current
                if current.left is not None:
                    q.enqueue(current.left)
                if current.right is not None:
                    q.enqueue(current.right)
                
        
    def walk_dfs_inorder(self):
        '''iterate through nodes in depth-first-search "inorder"'''
        if self.root is not None:
            self._inorder(self.root)
            
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print node.value
            self._inorder(node.right)
        else:
            return None
        
    def walk_dfs_preorder(self):
        '''iterate through nodes in depth-first-search "preorder"'''
        if self.root is not None:
            self._preorder(self.root)
        
    def _preorder(self, node):
        if node is not None:
            print node.value
            self._preorder(node.left)
            self._preorder(node.right)
        else:
            return None
    
    def walk_dfs_postorder(self):
        '''iterate through nodes in depth-first-search "postorder"'''
        if self.root is not None:
            self._postorder(self.root)
            
    def _postorder(self, node):
        if node is not None:
            self._preorder(node.left)
            self._preorder(node.right)
            print node.value
        else:
            return None    
    
    def walk_bfs(self):
        '''iterate through nodes in breadth-first-search order'''
        q = Queue()
        q.enqueue(self.root)
        
        while not q.is_empty():
            current = q.dequeue()
            print current.value
            if current.left is not None:
                q.enqueue(current.left)
            if current.right is not None:
                q.enqueue(current.right)
            
        
    def debug_print(self):
        '''print graphical representation of tree'''
        if self.root is not None:
            self._print_tree(self.root)
            
    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            self._print_tree(node.right)
            print node
        
class Node(object):
    
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
    def __str__(self):
        return '{}({})'.format(self.key, self.parent.key)
    
    
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)