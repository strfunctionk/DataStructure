data = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi"]  # 7
ori = ["abc", "bcd", "cde", "def", "efg", "fgh", "ghi"]  # 7
string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


def Myappend(value):
    data.append(value)


def Mypop():
    if len(data) == 0:
        raise IndexError("mypop from empty list")
    del data[-1]


def Myinsert(a, b):
    # 위치 지정으로 안한 a의 타입은 int, b는 자유
    if type(a) != int:
        raise TypeError("index must be int")

    # a가 양의 범위를 벗어날 때
    if a > len(data):
        a = len(data)

    # a가 음의 범위를 벗어날 때
    if a < 0:
        if a < -len(data):
            a = len(data)
        a = len(data) + a

    data.append(None)
    for i in range(len(data) - 1, a, -1):
        data[i] = data[i - 1]
    data[a] = b


def Myremove(value):
    switch = True
    for i in range(0, len(data) - 1, 1):
        if data[i] == value:
            del data[i]
            switch = False
    if switch:
        raise ValueError("myindex: no value")


def Myindex(value):
    for i in range(0, len(data), 1):
        if data[i] == value:
            return i
    raise ValueError("myindex: no value")


def Myreverse():
    tmp = []
    for i in range(len(data) - 1, -1, -1):
        tmp.append(data[i])
    for i in range(len(tmp)):
        data[i] = tmp[i]
    tmp.clear()


def Mycount(value):
    if type(value) != str:
        raise TypeError("index must be str")
    if value == "":
        return len(string) + 1
    count = 0
    tmp = 0
    i = 0
    while i < len(string):
        if string[i] == value[0]:
            for j in range(0, len(value), 1):
                if string[i + j] == value[j]:
                    tmp += 1
                if tmp == len(value):
                    count += 1
                    i += len(value) - 1
            tmp = 0
        i += 1
    return count


def Mylen():
    return len(string)


def test():
    Myappend("last")
    ori.append("last")
    print(f"Append, {ori == data} | ori: {ori}, data: {data}")

    Mypop()
    ori.pop()
    print(f"Pop, {ori == data} | ori: {ori}, data: {data}")

    Myinsert(-1, "test")
    ori.insert(-1, "test")
    print(f"Insert, {ori == data} | ori: {ori}, data: {data}")

    Myremove("test")
    ori.remove("test")
    print(f"Remove, {ori == data} | ori: {ori}, data: {data}")

    print(
        f"index, {ori.index('abc') == Myindex('abc')} | ori: {ori.index('abc')}, data: {Myindex('abc')}"
    )

    Myreverse()
    ori.reverse()
    print(f"Reverse, {ori == data} | ori: {ori}, data: {data}")
    print(
        f"Count, {string.count('e') ==Mycount('e')} | ori: {string.count('e')}, data: {Mycount('e')}"
    )


test()
