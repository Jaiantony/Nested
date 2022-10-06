from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')
router.register('category', CategoryViewSet, basename="category")
router.register('module', ModuleViewSet, basename='module')
router.register('submodule', SubModuleViewSet, basename='submodule')
router.register('quiz', QuizViewSet, basename='quiz')
router.register('answer', AnswerViewSet, basename='answer')
router.register('question', QuestionViewSet, basename='question')
router.register('project', ProjectViewSet, basename='project')
urlpatterns = [
    path('', include(router.urls)),
    # path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>', QuizQuestion.as_view(), name='questions'),

]
