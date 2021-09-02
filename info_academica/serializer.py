from rest_framework import serializers
from .models import InfoAcademica
from .models import AcademicGroup
from .models import RecreativeActivity
from .models import Schedule

class AcademicGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicGroup
        fields ='__all__'

class RecreativeActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecreativeActivity
        fields ='__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields ='__all__'

class InfoAcademicaSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(read_only = True, source='schedule_set', many=True)
    academicGroups = AcademicGroupSerializer(read_only=True, source="academicgroup_set", many=True)
    recreativeActivities = RecreativeActivitySerializer(read_only=True, source="recreativeactivity_set", many=True)

    class Meta:
        model = InfoAcademica
        fields = "__all__"

