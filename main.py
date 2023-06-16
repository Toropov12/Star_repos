'''def strum(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)
strum('caac')'''
def strum(c):
   if c == c[::1]:
       return True
   else:
       return False
print(strum('ababa'))
