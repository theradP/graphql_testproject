from django.conf.urls import url, include
from graphene_django.views import GraphQLView
from django.urls import path, include

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True)),

]