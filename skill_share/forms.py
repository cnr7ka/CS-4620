from django import forms
from skill_share.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class createAccountForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = [
			'first_name',
			'last_name',
            'email',
            'date_of_birth',
            'gender',
			'skills',
		]
	def __init__ (self, *args,**kwargs):
		super(createAccountForm,self).__init__(*args,**kwargs)


		self.fields["skills"].widget=forms.widgets.CheckboxSelectMultiple()
		self.fields["skills"].queryset= Skill.objects.all()

class createSkillForm(forms.ModelForm):
	class Meta:
		model = Skill
		fields = [
			'name',
		]
	def __init__ (self, *args,**kwargs):
		super(createSkillForm,self).__init__(*args,**kwargs)
