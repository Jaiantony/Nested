from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField(null=False)
    thumbnail = models.ImageField(upload_to='media/thumbnails')
    active = models.BooleanField(default=True)
    language = models.CharField(max_length=100, null=False)
    requirements = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    outcome = ArrayField(models.CharField(max_length=256), blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']  # inorder to overcome inconsistent results in Pagination


class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    description = models.TextField(null=False)
    project_resource = models.FileField(upload_to='media/project_resource')
    course_id = models.ForeignKey(Course,
                                  related_name='project',
                                  on_delete=models.CASCADE)  # Referenced with Course Table
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    category_name = models.CharField(max_length=256, null=False)
    course_id = models.ForeignKey(Course,
                                  related_name='category',
                                  on_delete=models.CASCADE)  # Referenced with Course Table

    def __str__(self):
        return self.category_name


class Module(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    module_name = models.CharField(max_length=256, null=False)
    course_id = models.ForeignKey(Course,
                                  related_name='module',
                                  on_delete=models.CASCADE)  # Referenced with Course Table
    created = models.DateTimeField(auto_now_add=True)
    video_count = models.PositiveIntegerField()
    duration = models.DurationField()

    def __str__(self):
        return self.module_name


class SubModule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    sub_module_name = models.CharField(max_length=256, null=False)
    course_id = models.ForeignKey(Course,
                                  related_name='submodule',
                                  on_delete=models.CASCADE) # Referenced with Course Table
    duration = models.DurationField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    module_id = models.ForeignKey(Module,
                                  related_name='module',
                                  on_delete=models.CASCADE) # Referenced with Module Table
    resource = models.FileField(upload_to='media/resource')
    thumbnail = models.ImageField(upload_to='media/thumbnails')

    def __str__(self):
        return self.sub_module_name


class Quizzes(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256)
    course_id = models.ForeignKey(Course,
                                  related_name='quizzes',
                                  on_delete=models.CASCADE) # Referenced with Course Table
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(Updated):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    Question_choice = (
        ('MCQ', 'Multiple Choice'),
    )
    quiz = models.ForeignKey(
        Quizzes, related_name='question',
        on_delete=models.DO_NOTHING) # Referenced with Quizzes Table
    question = models.CharField(max_length=256)
    date_created = models.DateTimeField(
        auto_now_add=True)
    is_active = models.BooleanField(
        default=False, )
    is_mcq = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Answer(Updated):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    question = models.ForeignKey(
        Question, related_name='answer',
        on_delete=models.DO_NOTHING)  # Referenced with question Table
    answer_text = models.CharField(
        max_length=256)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
