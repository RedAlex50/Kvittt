from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput
from .models import *
from django.utils.timezone import localdate

today = localdate()

class NewForm(ModelForm):
    class Meta:
        model = New
        fields = ['title', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
             'text': Textarea(attrs={
                'class': 'form-control text-area',
                'placeholder': 'Текст новости'
            }),
            'img_1': FileInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Изображение 1',
                'id': 'img_1',
                'style': 'display: block;',
            }),
            'img_2': FileInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Изображение 2',
                'id': 'img_2',
                'style': 'display: none;',
            }),
            'img_3': FileInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Изображение 3',
                'id': 'img_3',
                'style': 'display: none;',
            }),
            'img_4': FileInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Изображение 4',
                'id': 'img_4',
                'style': 'display: none;',
            }),
            'img_5': FileInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Изображение 5',
                'id': 'img_5',
                'style': 'display: none;',
            }),
        }
    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)
        # self.fields['img_1'].required = False
        # self.fields['img_2'].required = False
        # self.fields['img_3'].required = False
        # self.fields['img_4'].required = False
        # self.fields['img_5'].required = False