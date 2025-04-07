from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Post, CareerForm, ContactInquiry, AftermarketForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    
    class Meta:
        model = Post
        fields = [
            'id', 'meta_title', 'meta_description', 'title', 'slug', 
            'date_added', 'author', 'featured_image', 'category', 'category_id',
            'intro', 'body'
        ]
        read_only_fields = ['slug']

class CareerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerForm
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'application_type', 'role_applied_for', 'current_location',
            'resume', 'message', 'agreed_to_terms'
        ]

class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ['id', 'name', 'email', 'phone_number', 'message']

class AftermarketFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AftermarketForm
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number',
            'company_name', 'country', 'message'
        ] 

