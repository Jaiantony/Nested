from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Course instances.
    """
    serializer_class = Course_serializer
    pagination_class = StandardResultsSetPagination
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', "price", 'active', 'created', 'updated']
    search_fields = ['^title', '=language']
    ordering_fields = ['created', 'updated']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Category instances.
    """
    serializer_class = Categoryserializer
    queryset = Category.objects.all()


class ModuleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Module instances.
    """
    serializer_class = Moduleserializer
    queryset = Module.objects.all()


class SubModuleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Submodule instances.
    """
    serializer_class = SubModuleserializer
    queryset = SubModule.objects.all()


class QuizViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Quiz instance.
    """
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


# class RandomQuestion(APIView):
#
#     def get(self, request, format=None, **kwargs):
#         question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')
#         serializer = RandomQuestionSerializer(question, many=True)
#         return Response(serializer.data)


class QuizQuestion(APIView):
    """
    An APIView to get Quiz details of single quiz

    """

    def get(self, request, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Answer instances.
    """
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Question instances.
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    """
     A viewset for viewing and editing Project instances.
    """
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
