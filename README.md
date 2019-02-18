# Usage
```
Examples:
./unspendable.py adfadfadfa 1 0
./unspendable.py adfadfadfa 2 3
./unspendable.py adfadfadfa 3 6
./unspendable.py adfadfadfa 4 8
./unspendable.py adfadfadfa D 31 
./unspendable.py adfadfadfa R 61
./unspendable.py adfadfadfa hH 100
./unspendable.py adfadfadfa "mv" 111

Returns:
1adfadfadfaXXXXXXXXXXXXXXXXXYVEsgt
2adfadfadfaXXXXXXXXXXXXXXXXXYN9qBS
3adfadfadfaXXXXXXXXXXXXXXXXXX27fry
4adfadfadfaXXXXXXXXXXXXXXXXXXoPjaP
DadfadfadfaXXXXXXXXXXXXXXXXXajVtc6
RadfadfadfaXXXXXXXXXXXXXXXXXdHY8F7
hHadfadfadfaXXXXXXXXXXXXXXXXc6hvbK
mvadfadfadfaXXXXXXXXXXXXXXXXcZXiuR

Note: 
Fiddle with the second number until it perfectly hits:

./unspendable.py adfadfadfa D 31   <--- 31 is the magic number here
DadfadfadfaXXXXXXXXXXXXXXXXXajVtc6
./unspendable.py SuchLostCoin D 31  <---- 31 gets the first character right, so you are close
DrFDgT7AbPGbbxfcYwrr1eoKA2nUHkQawt
./unspendable.py SuchLostCoin D 30  <---- a small change fixes the issue
DSuchLostCoinXXXXXXXXXXXXXXXYhdUpU

In the original (awesome) code, only Bitcoin was supported.  This will probably work for many currencies, you can test out the address with your wallet software.

```

