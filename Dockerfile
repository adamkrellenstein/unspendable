FROM python:3
ADD unspendable.py /
CMD [ "python","unspendable/unspendable.py","D","DDD","30" ]
