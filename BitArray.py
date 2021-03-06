""" An efficient class for representing a boolean array with a single integer """

from collections import MutableSequence

class BitArray(MutableSequence):

    def __init__(self, arr=0):
        if isinstance(arr, int):
            self.arr = arr
        else: # convert from list to binary to int
            self.arr = int(''.join(map(str, arr)), 2)

    def __getitem__(self, i):
        if self.__len__() <= i:
            raise IndexError
        else:
            return self.arr & (1 << i) > 0

    def __setitem__(self, i, val):
        self.arr = self.arr | (bool(val) << i)

    def __delitem__(self, i):
        self.arr = self.arr ^ (self.__getitem__(i) << i)

    def __len__(self):
        return self.arr.bit_length()

    def __str__(self):
        return bin(self.arr)[2:][::-1]

    def insert(self, i, val):
        self.arr = ((self.arr >> i << (i + 1)) # bits i + 1 to end
                    | val << i # bit i
                    | (self.arr & (1 << i - 1) )) # bits 0 to i - 1

def main():
    x = BitArray()

    x[5] = 1
    x[4] = 1
    x[7] = 1

    assert(x[5] == True)
    assert(x[3] == False)

    del x[7]
    assert([int(el) for el in x] == [0, 0, 0, 0, 1, 1])

    x.insert(3, 1)
    assert([int(el) for el in x] == [0, 0, 0, 1, 0, 1, 1])

    print("All tests passed!")

if __name__ == "__main__": main()
