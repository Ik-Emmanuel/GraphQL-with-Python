from ast import mod
from dataclasses import field
from re import T
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import  GraphQLRouter
from schemas import PostSchema
import typing
import models
from db_config import db_session


db = db_session.session_factory()


@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author: str
    time_created: str

@strawberry.type
class PostMutation:
    title: str
    content: str
    author: str


def get_blogs():
    data = db_session.query(models.Post).all()
    return data


@strawberry.type
class Query:
    blog: typing.List[Post] = strawberry.field(resolver=get_blogs)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_post(self, title:str,  content:str, author:str) -> PostMutation:
        post = PostSchema(title=title, content=content, author=author)
        db_post = models.Post(title=post.title, content=post.content, author=post.author)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        print(f"Adding {title} by {author}")
        return PostMutation(title=title, content=content, author=author)



schema = strawberry.Schema(query=Query, mutation= Mutation)
graphql_app = GraphQLRouter(schema) 


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def root():
    return {"message": " Welcome to graphQL"}


## query for all posts
# {
#   blog{
#     id
#     title
#     author
#     content
#     timeCreated
#   }
# }



#add a new post 

# mutation{
#  addPost(title:"The New dawn", content:"This right here signifies the start of new things", author:"Mac Anthony")
#    {
#     title
#     author
#   }
# }