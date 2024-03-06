from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'house_number', 'city', 'state', 'zipcode', 'street', 'question', 'add_member')