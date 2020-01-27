gens = {
    "a": "alpha",
    "b": "beta",
    "d": "pre-alpha",
    "z": "pre-pre-alpha"
}

__ver__ = "0.1.7.6z"
#major.minor.bugfix.smolfix

__gen__ = "release"
if __ver__[-1] in gens:
    __gen__ = gens[__ver__[-1]]

__ls__ = []
for c in __ver__:
    if c != ".":
        __ls__.append(c)

"""
This file just provides version data, nothing to see here
"""
