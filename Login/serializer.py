# --------------AGRAGANDO LIBERIAS FRAMEWORK --------------
from rest_framework import routers, serializers, viewsets

from Login.models import Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('__all__')