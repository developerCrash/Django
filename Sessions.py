To Check the items stored in Cookie Sessions 

>>> from django.contrib.sessions.models import Session
>>> k = Session.objects.get(pk='xxgojzaboqd821q8cgf6e9zthlalix9s') 
>>> k.get_decoded() 
{'session_key': {'1': {'price': '1000.00'}, '2': {'price': '60.00'}}}
