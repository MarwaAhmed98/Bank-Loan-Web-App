from django.db import models
class approvals(models.Model):
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'))
    
    MARRIED_CHOICES = (	('Yes', 'Yes'),('No', 'No'))
    
    
    GRADUATED_CHOICES = (('Graduate', 'Graduated'),('Not_Graduate', 'Not_Graduate'))
    
    
    SELFEMPLOYED_CHOICES = (('Yes', 'Yes'),('No', 'No')) 
    
    CLIENT_CHOICES = (('Yes', 'Yes'),('No', 'No')) 
    
    
    PROPERTY_CHOICES = (('Rural', 'Rural'), ('Semiurban', 'Semiurban'),('Urban', 'Urban'))
		
	
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    dependents=models.IntegerField(default=0)
    applicantIncome=models.IntegerField(default=150)
    coapplicantIncome=models.IntegerField(default=0)
    loanAmt=models.IntegerField(default=0)
    loanTerm=models.IntegerField()
    creditHistory=models.IntegerField()
    gender=models.CharField(max_length=15, choices=GENDER_CHOICES)
    married=models.CharField(max_length=15, choices=MARRIED_CHOICES)
    graduateEducation=models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    selfEmployed=models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
    propertyArea=models.CharField(max_length=15, choices=PROPERTY_CHOICES)

def __str__(self):
     return '{}, {}'.format(self.lastname, self.firstname)