from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School, Classroom, Teacher, Student
from ...serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'gender', 'classroom__school', 'classroom']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['classroom'] = ClassroomSerializer(instance.classroom).data
        return response