from django.urls import path
from graphene_django.views import GraphQLView
from books.schema import schema



urlpatterns = [
    #only 1 endpoint to access Graphql
    #graphiql=True specifies that your want the graphcal interface (the playground)
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
]