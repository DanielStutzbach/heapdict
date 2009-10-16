#!/usr/bin/python
from __future__ import print_function
from heapdict import heapdict
import random
import unittest
import sys
try:
    import test.support as test_support # Python 3
except ImportError:
    import test.test_support as test_support # Python 2

N = 100

class TestHeap(unittest.TestCase):
    def check_invariants(self, h):
        for i in range(len(h)):
            self.assertEqual(h.heap[i][2], i)
            if i > 0:
                self.assertTrue(h.heap[h._parent(i)][0] <= h.heap[i][0])

    def make_data(self):
        pairs = [(random.random(), random.random()) for i in range(N)]
        h = heapdict()
        d = {}
        for k, v in pairs:
            h[k] = v
            d[k] = v

        pairs.sort(key=lambda x: x[1], reverse=True)
        return h, pairs, d
    
    def test_popitem(self):
        h, pairs, d = self.make_data()
        while pairs:
            v = h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2)
        self.assertEqual(len(h), 0)

    def test_popitem_ties(self):
        h = heapdict()
        for i in range(N):
            h[i] = 0
        for i in range(N):
            k, v = h.popitem()
            self.assertEqual(v, 0)
            self.check_invariants(h)

    def test_peek(self):
        h, pairs, d = self.make_data()
        while pairs:
            v = h.peekitem()[0]
            h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2[0])
        self.assertEqual(len(h), 0)

    def test_iter(self):
        h, pairs, d = self.make_data()
        self.assertEqual(list(h), list(d))

    def test_keys(self):
        h, pairs, d = self.make_data()
        self.assertEqual(list(sorted(h.keys())), list(sorted(d.keys())))

    def test_values(self):
        h, pairs, d = self.make_data()
        self.assertEqual(list(sorted(h.values())), list(sorted(d.values())))

    def test_del(self):
        h, pairs, d = self.make_data()
        k, v = pairs.pop(N//2)
        del h[k]
        while pairs:
            v = h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2)
        self.assertEqual(len(h), 0)

    def test_change(self):
        h, pairs, d = self.make_data()
        k, v = pairs[N//2]
        h[k] = 0.5
        pairs[N//2] = (k, 0.5)
        pairs.sort(key = lambda x: x[1], reverse=True)
        while pairs:
            v = h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2)
        self.assertEqual(len(h), 0)

#==============================================================================

def test_main(verbose=None):
    from types import BuiltinFunctionType

    test_classes = [TestHeap]
    test_support.run_unittest(*test_classes)

    # verify reference counting
    if verbose and hasattr(sys, "gettotalrefcount"):
        import gc
        counts = [None] * 5
        for i in xrange(len(counts)):
            test_support.run_unittest(*test_classes)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)

if __name__ == "__main__":
    test_main(verbose=True)
