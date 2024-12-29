## BINARY TREE

class Node:
  def __init__(self, data): #membuat kelas untuk node tunggal dalam pohon biner.
    self.data = data  #setiap node akan memiliki data yang disimpan didalam nya,
    self.left = None  #serta referensi ke node kiri atau kanan.
    self.right = None
class BinaryTree:   #membuat kelas untuk pohon biner, memiliki metode untuk menyisipkan node baru kedalam pohon- 
  def __init__(self): #-serta 3 metode untuk melakukan penelusuran pohon biner
    self.root = None
  def insert(self, data): #metode untuk menyisipkan data baru kedalam pohon biner
    if not self.root:
      self.root = Node(data) #jika pohon masih kosong, maka data baru tersebut akan menjadi akar pohon
    else:                                #jika tidak kosong, panggil metode _insert_recursively-
      self._insert_recursively(self.root, data) #-untuk menyisipkan data secara rekursif kedalam pohon.
  def _insert_recursively (self, node, data): #ini merupakan metode pembantu untuk menyisipkan data secara rekursif.
    if data < node.data:  #data yang akan disisipkan akan dibandingkan dengan data pada node saat ini-
      if node.left is None: #jika data lebih kecil, itu disisipkan keanak kiri node saat ini
        node.left = Node(data)
      else:
        self._insert_recursively(node.left, data)
    elif data > node.data:    #jika lebih besar, itu disisipkan keanak kanan node saat ini
      if node.right is None:
        node.right = Node(data)
      else:
        self._insert_recursively(node.right, data)
    else:
      pass # ignore duplicates(assuming no duplicates allowed)
  def inorder_traversal(self, node): #metode ini merupakan metode pembantu utuk menyisipkan data secara rekursif kedalam pohon.
    if node:  
      self.inorder_traversal(node.left) # terlebih dahulu menelusuri anak kiri,
      print(node.data, end=" ")     #-kemudian mencetak data dari node saat ini,
      self.inorder_traversal(node.right)  #-dan terakhir menelusuri anak kanan.
  def preorder_traversal(self, node): #metode ini melakukan penelusursan preorder pada pohon biner
    if node: 
      print(node.data, end=" ")   #terlebih dahulu mencetak data dari node saat ini,
      self.preorder_traversal(node.left)  #-kemudian menelusuri anak kiri,
      self.preorder_traversal(node.right) #-dan terakhir menelusuri anak kanan.
  def postorder_traversal(self, node):    #metode ini melakukan penelusuran postorder pada pohon biner
    if node:
      self.postorder_traversal(node.left)   #terlebih dahulu menelusuri anak kiri, 
      self.postorder_traversal(node.right)  #-kemudian menelusuri anak kanan,
      print(node.data, end=" ")       #-dan terakhir mencetak data dari node saat ini.

#example usage
tree = BinaryTree()
tree.insert(5)    #menambahkan nilai pada tree
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Inorder Traversal: ")
tree.inorder_traversal(tree.root) #memanggil metode inorder
print("\nPreorder Traversal: ")
tree.preorder_traversal(tree.root) #memanggil metode preorder
print("\nPostorder traversal: ")
tree.postorder_traversal(tree.root) #memanggil metode postorder