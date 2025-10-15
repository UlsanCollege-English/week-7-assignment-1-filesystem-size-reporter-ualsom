import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from filesystem import Node, total_size, folder_sizes, level_order

# helpers
def fs1():
    # root/
    #  ├─ pics/ (files: a=5, b=7)
    #  └─ docs/ (files: c=3)
    pics = Node("pics", 0, [Node("a",5), Node("b",7)])
    docs = Node("docs", 0, [Node("c",3)])
    root = Node("root", 0, [pics, docs])
    return root, pics, docs

# --- normal (4)
def test_total_size_on_folder():
    root, pics, _ = fs1()
    assert total_size(pics) == 12

def test_total_size_on_root():
    root, _, _ = fs1()
    assert total_size(root) == 15

def test_folder_sizes_map():
    root, pics, docs = fs1()
    m = folder_sizes(root)
    assert m["pics"] == 12 and m["docs"] == 3

def test_level_order_basic():
    root, pics, docs = fs1()
    assert level_order(root) == [["root"], ["pics", "docs"], ["a","b","c"]]

# --- edge (3)
def test_empty_root_none():
    assert total_size(None) == 0
    assert folder_sizes(None) == {}
    assert level_order(None) == []

def test_single_file():
    f = Node("single", 42, [])
    assert total_size(f) == 42
    assert folder_sizes(f) == {}
    assert level_order(f) == [["single"]]

def test_deep_chain():
    n3 = Node("n3", 3, [])
    n2 = Node("n2", 0, [n3])
    n1 = Node("n1", 0, [n2])
    assert total_size(n1) == 3
    assert level_order(n1) == [["n1"], ["n2"], ["n3"]]

# --- harder (3)
def test_wide_folder():
    kids = [Node(str(i), i) for i in range(10)]
    root = Node("root", 0, kids)
    assert total_size(root) == sum(range(10))
    assert level_order(root)[1] == [str(i) for i in range(10)]

def test_mixed_nested():
    leafs = [Node("f"+str(i), i) for i in range(4)]
    sub = Node("sub", 0, [leafs[0], Node("mid",0,[leafs[1], Node("deep",0,[leafs[2],leafs[3]])])])
    root = Node("root", 0, [sub])
    assert folder_sizes(root)["sub"] == sum(i for i in range(4))

def test_large_random_shape():
    # small stress
    n = Node("r", 0, [Node("a",0,[Node("x",5)]), Node("b",0,[Node("y",7), Node("z",9)])])
    assert total_size(n) == 21
