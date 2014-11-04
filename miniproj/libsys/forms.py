from django.forms import ModelForm
from libsys.models import Member

class SignupForm(ModelForm):
	class Meta:
		model = Member
