from rest_framework import serializers
from .models import AcademicInfo
from .models import TermSummary
from .models import Classes
from .models import BasicInfo
from .models import LibraryHistory
from .models import TransactionLibrary

class TermSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TermSummary
        fields ='__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields ='__all__'

class AcademicInfoSerializer(serializers.ModelSerializer):
    summaries = TermSummarySerializer(read_only=True, source='termsummary_set', many=True)
    classes = ClassesSerializer(read_only=True, source='classes_set', many=True)
    class Meta:
        model = AcademicInfo
        fields ='__all__'

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = '__all__'

class TransactionLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLibrary
        fields = '__all__'

class LibraryHistorySerializer(serializers.ModelSerializer):
    transactions = TermSummarySerializer(read_only=True, source='transactionlibrary_set', many=True)

    class Meta:
        model = LibraryHistory
        fields ='__all__'
