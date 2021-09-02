from rest_framework import serializers
from .models import LibUse
from .models import TranLib
from .models import LibRes
from .models import AzUse
from .models import TranAz
from .models import AzRes
from .models import RepoUse
from .models import TranRepo
from .models import RepoRes

class TranLibSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranLib
        fields ='__all__'

class LibResSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibRes
        fields ='__all__'

class LibUseSerializer(serializers.ModelSerializer):
    trans = TranLibSerializer(read_only = True, source='tranlib_set', many=True)

    class Meta:
        model = LibUse
        fields = "__all__"

class TranAzSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranAz
        fields ='__all__'

class AzResSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzRes
        fields ='__all__'

class AzUseSerializer(serializers.ModelSerializer):
    trans = TranAzSerializer(read_only = True, source='tranaz_set', many=True)

    class Meta:
        model = AzUse
        fields = "__all__"

class TranRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranRepo
        fields ='__all__'

class RepoResSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepoRes
        fields ='__all__'

class RepoUseSerializer(serializers.ModelSerializer):
    trans = TranRepoSerializer(read_only = True, source='tranrepo_set', many=True)

    class Meta:
        model = RepoUse
        fields = "__all__"
