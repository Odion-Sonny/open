# preorder traversal of binary tree

'''
      1
     / \
    2   3
   / \
  4   5
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_Trav(root):
    if root is None:
        return
    print(root.value)
    preorder_Trav(root.left)
    preorder_Trav(root.right)
root = Node(1, Node(2, Node(4), Node(5)), Node(3))
# preorder_Trav(root) #[1,2,3,4,5]





# In order traversal of binary tree

'''
      1
     / \
    2   3
   / \
  4   5
'''

def inorder_Trav(root):
    result = []
    if root is not None:
        result = inorder_Trav(root.left)
        result.append(root.value)
        result += inorder_Trav(root.right)
    return result
print(inorder_Trav(root)) #[4,2,5,1,3]


# post order traversal of binary tree

'''
      1
     / \
    2   3
   / \
  4   5
'''

def post_order_traversal(root):
    result = []
    if root is not None:
        result = post_order_traversal(root.left)
        result += post_order_traversal(root.right)
        result.append(root.value)
    return result

# Example usage
root = Node(1, Node(2, Node(4), Node(5)), Node(3))
print(post_order_traversal(root))


# bellman ford algorithm
def bellman_ford(g, dist, src, mx_edges):
    dist[src] = 0
    for i in range(mx_edges + 1):
        ndist = dist[:]
        for x in g:
            _from, to, cost = x
            ndist[to] = min(ndist[to], dist[_from] + cost)
        dist = ndist
    return dist