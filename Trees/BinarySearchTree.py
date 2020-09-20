class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def AddChild(self, val):
        if self.data == val:
            return

        if val < self.data:
            if self.left:
                self.left.AddChild(val)
            else:
                self.left = BinarySearchTree(val)
        else:
            if self.right:
                self.right.AddChild(val)
            else:
                self.right = BinarySearchTree(val)

    def PreOrder(self):
        ele = []
        ele.append(self.data)
        if self.left:
            ele += self.left.PreOrder()
        if self.right:
            ele += self.right.PreOrder()
        return ele

def BuildTree(nums):
    root = BinarySearchTree(nums[0])
    for i in range(1, len(nums)):
        root.AddChild(nums[i])
    return root

if __name__ == "__main__":
    nums = [5,3,2,4,1,8,6]
    tree = BuildTree(nums)
    a = tree.PreOrder()
    print(a)