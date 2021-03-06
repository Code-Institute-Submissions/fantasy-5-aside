from django.forms import FileField, CharField, ModelForm
from teams.models import Team
from django.core.exceptions import ValidationError



class CreateTeamForm(ModelForm):

    class Meta:
        model = Team
        fields = ['name', 'defender', 'midfielder1', 'midfielder2', 'striker1', 'striker2']

    def save(self, commit=True):
        instance = super(CreateTeamForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance

class TeamUpdate(ModelForm):

    class Meta:
        model = Team
        fields = ['defender', 'midfielder1', 'midfielder2', 'striker1', 'striker2']

    def save(self, commit=True):
            instance = super(TeamUpdate, self).save(commit=False)

            if commit:
                instance.save()

            return instance






