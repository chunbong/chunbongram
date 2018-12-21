# rest_framework은 pipenv install djangorestframework로 설치한 앱
from rest_framework import serializers
from . import models

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    image = ImageSerializer()

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    # 2. 특정 필드는 키 값이 아니라 serizalizer라고 알려줌
    # 3. 따라서, 키 값 대신 serialize 된 오브젝트가 출력됨
    image = ImageSerializer()

    class Meta:
        model = models.Like
        # 1. 모든 필드를 가져오는데
        fields = '__all__'