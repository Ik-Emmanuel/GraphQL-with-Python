# GraphQL-Blog-API-with-FastAPI
A blog app API built with GraphQL, PostgreSQL and FastAPI using strawberry


# Make  GraphQl Queries 

- Get all posts (include needed fields )

` {
  blog{
   id
   title
    author
   content
    timeCreated
  }
}`



- Create a post 
` mutation{
  addPost(title:"The New dawn", content:"This right here signifies the start of new things", author:"Mac Anthony")
   {
     title
    author
    ... and any other field needed in response model
   }
 }`
