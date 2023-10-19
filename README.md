# Purpose

The original unspendable code was used to create "obviously unspendable" cryptocurrency addresses. An example is 
described here:

https://bitcoin.stackexchange.com/questions/35842/is-it-actually-possible-to-create-a-verifiably-unspendable-address

The referenced address is "1BitcoinEaterAddressDontSendf59kuE". Bitcoin addresses must follow certain rules. They often start with the number 1 and the last six characters appear to be random (they aren't). This address is meant as an instruction: "Bitcoin Eater, don't send". Any crypto transaction sent to this address is understood to be "burned" or not retrievable. This is because the address was constructed in an special way that does not have a private key. If it did have a private key, it would not contain such an obvioulsly readable statement. This particular address would normally take a significant amount to time to find (thousands if not millions of years).

Obviously unspendable addresses are different from "vanity addresses" which contain a short word. These addresses tend to use every available character in their message.

This code set creates a standardized set of character replacements which can represent natural language in a much more exact way. The exact mapping presented here is known as "MacDougal". The macdougal.js script prints out the simple substitution table.


# Usage


Usage: ./unspendable.py [prefix] [body]


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

October/19/2023

The character mapping scheme that we are calling "MacDougal" contains one other element. The first character of the address is determined by the currency. Bitcoin requires "1", "2", etc. while Dogecoin and Digibyte accept "D". In the python script (as imperfect as it is), not all second characters are supported. The code throws up jibberish sometimes. Rather than fix this, I just leaned into it and assigned a special meaning to the second character. The third character is always "x". So the second characters that I use are:

A,B,C,D,E

Thus, in Dogecoin, we have: DAx.... DBx..... DCx..... DDx.... DEx....

Here is what they mean. 

DAx: This is a reference to a real person, so it would be their name:

DAxDAViDxBoWiEzzz

DBx: This is a reference to the transport mechanism:

DBxYoUTUBEvCoMzzz

DCx: This is the subject and is often sent by itself if from a smart phone:

DCxGoLDENxYEARSzzz

DDx and DEx: These are uses to represent a first version IPFS address cut in half.

These are rarely used because if you run dogecoind or digibyted (or any similar daemon), you send an IPFS address in the OP_RETURN field without having to go through the permutation of hacking into this range. After all, the DAx, DBx, and DCx ranges transform a standard block explorer into a Web3 entry point because you can drill and spin through them like a crude database:

https://digibyteblockexplorer.com/address/DBxYoUTUBEvCoMzzzzzzzzzzzzzzZ31xMU

But you would never search on the first 1/2 of an IPFS address (unless you decide that this is of value). 

If you are using BSV (Satoshi Vision), this OP_RETURN field becomes an entire universe of possibilities because the size of the field is not limited to 80 characters. For other currencies you could store values in Base64. This would get you more space than ascii and totally encompasses Base58, but this field is really beyond the scope of this tool.

Thanks 

John Rigler
john@rigler.org

I use LinkedIn like Facebook, so that is the best way to find me.

https://www.linkedin.com/in/jrigler/

```
