def __init__(self, text, author):
self.author = author
self.text = text
class Book:
def __init__(self, name, authors):
self.name = name
self.authors = authors
class Article:
def __init__(self, name, author):
self.name = name
self.author = author


class AuthorSerializer(serializers.Serializer):
name = serializers.CharField(max_length=128)
birthday_year = serializers.IntegerField()
author = Author('Грин', 1880)
serializer = AuthorSerializer(author)
print(serializer.data) # {'name': 'Грин', 'birthday_year': 1880}
print(type(serializer.data))
#
'rest_framework.utils.serializer_helpers.ReturnDict'>
from rest_framework.renderers import JSONRenderer
renderer = JSONRenderer()
json_bytes = renderer.render(serializer.data)
print(json_bytes)
b'{"name":"\xd0\x93\xd1\x80\xd0\xb8\xd0\xbd","birthday_year":1880}'
print(type(json_bytes)) # <class 'bytes'>
<class
#
from rest_framework.parsers import JSONParser
stream = io.BytesIO(json_bytes)
data = JSONParser().parse(stream)
print(data) # {'name': 'Грин', 'birthday_year': 1880}
print(type(data)) # <class 'dict'>