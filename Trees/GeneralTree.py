# -> Music
#   -> Shaan
#     -> Bum Bum Bole
#     -> Chand Shifarish
#   -> Vijay
#     -> Hands Up
#     -> Gatiya Ilidu
#     -> Belageddu
#   -> Arijit
#     -> Tum Hi Ho
#     -> Janam Janam


class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def AddChild(self, child):
        child.parent = self
        self.children.append(child)

    def GetLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def PrintChildren(self):
        spaces = " " * self.GetLevel()*2
        prefix = spaces + "->"
        print(f"{prefix} {self.data}")
        if self.children:
            for child in self.children:
                child.PrintChildren()

def BuildTree():
    root = Treenode("Music")

    Shaan = Treenode("Shaan")
    Shaan.AddChild(Treenode("Bum Bum Bole"))
    Shaan.AddChild(Treenode("Chand Shifarish"))

    Vijay = Treenode("Vijay")
    Vijay.AddChild(Treenode("Hands Up"))
    Vijay.AddChild(Treenode("Gatiya Ilidu"))
    Vijay.AddChild(Treenode("Belageddu"))

    Arijit = Treenode("Arijit")
    Arijit.AddChild(Treenode("Tum Hi Ho"))
    Arijit.AddChild(Treenode("Janam Janam"))

    root.AddChild(Shaan)
    root.AddChild(Vijay)
    root.AddChild(Arijit)

    return root

if __name__ == "__main__":
    r = BuildTree()
    r.PrintChildren()
