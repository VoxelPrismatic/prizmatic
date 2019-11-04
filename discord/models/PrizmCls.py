class PrizmList(list):
    def __lshift__(self, item):
        "list << item  ||  list.append(item)"
        self.append(item)
    def __rshift__(self, item):
        "list >> item  ||  list.remove(item)"
        self.remove(item)
    def __invert__(self):
        "~list | list[::-1]"
        self = self[::-1]
    def __isub__(self, data):
        "list -= data  ||  for item in data: list.remove(item)"
        for item in data:
            self >= item
        return self
    def __iadd__(self, data):
        "list += data  ||  list.extend(data)"
        self.extend(data)
        return self
    def __or__(self, seperator):
        "list | ' '  ||  ' '.join([str(item) for item in list])"
        ls = [str(item) for item in self]
        return PrizmStr(seperator.join(ls))
    def __and__(self, item):
        "list & item  ||  list.index(item)"
        return self.index(item)
    def __matmul__(self, index: int = 1):
        "list @ index  ||  list.pop(index)"
        return self.pop(index)

class PrizmDict(dict):
    def __lshift__(self, other_dict):
        "dict << other  ||  dict.update(other)"
        self.update(other_dict)
    def __rshift__(self, key):
        "dict >> key || item = dict[key]; del dict[key]"
        item = self[key]
        del self[key]
        return item
    def __isub__(self, keys):
        "dict -= keys  ||  for key in keys: del dict[key]"
        for key in keys:
            del self[key]
        return self
    def __invert__(self):
        "~dict  ||  [(key, dict[key]) for key in dict]"
        return [(key, self[key]) for key in self]

def PrizmStr(str):
    def __ge__(self, string):
        "str >=  other  ||  str = other + str"
        self = self+str(string)
    def __isub__(self, string):
        "str -= chars  ||  str.strip(chars)"
        return self.strip(string)
    def __and__(self, string):
        "str & substr  ||  str.index(substr)"
        return self.index(string)
    def __or__(self, seperator):
        "str | chars  ||  str.split(chars)"
        return PrizmList(self.split(seperator))
    def __iadd__(self, string):
        "str += any  ||  str = str+str(any)"
        return self + str(string)
    def __gt__(self, amount: int):
        "str < num  ||  str.ljust(num)"
        return self.ljust(amount)
    def __lt__(self, amount: int):
        "str > num  ||  str.rjust(num)"
        return self.rjust(amount)
    def __xor__(self, amount: int):
        "str ^ num  ||  f'{str:^literal_num}'"
        while len(" "+self+" ") < amount:
            self = " "+self+" "
        if len(self) < amount:
            self += " "
        return self
    def __truediv__(self, length: int):
        "str / length  ||  str[:length] if len(str) > length else str"
        if len(self) > length:
            return self[:length]
        return self
    def __delitem__(self, index: int):
        "del str[x]  ||  impossible"
        ls = self
        del ls[index]
        self = PrizmStr("".join(ls))
    def __setitem__(self, index: int, char: c):
        "str[x] = y  ||  impossible"
        ls = PrizmList(self)
        ls[index] = char
        self = PrizmStr("".join(ls))

class PrizmFloat(float):
    def __xor__(self, num):
        "float ^ exponent  ||  float ** exponent"
        return self ** num
    def __ixor__(self, num):
        "float ^ exponent  ||  float ** exponent"
        return self ** num
    def __rshift__(self, amount: int):
        "float << amount  ||  float.round(amount)"
        return self.round(amount)
    def __getitem__(self, index: int):
        "float[digit]  ||  str(float)[digit]"
        return str(self)[index]

class PrizmInt(int):
    def __xor__(self, num):
        "int ^ exponent  ||  int ** exponent"
        return self ** num
    def __ixor__(self, num):
        "int ^ exponent  ||  int ** exponent"
        return self ** num
    def __getitem__(self, index: int):
        "int[digit]  ||  str(int)[digit]"
        return str(self)[index]
