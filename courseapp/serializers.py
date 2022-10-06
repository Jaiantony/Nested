from rest_framework import serializers
from .models import *


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'course_id')


class Moduleserializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class SubModuleserializer(serializers.ModelSerializer):
    class Meta:
        model = SubModule
        fields = '__all__'


class Course_serializer(serializers.ModelSerializer):
    category = Categoryserializer(read_only=True, many=True)  # serializer relationship for Category
    module = Moduleserializer(read_only=True, many=True) # serializer relationship for Module
    submodule = SubModuleserializer(read_only=True, many=True)   # serializer relationship for Submodule

    class Meta:
        model = Course
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ('title', 'course_id')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text', 'is_right')


# class RandomQuestionSerializer(serializers.ModelSerializer):
#     answer = AnswerSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Question
#         fields = [
#             'title', 'answer',
#         ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)   # serializer relationship for Answer
    quizzes = QuizSerializer(read_only=True)  # serializer relationship for Quizzes

    class Meta:
        model = Question
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
