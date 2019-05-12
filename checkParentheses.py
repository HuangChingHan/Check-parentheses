# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:29:46 2019

This is checking balanced parentheses.
"""
from pythonds.basic import Stack

def parCheck(symbolString):
    pos = 0
    s = Stack()
    label = True
    while pos < len(symbolString) and label:
        symbol = symbolString[pos]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                label = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    label = False
        pos = pos + 1
    
    if s.isEmpty() and label:
        return True
    else:
        return False
    
def match(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(parCheck('(((}))'))
