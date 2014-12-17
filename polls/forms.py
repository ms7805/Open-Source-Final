from django import forms
from polls.models import UserProfile, User, Question, Choice,photo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
   class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class PictureForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    text = forms.CharField(max_length=100, help_text="Enter a description of the picture",required=True)
    class Meta:
        model = photo
        fields = ('text','image')

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user',None)
         super(QuestionForm, self).__init__(*args, **kwargs)
    question_title = forms.CharField(max_length=100, help_text="Please enter the question Title.")
    question_text =  forms.CharField(max_length=500, widget=forms.Textarea, help_text="Please enter the question Text.")
    tag = forms.CharField(max_length=20,help_text="Please enter a tag",required=False)
    class Meta:
        model = Question
        fields = ('question_title','question_text','user','tag','pic')

class ChoiceForm(forms.ModelForm):
    choice_title = forms.CharField(max_length=100, help_text="Please enter the Answer Title.")
    choice_text =  forms.CharField(max_length=500, widget=forms.Textarea, help_text="Please enter the Answer Text.")
    class Meta:
        model = Choice
        fields = ('question','choice_title','choice_text','creator','pic')