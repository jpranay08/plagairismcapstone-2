from django import forms
from .models import Subject, Enroll, files

class CourseForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title','slug','photo')

    def save(self):
        s = Subject() # s = self.instance
        s.title = self.cleaned_data['title']
        s.slug = self.cleaned_data['slug']
        s.photo = self.cleaned_data['photo']
        s.save()
        return s

class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = '__all__'
   
    def save(self):
        a= Enroll()
        a.status=self.cleaned_data['status']
        a.student=self.cleaned_data['student']
        a.subject=self.cleaned_data['subject']
        a.save()
        return a

class FileForm(forms.ModelForm):
    class Meta:
        model = files
        fields = ('Name','File')

    def save(self):
        f = files() # s = self.instance
        f.Name = self.cleaned_data['Name']
        f.photo = self.cleaned_data['File']
        f.save()
        return f