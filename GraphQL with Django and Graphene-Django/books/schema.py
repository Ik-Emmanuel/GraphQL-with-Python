import graphene
from graphene_django import DjangoObjectType, DjangoListField
from . models import Books

class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields =  ("id", "title", "excerpt")


class Query(graphene.ObjectType):
    #query key
    #custom resolver definition
    # all_books = graphene.List(BooksType)

    # def resolve_all_books(root, info):
    #     return Books.objects.all()

    #working without resolvers 
    all_books = DjangoListField(BooksType)

schema = graphene.Schema(query=Query)



# type Books {
#     id: id
#     title: String
#     excerpt: String
# }

