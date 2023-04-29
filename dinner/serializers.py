from rest_framework import serializers
from dinner.models import User, Bookpost

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nickname', 'phonenum']

class BookpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookpost
        fields = ['whos', 'title', 'contents', 'image']

    def get_bookInfo(self, obj):
        return obj.values('title', 'contents')