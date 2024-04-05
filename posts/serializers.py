from rest_framework import serializers
from .models import Post,User

class UserSerializer(serializers.ModelSerializer):
     class Meta:
       model = User
       fields = ['id','username','email']
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = serializers.StringRelatedField()
    class Meta:
       model = Post
       fields = '__all__'
      
