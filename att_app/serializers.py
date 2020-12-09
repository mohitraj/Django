from rest_framework import serializers
from .models import Masterdata5


'''
class AttSerializer(serializers.Serializer):
	roll_number = serializers.IntegerField()
	name = serializers.CharField(max_length=100)
	email = serializers.EmailField()
	class_name = serializers.CharField(max_length=100)

'''
def email_valid(value):
	if not value.endswith("gmail.com"):
		raise serializers.ValidationError('Not valid Email please use Gmail')


class AttSerializer(serializers.ModelSerializer):
	email = serializers.CharField(validators=[email_valid])
	class Meta:
		model = Masterdata5
		fields = ['roll_number', 'name', 'class_name', 'email']

	'''
	def  validate_roll_number(self, value):  # Field Level validation
		if value >= 100 :
			raise serializers.ValidationError('Not valid Roll number')
		return value

	def validate(self, data):  # object level validation
		roll = data.get('roll_number')
		cl = data.get('class_name')
		if roll <= 50 or cl.lower() != 'csed':
			raise serializers.ValidationError('Either rollnumber or class not valid')
		return data


    '''
