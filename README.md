# Usage
```
To see a sample, load the test environment into the shell and run the 
unspendable_test function:

. test/test.bash
unspendable_test

=> unspendable_test
1DDxxDDDDDDDDDzzzzzzzzzzzzzzaGWgks
2DDxxDDDDDDDDDzzzzzzzzzzzzzzWGXZh6
EDDxxDDDDDDDDDzzzzzzzzzzzzzzV1ZCQW
...
FDDxxDDDDDDDDDzzzzzzzzzzzzzzVjutFL
GDDxxDDDDDDDDDzzzzzzzzzzzzzzaAVXEU
HDDxxDDDDDDDDDzzzzzzzzzzzzzzWVFTan
JDDxxDDDDDDDDDzzzzzzzzzzzzzzV8f3k9
KDDxxDDDDDDDDDzzzzzzzzzzzzzzYxTgTt
mvDDxxDDDDDDDDDzzzzzzzzzzzzzc3bLcu

Usage: ./unspendable.py [prefix] [body]

The code is now on version 2.0, but is backwards
compatible with version 1:

(version 1, you have to specify the seed and no character
substition or help.  It just fails if you type a capital I)

=> ./unspendable.py D DDDD 30
DDDDDzzzzzzzzzzzzzzzzzzzzzzzT1kYx9

(version 2, no seed required and many ascii characters 
are supported.  I haven't included a way to translate
back yet, but after a while, you can read this stuff
without any help.)

=> ./unspendable.py DCx "this is the stuff"
DCxTHiSxiSxTHExSTUFFzzzzzzzzbSG1oo

Apr/27/2021

I have added un3.cgi and unspendable.html. The cgi script goes in
your /usr/lib/cgi-bin directory. Its a script. Yea, deal with it.


```
