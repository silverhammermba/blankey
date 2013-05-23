from numbth import gcd, lcm


#class lc_iterator():
#    """
#    Dangerous iterator with no StopIteration
#    """
#    def __init__(self, lc):
#        self.lc = lc
#        self.state = self.lc.residue
#    def __next__(self):
#        temp = self.state
#        self.state += self.lc.modulus
#        return temp

class lc:
    """Linear Congruence python object.
    Simple object for linear congruences.

    Usage Example:
    >>> x = lc(1,4)
    >>> x
    x = 1 (mod 4)
    >>> 1 == x # 1 in x?
    True
    >>> 5 == x # 5 in x?
    True
    >>> 142 == x # 142 in x?
    False
    """
    def __init__(self, residue, modulus):
        self.residue = residue
        self.modulus = modulus
        if modulus <= 0 or type(modulus) != int:
            raise ValueError('modulus must be a positive integer')

    def __repr__(self):
        return "x = %d (mod %d)" % (self.residue, self.modulus)

    def __eq__(self, other):
        if type(other) == int:
            return other % self.modulus == self.residue
        elif type(other) == lc:
            return (self.residue == other.residue and self.modulus ==
                    other.modulus)
        else:
            return False

#    def __iter__(self):
#       return lc_iterator(self)


class lcs(list):
    """Linear Congruence Set python object.
    Initialize with a list of lc's or a list of 2-long lists.

    Basic object is a list of lc's, with a bit of extra functionality.

    Usage Examples:
    >>> a = lc(1,3)
    >>> b = [2,3]
    >>> c = lc(0,3)
    >>> s = lcs(a,b)
    >>> s
    [x = 1 (mod 3), x = 2 (mod 3)]
    >>> print(s)
    x = 1 (mod 3)
    x = 2 (mod 4)
    LCM: 3
    >>> s.is_covering()
    Missing:
    [0]
    False
    >>> s.append([0,3])
    >>> s.is_covering()
    True
    """
    __old_append = list.append  # want to make sure when we append, we can cast
                                # to lc on the fly

    def __init__(self, *elts):
        if list in [type(e) for e in elts]:
            elts = [e if type(e) == lc else lc(*e) for e in elts]

        self.elts = list(elts)

        for e in elts:
            self.__old_append(e)

    def append(self, e):
        if type(e) == list:
            if len(e) == 2:
                    self.__old_append(lc(*e))
            else:
                raise ValueError("can only have lc's or lists of length 2 as"
                                 "elements")
        elif type(e) == lc:
            self.__old_append(e)
        else:
            raise ValueError("can only have lc's or lists of length 2 as"
                             "elements")

    def get_lcm(self):
        """Returns the least common multiple of the moduli of the system of
        linear congruences
        """
        moduli = [e.modulus for e in self]
        return lcm(*moduli)

    def is_covering(self, return_missing=False):
        """Boolean return of whether a set of linear congruences is a covering
        system or not.
        """
        missing = [i for i in range(self.get_lcm()) if i not in self]
        if len(missing) == 0:
            return True
        else:
            print("Missing:\n%s" % missing)
            return False if not return_missing else missing

    def __str__(self):
        s = '\n'.join([e.__repr__() for e in self])
        s += '\n\nLCM: %d\n' % self.get_lcm()
        return s

a = lc(1, 4)
b = [2, 4]
c = lc(3, 4)

#s = lcs(a,b,c)
