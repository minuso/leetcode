class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.cur = self.iter.next() if self.iter.hasNext() else None # for peeking

    def peek(self):
        return self.cur
        
    def next(self):
        res = self.cur
        self.cur = self.iter.next() if self.iter.hasNext() else None
        return res
        
    def hasNext(self):
        return self.cur != None