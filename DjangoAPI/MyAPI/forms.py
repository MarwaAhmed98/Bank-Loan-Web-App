from django import forms


class ApprovalForm(forms.Form):
    Firstname = forms.CharField( max_length=15, widget=forms.TextInput(attrs = {'placeholder': 'Enter your first name'}))
    Lastname=forms.CharField( max_length=15, widget=forms.TextInput(attrs = {'placeholder': 'Enter your last name'}))
    Dependents=forms.IntegerField(widget=forms.NumberInput(attrs = {'placeholder': 'Enter number of dependents'}))
    ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs = {'placeholder': 'Enter your income'}))
    CoapplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs = {'placeholder': 'Enter your co-partner income'}))
    LoanAmount= forms.IntegerField(widget=forms.NumberInput(attrs = {'placeholder': 'Enter the loan amount you\'re asking for '}))
    Loan_Amount_Term = forms.IntegerField(widget=forms.NumberInput(attrs = {'placeholder': 'Enter loan term'}))
    Credit_History=forms.ChoiceField(choices=[('0', 0), ('1', 1)])
    Gender=forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    Married=forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Education=forms.ChoiceField(choices=[('Graduated', 'Graduated'), ('Not Graduated', 'Not Graduated')])
    Self_Employed=forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Property_Area=forms.ChoiceField(choices=[('Rural', 'Rural'), ('Urban', 'Urban'),  ('Semiurban', 'Semiurban')])
    
    
    
