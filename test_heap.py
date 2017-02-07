#!/usr/bin/python
from __future__ import print_function
import random
import sys
import unittest
from heapdict import heapdict
try:
    # Python 3
    import test.support as test_support
except ImportError:
    # Python 2
    import test.test_support as test_support

N = 100


class TestHeap(unittest.TestCase):

    def check_invariants(self, h):
        # the 3rd entry of each heap entry is the position in the heap
        for i, e in enumerate(h.heap):
            self.assertEqual(e[2], i)
        # the parent of each heap element must not be larger than the element
        for i in range(1, len(h.heap)):
            parent = (i - 1) >> 1
            self.assertLessEqual(h.heap[parent][0], h.heap[i][0])

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
        h, pairs, _ = self.make_data()
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
            _, v = h.popitem()
            self.assertEqual(v, 0)
            self.check_invariants(h)

    def test_peek(self):
        h, pairs, _ = self.make_data()
        while pairs:
            v = h.peekitem()[0]
            h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2[0])
        self.assertEqual(len(h), 0)

    def test_iter(self):
        h, _, d = self.make_data()
        self.assertEqual(list(h), list(d))

    def test_keys(self):
        h, _, d = self.make_data()
        self.assertEqual(list(sorted(h.keys())), list(sorted(d.keys())))

    def test_values(self):
        h, _, d = self.make_data()
        self.assertEqual(list(sorted(h.values())), list(sorted(d.values())))

    def test_del(self):
        h, pairs, _ = self.make_data()
        k, v = pairs.pop(N//2)
        del h[k]
        while pairs:
            v = h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2)
        self.assertEqual(len(h), 0)

    def test_change(self):
        h, pairs, _ = self.make_data()
        k, v = pairs[N//2]
        h[k] = 0.5
        pairs[N//2] = (k, 0.5)
        pairs.sort(key=lambda x: x[1], reverse=True)
        while pairs:
            v = h.popitem()
            v2 = pairs.pop(-1)
            self.assertEqual(v, v2)
        self.assertEqual(len(h), 0)

    def test_clear(self):
        h, _, _ = self.make_data()
        h.clear()
        self.assertEqual(len(h), 0)


def test_main(verbose=None):
    test_classes = [TestHeap]
    test_support.run_unittest(*test_classes)

    # verify reference counting
    if verbose and hasattr(sys, "gettotalrefcount"):
        import gc
        counts = [None] * 5
        for i in range(len(counts)):
            test_support.run_unittest(*test_classes)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)


if __name__ == "__main__":
    test_main(verbose=True)
