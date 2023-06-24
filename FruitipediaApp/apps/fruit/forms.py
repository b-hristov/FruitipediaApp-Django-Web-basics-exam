from django import forms
from FruitipediaApp.apps.fruit.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),
            'nutrition': forms.TextInput(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = Fruit
        fields = '__all__'
        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.disabled = True
