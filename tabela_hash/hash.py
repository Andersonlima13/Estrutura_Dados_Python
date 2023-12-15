
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hash:

    def __init__(self, size=10):
        self._size = size
        self._table = [None for x in range(size)] # vetor que guarda os dados

    def _rehash(self, i):
        return (i+1) % self._size

    def _hash(self, key):
        return key % self._size

    def put(self, key, value):
        h = self._hash(key)
        if self._table[h] is None:
            self._table[h] = Entry(key, value)
        else:
            if self._table[h].key == key:
                self._table[h].value = value
            else:
                index = 2
                while index < self._size:
                    r = self._rehash(index)
                    if self._table[r] is None:
                        self._table[r] = Entry(key, value)
                    else:
                        if self._table[r].key == key:
                            self._table[r].value = value

                    index += 1
                    

    def get(self, key):
        entry = self._table[self._hash(key)]
        if entry:
            if entry.key == key:
                return entry.value
            else:
                index = 2
                while index < self._size:
                    r = self._rehash(index)
                    if self._table[r] is None:
                        return None
                    else:
                        if self._table[r].key == key:
                            return self._table[r].value
                    index += 1
        return None # key não existe


    def delete(self, key):
        entry = self._table[self._hash(key)]
        if entry:
            if entry.key == key:
                self._table[self._hash(key)] = None
            else:
                index = 2
                while index < self._size:
                    r = self._rehash(index)
                    if self._table[r] is None:
                        return None
                    else:
                        if self._table[r].key == key:
                            self._table[self._hash(key)] = None
                    index += 1
        return None # key não existe
        
    

if __name__ == "__main__":
    h = Hash()
    h.put(1, "Rodrigo")
    assert h._table[1].value == "Rodrigo"
    assert h.get(1) == "Rodrigo"
    h.put(2, "João")
    assert h.get(2) == "João"
    assert h._table[2].value == "João"
    h.put(1, "José")
    assert h.get(1) == "José"
    assert h._table[1].value == "José"
    h.put(11, "Maria")
    assert h._table[3].value == "Maria"
    assert h.get(11) == "Maria"
    assert h.get(1) == "José"