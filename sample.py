# パス上の次の状態で f が成り立つ
def next_(path, current_point, f):
    msg =  "次の状態の真偽 : "  + str(path[current_point + 1][0]) + "\n"
    msg += "      次の中身 : " + str(path[current_point + 1][1]) + "\n"

    if path[current_point + 1][0]:
        if f in path[current_point + 1][1]:
            msg += "          真偽 : " + str(f) + " は Next が成り立つ"
        else:
            msg += "          真偽 : " + str(f) + " は Next が成り立たない"
    else:
        msg += "          真偽 : " + str(f) + " は Next が成り立たない"

    return msg

# パス上のある状態でいつかは f が成り立つ
def finally_(path, f):
    r = False

    # TODO: 本来pathは無限なので変更必要
    for p in path:
        if p[0]:
            if f in p[1]:
                r = True
                break
    
    if r:
        msg = "          真偽 : " + str(f) + " は Finally が成り立たつ"
    else:
        msg = "          真偽 : " + str(f) + " は Finally が成り立たない"

    return msg

# パス上のすべての状態でいつも f が成り立つ
def globally_(path, f):
    r = True

    # TODO: 本来pathは無限なので変更必要
    for p in path:
        if not p[0]:
            r = False
        else:
            if f not in p[1]:
                r = False

    if r:
        msg = "          真偽 : " + str(f) + " は Globally が成り立たつ"
    else:
        msg = "          真偽 : " + str(f) + " は Globally が成り立たない"

    return msg

# パス上のある状態で g が成り立ち かつ その直前までのすべての状態で f が成り立つ
def until_(g, f):
    #
    return True


# ==============================================================================
# 本来は無限
path = [[False, ["a", "b"]], [False, ["a"]], [True, ["b", "c"]], [False, ["a"]]]
# 現時点
current_point = 1

print( next_(path, current_point, "a") ) # next_ のサンプル
print( finally_(path, "b") )             # finally_ のサンプル
print( globally_(path, "b") )            # globally_ のサンプル
