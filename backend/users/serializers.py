# from rest_framework import serializers
# from django.contrib.auth.models import User



# def clean_email(value):
# 	check_email = User.objects.filter(email = value).first()
# 	if check_email : 
# 		raise serializers.ValidationError('A user with that email already exists.')


# class UserRegisterSerializer(serializers.Serializer):
# 	password2 = serializers.CharField(write_only=True, required=True)
# 	password = serializers.CharField()
# 	email = serializers.EmailField()
# 	username = serializers.CharField()
# 	# class Meta:
# 	# 	model = User
# 	# 	fields = ('username', 'email', 'password', 'password2')
# 	# 	extra_kwargs = {
# 	# 		'password': {'write_only':True},
# 	# 		'email': {'validators': (clean_email,)}
# 	# 	}
		

# 	def create(self, validated_data):
# 		del validated_data['password2']
# 		return User.objects.create_user(**validated_data)

# 	def validate_username(self, value):
# 		check_username = User.objects.filter(username = value).first()
# 		if check_username: 
# 			raise serializers.ValidationError('A user with that username already exists.')
# 		return value

# 	def validate(self, data):
# 		if data['password'] != data['password2']:
# 			raise serializers.ValidationError('passwords must match')
# 		return data




from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserInformationSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = User
        fields = '__all__'