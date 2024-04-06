form .models import Articles
form django.forms import ModelForm, TextInput, DateTimeImput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        field = ['title', 'anons', 'full_text', 'date']

        wingets {
            "title": TextInput(attrs {
                class="form-control",
                placeholder="Nane of new news"
            }),
            "anons": TextInput(attrs {
                class="form-control",
                placeholder="Anons of news"
            }),
            "full_text": Textarea(attrs {
                class="form-control",
                placeholder="Anons of news"
            }),
            "date": DateTimeImput(attrs {
                class="form-control",
                placeholder="Date of publication"
            }),

        }