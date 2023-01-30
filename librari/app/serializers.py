from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Book, Biography


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['first_name', 'last_name']
        #exclude = ['first_name']


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class BookModelSerializer(HyperlinkedModelSerializer):
    author = ArticleModelSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
