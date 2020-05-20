# LTL のサンプルプログラム

# パス上の次の状態で f が成り立つ
def next_(f):
    #
    return True

# パス上のある状態でいつかは f が成り立つ
def finally_(f):
    # 
    return True

# パス上のすべての状態でいつも f が成り立つ
def globally_(f):
    #
    return True

# パス上のある状態で g が成り立ち かつ その直前までのすべての状態で f が成り立つ
def until_(f):
    #
    return True

# 本来は無限
path = [[False, ["a", "b"]], [False, ["a"]], [True, ["b", "c"]], [False, ["a"]]]
