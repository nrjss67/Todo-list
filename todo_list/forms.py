from django import forms

from todo_list.models import Tag, Task


class TaskCreateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
    )
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags_exist = Tag.objects.exists()
    
    
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
                   "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
                   "tags": forms.CheckboxSelectMultiple,
                }
