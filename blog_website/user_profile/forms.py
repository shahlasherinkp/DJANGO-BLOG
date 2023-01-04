from django import forms

from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=250, required=True)
    password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "email", "password",)

        def clean_username(self):
            username = self.cleaned_data.get()
            model = self.Meta.model
            user = model.objects.filter(username_iexact=username)
            
            if user.exists():
                raise forms.ValidationError("a user with that name already exists")
            
            return self.cleaned_date.get('username')

        
        def clean_email(self):
            email = self.cleaned_data.get()
            model = self.Meta.model
            user = model.objects.filter(email_iexact=email)
            
            if user.exists():
                raise forms.ValidationError("a user with that email already exists")
            
            return self.cleaned_date.get('email')

        def clean_password(self):
            password = self.cleaned_date.get('password')
            confim_password = self.data.get('confirm_password')

            if password != confim_password:
                raise forms.ValidationError("Passwords do not match")

            return self.cleaned_date.get('password')

class UserProfileUpdateForm(forms.ModelForm):
    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email",)

        def clean_username(self):
            username = self.cleaned_data.get()
            model = self.Meta.model
            user = model.objects.filter(username_iexact=username).exclude(pk=self.instance.pk)
            
            if user.exists():
                raise forms.ValidationError("a user with that name already exists")
            
            return self.cleaned_date.get('username')

        
        def clean_email(self):
            email = self.cleaned_data.get()
            model = self.Meta.model
            user = model.objects.filter(email_iexact=email).exclude(pk=self.instance.pk)
            
            if user.exists():
                raise forms.ValidationError("a user with that email already exists")
            
            return self.cleaned_date.get('email')
        
        def change_password(self):
            if 'new_password' in self.data and 'confirm_password' in self.data:
                new_password = self.data['new_password']
                confirm_password = self.data['confirm_password']
                if new_password != '' and confirm_password !='':
                    if new_password != confirm_password:
                        raise forms.ValidationError("password do not match")
                    else:
                        self.instance.set_password(new_password)
                        self.instance.save()

        def clean(self):
            self.change_password()

class ProfilePictureUpdateForm(forms.Form):
    profile_image = forms.ImageField(required=True)
     