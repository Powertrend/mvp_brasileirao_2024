import strawberry
from api.resolvers import Query
from api.mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
