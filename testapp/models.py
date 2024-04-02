from django.db import models

# Create your models here.
# from django.db import models



class People(models.Model):
    name = models.CharField(max_length = 100)
    about = models.TextField()
    # age = models.IntegerField
    email = models.EmailField()
    # colors = models.ManyToManyField(colors)
    
class PeopleAddress(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE,related_name = 'people_r')
    address = models.TextField()
    
    
    
'''
WITH RELATED NAME

C:\Users\khanz\Desktop\all djngo project\DRW\test-drf\testenv2>python manage.py shell
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from testapp.models import *
>>> obj = People.objects.first()
>>> address_1 = obj.people_r.first()
>>> address_1
<PeopleAddress: PeopleAddress object (1)>
>>> address_1.address 
'fatehganj west bareilly 111'
>>>


'''
'''
WITHOUT RELATED NAME
>>> from testapp.models import *  
>>> obj = People.objects.first()
>>> obj
<People: People object (1)>
>>> obj.name
'people1'
>>> obj.address
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'People' object has no attribute 'address'
>>> first_address = obj.peopleaddress_set.first()
>>> first_address
<PeopleAddress: PeopleAddress object (1)>
>>> first_address.people
<People: People object (1)>
>>> first_address.address
'fatehganj west bareilly 111'
>>>

'''

'''
# Get the People object
obj = People.objects.first()

# Access related PeopleAddress objects
addresses = obj.peopleaddress_set.all()  # 'peopleaddress_set' is the default related name
# You can use 'peopleaddress_set' if you haven't specified a related name for the foreign key field
# Otherwise, use the related name you have defined.

# Iterate through the addresses and print each one
for address in addresses:
    print(address.address)



'''