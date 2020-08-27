from django import forms
from django.core import validators
import re
from django.core.exceptions import ValidationError


def validate_name(name):
    m = re.match('[a-zA-Z]+', name)
    if m.group()!=name:
        raise ValidationError("Name should contains only alphabet")
    return name

day_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')]
month_choices = [('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'), ('12', 'Dec')]
year_choices = [('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012')]
class BuiltinForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True, label="First Name", validators=[validate_name])
    last_name = forms.CharField(max_length=20, required=False, label="Last Name", validators=[validate_name])
    pwd = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label="Password")
    pwd1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput, label="Confirm Password")
    birth_day = forms.ChoiceField(choices=day_choices, required=True, label="Birth Day")
    birth_month = forms.ChoiceField(choices=month_choices, required=True, label="Birth Month")
    birth_year = forms.ChoiceField(choices=year_choices, required=True, label="Birth Year")
    gender = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female")], required=True, widget=forms.RadioSelect)
    languages = forms.MultipleChoiceField(choices=[("Python", "Python"), ("Java", "Java"), ("C", "C")], required=True, widget=forms.CheckboxSelectMultiple)
    
    def clean(self,*args,**kwars):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("pwd")
        pwd1 = cleaned_data.get("pwd1")
        if pwd!=pwd1:
            # raise ValidationError("Password must be same")
            self.add_error("pwd", "Passwords must be same")
        return cleaned_data

