# Usage
```


Usage: ./unspendable.py [prefix] [body]

DAxAhBhCvxDwEyFzzzzzzzzzzzzzYmxRjP
DBxAhBhCvxDwEyFzzzzzzzzzzzzza74Amo
DCxAhBhCvxDwEyFzzzzzzzzzzzzzZbP8fn
DExAhBhCvxDwEyFzzzzzzzzzzzzzXFfneb
DFxAhBhCvxDwEyFzzzzzzzzzzzzzZDGMbY
DGxAhBhCvxDwEyFzzzzzzzzzzzzzathuAJ
DHxAhBhCvxDwEyFzzzzzzzzzzzzzXgXcva
DJxAhBhCvxDwEyFzzzzzzzzzzzzzUcggJ5
DKxAhBhCvxDwEyFzzzzzzzzzzzzzXQtusk
DLxAhBhCvxDwEyFzzzzzzzzzzzzzW4E7oZ
DMxAhBhCvxDwEyFzzzzzzzzzzzzzVTAJWk
DNxAhBhCvxDwEyFzzzzzzzzzzzzzZXiSyS
DPxAhBhCvxDwEyFzzzzzzzzzzzzzWHsxgK
DQxAhBhCvxDwEyFzzzzzzzzzzzzzXqVkeM
DRxAhBhCvxDwEyFzzzzzzzzzzzzzY6MWaF
DSxAhBhCvxDwEyFzzzzzzzzzzzzza7nwwZ
DTxAhBhCvxDwEyFzzzzzzzzzzzzzWSmXBA

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

May/22/2022

It is important to note that using the second variable only adds 
the somewhat arbitrary DiMECASH substitution. If you figure out
how you want to craft your entire message in a different way and
are unhappy with the character set that I chose, then don't use
the second field, but put everything in the first field.

The first and second characters are ones that I have proven to work
so for example: un DiX doesn't work but DTiX does. If you muck with
the seeds, you might be able to fix this, but the last six characters
will change. Also, I want to keep this simple (because I really don't 
like python that much) so I will try to make as few changes to this as
possible and do error handling with php or bash.

You don't have to limit yourself to the "D" range (dogecoin,digibyte,verge, etc)

Bitcoin, Tron, all sort of other stuff is possible. You can even create
longer words for currencies such as Tezos or Zcash that have a different 
length. If you do, then please submit a pull request and I will consider your
changes.

Thanks 

John Rigler
john@rigler.org (alias)
john.rigler@protonmail.com

I use LinkedIn like Facebook, so that is the best way to find me.

https://www.linkedin.com/in/jrigler/

Also check out my latest project: https://ledger.church/broadcast 


```
