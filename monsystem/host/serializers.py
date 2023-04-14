from rest_framework import serializers

from .models import Members,all_users_data

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Members
        fields = ("name", "host","cpu_usage")

class all_memberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = all_users_data
        fields = ("program_name","name", "host","program_id","cores","cpu_usage","status","memory_usage")
