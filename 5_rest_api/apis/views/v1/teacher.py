from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School, Classroom, Teacher, Student
from ...serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'gender', 'classrooms__school', 'classrooms']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['classrooms'] = ClassroomSerializer(instance.classrooms.all(), many=True).data
        return response