from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data.get("username")
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError("Please make sure you have registered !")
		return username

	def clean_password(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError("Make sure your Password is correct!")
		elif user is None:
			pass
		else:
			return password




class RegistrationForm(forms.ModelForm):
	username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label='Password', \
					widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label='Password Confirmation', \
					widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'email','password1','password2']

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2

	def clean_email(self):
		email = self.cleaned_data.get("email")
		user_count = User.objects.filter(email=email).count()
		if user_count > 0:
			raise forms.ValidationError("This email has already been registered. Please check and try again or reset your password.")
		return email


	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1']) 
		if commit:
			user.save()
		return user
