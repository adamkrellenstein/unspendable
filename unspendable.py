#! /usr/bin/env python3

import sys
import hashlib
import binascii

dhash = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()
b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
b58_sub    = '.01234567abcdefghjklmnpqrstuvwxyz!)$(=/\_i;?"~O}{~~|*,: -+'
# These are the basic substitutions of dimecash (https://dime.cash)
# This allows for a broad set of characters to be
# These are the basic substitutions of dimecash
# This allows for broad set of characters to be
# easily encoded and understood
# 
# In some cases, the substitution is to look like
# the character it represents
# with small b resembling )
# and small d representing (
#
# The numbers are in a code known as shoctal
# which is octal shifted up two numerals
# and 1 representing decimal or period
# This system was first devised to work with
# Advanced Satoshi Codes so that a block 
# of meaning could be distinct from an empty set of zeros
#
# The s for shift and n for single quote (as opposed to
# m for double quote) are still a work in progress
# 
# bash functions can easily be coded into this without
# having to shift

b58_sft    = '89       ABCDEFGHJLKMNPQRSTUVWXYZ < >    I    O][         '

# Above is the next set of possible characters
# I would avoid capitals unless necessary

keys = [ '0','2','5','7','10','12','15','17','20','22','25',
         '27','30','32','35','37','40','42','45','48','50',
         '53','55','58','60','63','65','68','70','73','75',
         '78','80','83','85','88','91','93','96','98','101',
         '103','106','108','111','113','116','118','121',
         '123','126','128','131','134','136','139','141','144' ]

# The term keys may not be entirely correct, but these numbers
# map to the b58_digits.  For example D is 30

# Dogecoin: D,AA-AZ,9s-9t
# Litecoin: L,3

def split(word):
    return [char for char in word]

def base58_check_encode(b, version):
    d = version + b
    address = d + dhash(d)[:4]

    # Convert big‐endian bytes to integer
    n = int('0x0' + binascii.hexlify(address).decode('utf8'), 16)

    # Divide that integer into base58
    res = []
    while n > 0:
        n, r = divmod (n, 58)
        res.append(b58_digits[r])
    res = ''.join(res[::-1])

    # Encode leading zeros as base58 zeros
    czero = 0
    pad = 0
    for c in d:
        if c == czero: pad += 1
        else: break
    return b58_digits[0] * pad + res


def base58_decode (s, version):
    # Convert the string to an integer
    n = 0
    for c in s:
        n *= 58
        if c not in b58_digits:
            raise Exception
        digit = b58_digits.index(c)
        n += digit

    # Convert the integer to bytes
    h = '%x' % n
    if len(h) % 2:
        h = '0' + h
    res = binascii.unhexlify(h.encode('utf8'))

    # Add padding back.
    pad = 0
    for c in s[:-1]:
        if c == b58_digits[0]: pad += 1
        else: break
    k = version * pad + res

    addrbyte, data, chk0 = k[0:1], k[1:-4], k[-4:]
    return data


def generate (name, prefix_string , pb):

    prefix_bytes = b'\x00'
    prefix_bytes = bytes(pb)
    prefix_bytes = (pb).to_bytes(1, 'big')

    # Pad and prefix.
    prefixed_name = prefix_string + name
    padded_prefixed_name = prefixed_name.ljust(34, 'z')

    # Decode, ignoring (bad) checksum.
    decoded_address = base58_decode(padded_prefixed_name, prefix_bytes)

    # Re-encode, calculating checksum.
    address = base58_check_encode(decoded_address, prefix_bytes)

    # Double-check.
    assert base58_decode(address, prefix_bytes) == decoded_address

    return address


if __name__ == '__main__':

    ps = sys.argv[1]
    name = sys.argv[2]
    list = split(name)

    cnt = 0
    for n, c in enumerate(list):
       x = b58_sub.find(c)
       if x!= -1:
          list[cnt] = b58_digits[x]
       if c == 'i':
          list[cnt] = 'i'
       cnt=cnt+1

    # DCx is hard-coded in next steps
    # are to fix this to support
    # other code sets such as
    # for Dogecoin: 9s - 9z and the A ranges

    name = "DCx" + ''.join(list)

    padded_name = name.ljust(28,'z')

    index = b58_digits.find(ps)

    print(generate(ps, padded_name , int(keys[index])))

