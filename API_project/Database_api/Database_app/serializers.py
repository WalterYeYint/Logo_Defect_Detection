from . models import Detections
from rest_framework import serializers


class DetectionsSerializer(serializers.ModelSerializer):

    # photo = Base64ImageField(
    #     max_length=None, use_url=True,
    # )

    class Meta:
        model = Detections
        # fields = ("time","camera_number","behaviour","name","photo","video")
        fields = '__all__'
