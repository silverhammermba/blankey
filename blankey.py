#!/usr/bin/env python


from numbth import gcd, lcm


class lc:
    def __init__(self, residue, modulus):
        self.residue = residue
        self.modulus = modulus
        if modulus <= 0 or type(modulus) != int:
            raise ValueError('modulus must be a positive integer') 

    def __repr__(self):
        return "x = %d (mod %d)" % (self.residue, self.modulus)

    def __eq__(self, other):
        if type(other) == int:
            return int % self.modulus == self.residue
        elif type(other) == lc:
            return (self.residue == other.residue and self.modulus == other.modulus)
        else:
            return False

        
