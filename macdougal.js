b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
b58_dcmap  = '123456789abcdefghjklmnpqrstuvwxyz!)0(=/\,i;?"_o}{@+|*.: -~'

#It looks like I can import these lines of python directly into javascript...
for(x = 0; x < 58; x++)
    console.log(b58_digits[x] + " | " + b58_dcmap[x])
