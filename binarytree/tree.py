class Tree(object):
    
    def __init__(self):
        self.root = None
        
    def set(self, key, value):
        '''store key-value pair'''
        if self.root == None:
            self.root = Node(key, value)
        else:
           self._add(key, value, self.root)
    
    def _add(self, key, value, node):
        if key < node.value:
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
            return self._get(key, self.root)
        else:
            return None
        
    def _get(self, key, node):
        if key == node.key:
            print 'equal: ' + node.value
            return node.value
        elif node.left is not None and key < node.key:
            print 'left'
            self._get(key, node.left)
        elif node.right is not None and key > node.key:
            print 'right'
            self._get(key, node.right)
        else:
            return None
            
    def remove(self, key):
        '''remove node at key'''
        
    def walk_dfs_inorder(self):
        '''iterate through nodes in depth-first-search "inorder"'''
        
    def walk_dfs_preorder(self):
        '''iterate through nodes in depth-first-search "preorder"'''
        
    def walk_dfs_postorder(self):
        '''iterate through nodes in depth-first-search "postorder"'''
        
    def walk_bfs(self):
        '''iterate through nodes in breadth-first-search order'''
        
    def debug_print(self):
        '''print graphical representation of tree'''
        if self.root is not None:
            self._print_tree(self.root)
            
    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print node
            self._print_tree(node.right)
        
class Node(object):
    
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
    def __str__(self):
        return '{}({})'.format(self.key, self.value)