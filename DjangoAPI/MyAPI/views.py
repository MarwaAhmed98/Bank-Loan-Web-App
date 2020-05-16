from django.shortcuts import render, redirect
#from . forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import ApprovalForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import approvals 
from .serializers import approvalsSerializer
import pickle
from sklearn.externals import joblib
from django.contrib import messages
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class ApprovalsView(viewsets.ModelViewSet):
    queryset = approvals.objects.all()
    serializer_class= approvalsSerializer

def ohevalue(df):
    ohe_col=joblib.load("MyAPI/allcol.pkl")
    cat_columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed= pd.get_dummies(df, columns=cat_columns)
    newdict={}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
            
    newdf = pd.DataFrame(newdict)
    return newdf
    

#@api_view(["POST"])
def approvereject(unit):
    try: 
        mdl=joblib.load("MyAPI/final_model.pkl")
        #unit=np.array(list(unit.values()))
        #unit=unit.reshape(1,-1)
        scalers=joblib.load("MyAPI/scaler_final.pkl")
        X=scalers.transform(unit)
        y_pred=mdl.predict(X)
        y_pred=(y_pred>0.50)
        newdf=pd.DataFrame(y_pred, columns=['Status'])
        newdf=newdf.replace({True: "Approved", False: "Rejected"})
        return (list(newdf ['Status'])[0])
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
    
    
def cxcontact(request):
    if request.method == 'POST':
        form=ApprovalForm(request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data['Firstname']
            Lastname=form.cleaned_data['Lastname']
            Dependents=form.cleaned_data['Dependents']
            ApplicantIncome=form.cleaned_data['ApplicantIncome']
            CoapplicantIncome=form.cleaned_data['CoapplicantIncome']
            LoanAmount=form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History=form.cleaned_data['Credit_History']
            Gender=form.cleaned_data['Gender']
            Married=form.cleaned_data['Married']
            Education=form.cleaned_data['Education'] 
            Self_Employed=form.cleaned_data['Self_Employed']
            Property_Area=form.cleaned_data['Property_Area']
            myDict=(request.POST).dict()
            df=pd.DataFrame(myDict, index=[0])
            answer=approvereject(ohevalue(df))
            
            if int(df['LoanAmount']) < 5000:
                message=messages.success(request, 'Your Application Status is : {}' .format(answer))
            else: 
                messages.success(request, 'Invalid: Your Loan Request Exceeds the 5,000 Limit')
            print(approvereject(ohevalue(df)))
            #print(ohevalue(df))
            
     
    form=ApprovalForm()
    
             
    return render(request, 'myform/form.html', {'form': form})
    
        