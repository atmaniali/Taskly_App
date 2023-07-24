from django.contrib.auth.models import User
from rest_framework import serializers

from .logger import logger
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.HyperlinkedRelatedField(
        read_only=True, many=False, view_name='user-detail')

    class Meta:
        model = Profile
        fields = ['url', 'id', 'user', 'image']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)
    old_password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(read_only=True)

    logger.info("USER UserSerializer IS RUN OK")

    def validate(self, data):
        password = data.get('password', None),
        old_password = data.get('password', None),
        request_method = self.context['request'].method

        if request_method == "POST":
            if password == None:
                raise serializers.ValidationError(
                    {'info': 'Please Provide a Password'})
        elif request_method == "PATCH" or "PUT":
            if password != None and old_password == None:
                raise serializers.ValidationError(
                    {"info": "Please Provide The Old Password"})

    def create(self, validated_data):
        # logger.info("USERs UserSerializer created function IS RUNUNG OK")
        password = validated_data.pop('password')
        print(f"PASWORD ***** {password}")
        user = User.objects.create(**validated_data)
        # logger.info("THIS IS UserSerializer CLASS DEBUG : password", password)
        user.set_password(password)
        print(f"PASWORD HASH ***** {user}")
        # logger.info("THIS IS UserSerializer CLASS DEBUG : user.set_password",
        #             user.set_password(password))
        user.save()
        return user

    def update(self, instance, validated_data):

        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                old_password = validated_data.pop('old_password')

                if user.check_password(old_password):
                    user.set_password(password)

                else:
                    raise Exception('Invalid Old Password')

                user.save()

        except Exception as err:
            raise serializers.ValidationError({"info": err})

        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email',
                  'first_name', 'last_name', 'password', 'old_password', 'profile']
        # t
