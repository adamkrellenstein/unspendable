#! /usr/bin/env python3

import sys
import hashlib
import binascii

dhash = lambda x: hashlib.sha256(hashlib.sha256(x).digest()).digest()
b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
b58_dcmap  = '123456789abcdefghjklmnpqrstuvwxyz!)$(=/\.i;?"~o}{@~|*,: -~'
b58_sft    = '         ABCDEFGHJLKMNPQRSTUVWXYZ < >    I    O][         '

# b58_dcmap is the dimecash mapping
# Dimecash seeks to create an language where all of the readable text
# is capitalized, the small letter x is uses for space, and other 
# various conventions until all of the ascii characters are represented
# the small s will be a shift that will enable b58_sft

# In this version of the code, everything will be interpreted this way
# and the name field can include spaces if it is double-quoted

seeds = [ '0','3','5','7','10','12','15','17','20','22','25',
         '27','30','32','35','37','40','42','45','48','50',
         '53','55','58','60','63','65','68','70','73','76',
         '78','80','83','85','88','91','93','96','98','101',
         '103','106','108','111','113','116','118','121',
         '123','126','128','131','134','136','139','141','144' ]

# The seeds aren't perfect, the second character will 
# sometimes mean that the seed fails, I will
# have to run this again with a 1 and a z in each
# case, these seeds were found for AAAA,BBBB,CCCC,DDDD
# which was a bit arbitrary

# This may also be why the padding messes up at the 
# end sometimes, and why the original code makes 
# reference to bad checksums on line 150ish

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


def generate (prefix_string, name):

    # Find the prefix_bytes from the first character of the prefix
    first_char = prefix_string[0]
    seed_ref = b58_digits.find(first_char)
    prefix_char_seed = int(seeds[seed_ref])
    prefix_bytes = (prefix_char_seed).to_bytes(1, 'big')


    # Special Kludge for my favorite dogecoin range
    # I will come up with something more elegant later

    if (prefix_string == '9s'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9t'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9u'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9v'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9w'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9x'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9y'):
         prefix_bytes = b'\x16'
    elif (prefix_string == '9z'):
         prefix_bytes = b'\x16'

    # Pad and prefix.
    prefixed_name = prefix_string + name 
    partly_padded_prefixed_name = prefixed_name.ljust(28,'z')
    # partly_padded_prefixed_name = prefixed_name
    # This seems to work as two sets, see comments below
    padded_prefixed_name = partly_padded_prefixed_name.ljust(34, 'X')

    # What I really want to do is pad the prefix
    # name with a small z, but doing it here
    # seems to give inconsistent results
    # Padding with just a capital Z works
    # but is not what I want to use

    # EDDDDDDDDDDE11111111111111111Gk54D
    # FDDDDDDDDDDE111111111111111123L5F2
    # GDDDDDDDDDDE11111111111111114d4Hd3
    # HDDDDDDDDDDE11111111111111111U5ouh
    # JDDDDDDDDDDE11111111111111111LQNJo
    # KDDDDDDDDDDDzzzzzzzzzzzzzzzzzsdadA
    # mvDDDDDDDDDDE1111111111111111CW9AV

    # EDDDDDDDDDDDZZZZZZZZZZZZZZZZeMDHXH
    # FDDDDDDDDDDDZZZZZZZZZZZZZZZZZwwLbi
    # GDDDDDDDDDDDZZZZZZZZZZZZZZZZcrgkxC
    # HDDDDDDDDDDDZZZZZZZZZZZZZZZZZpM6E8
    # JDDDDDDDDDDDZZZZZZZZZZZZZZZZbgYpBG
    # KDDDDDDDDDDDZZZZZZZZZZZZZZZZd79WxX
    # mvDDDDDDDDDDDZZZZZZZZZZZZZZZYLf2rF

    # I have had success simply calculating
    # this elsewhere.  This is a strange bug

    # Decode, ignoring (bad) checksum.
    decoded_address = base58_decode(padded_prefixed_name, prefix_bytes)

    # Re-encode, calculating checksum.
    address = base58_check_encode(decoded_address, prefix_bytes)

    # Double-check.
    assert base58_decode(address, prefix_bytes) == decoded_address

    return address


if __name__ == '__main__':

    prefix_string = sys.argv[1]

    list = split(sys.argv[2])

    cnt = 0
    for n, c in enumerate(list):
       x = b58_dcmap.find(c)
       if x!= -1:
          list[cnt] = b58_digits[x]
       if c == 'I':
          list[cnt] = 'i'
       cnt=cnt+1

    # DCx is hard-coded in next steps
    # are to fix this to support
    # other code sets such as
    # for Dogecoin: 9s - 9z and the A ranges

    name = ''.join(list)
    print(generate(prefix_string, name))
