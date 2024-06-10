from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School, Classroom, Teacher, Student
from ...serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, StudentSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['classroom_count'] = instance.classrooms.count()
        response.data['teacher_count'] = Teacher.objects.filter(classrooms__school=instance).distinct().count()
        response.data['student_count'] = Student.objects.filter(classroom__school=instance).distinct().count()
        return response

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['teachers'] = TeacherSerializer(instance.teachers.all(), many=True).data
        response.data['students'] = StudentSerializer(instance.students.all(), many=True).data
        return response