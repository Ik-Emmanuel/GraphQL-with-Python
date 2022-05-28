from unicodedata import category
import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from pkg_resources import require
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text", "is_right")



class Query(graphene.ObjectType):
    all_quizzes = DjangoListField(QuizzesType)  
    question_types = DjangoListField(QuestionType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)




class CategoryMutation(graphene.Mutation):
    #used to defined the resposne of the mutation
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True) 


    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()

        return CategoryMutation(category=category)

class CategoryUpdate(graphene.Mutation):
    #used to defined the resposne of the mutation
    category = graphene.Field(CategoryType)

    class Arguments:
        id =  graphene.ID()
        name = graphene.String(required=True) 

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()

        return CategoryMutation(category=category)


class CategoryDelete(graphene.Mutation):
    #used to defined the resposne of the mutation
    category = graphene.String()

    class Arguments:
        id =  graphene.ID()

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()


        return f"Category with ID:{id}, has been deleted"





class QuizzesMutation(graphene.Mutation):
    # category_id = graphene.Int(required=True) 
    category_name = graphene.String(required=True) 
    
    class Arguments:
        title = graphene.String(required=True)

    quiz = graphene.Field(QuizzesType)

    def mutate(root, info, category_name, title):
        category = Category.objects.get(name__icontains=category_name)
        quiz = Quizzes.objects.create(title=title, category=category)
        return QuizzesMutation(quiz=quiz)



class Mutation(graphene.ObjectType):
    create_category = CategoryMutation.Field()
    update_category = CategoryUpdate.Field()
    delete_category = CategoryDelete.Field()
    create_quizzes = QuizzesMutation.Field()




schema = graphene.Schema(query=Query, mutation=Mutation)




# ================================ Query =============================== 
#    query {
#  allQuizzes{
#     title
#   }
# }

#     query {
#  questionTypes{
#     title
#   }
# }

# working with arguments
#     {
# allQuestions(id:2){
#   title
# }
# }



# ======================= Mutations ====================
# mutation {
#    createCategory(name:"Music" ){
#     category{
#       name
#     }
#   }
# }


# mutation{
#    createQuizzes (title:"Dentistry", categoryName:"Health"){
#     quiz{
#       title
#       category{
#         id
#         name
#       }
#     }
    
#   }
# }

# mutation{
#   updateCategory(id: 8, name: "Music Production"){
#     category{
#       name
#     }
#   }
# }


# query{
#   allQuizzes{
#     title
#     category{
#       name
#     }
#   }
# }


# mutation{
#    createQuizzes (title:"3D modeling", categoryName:"Animations"){
#     quiz{
#       title
#       category{
#         id
#         name
#       }
#     }
    
#   }
# }
