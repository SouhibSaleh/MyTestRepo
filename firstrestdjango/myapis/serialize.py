from rest_framework import serializers
from firstapp.models import myitem


class mySerializers(serializers.ModelSerializer):
    class Meta:
        model = myitem
        fields = '__all__'
