
from . import views

from rest_framework import routers
from django.urls import path, include

router=routers.DefaultRouter()
router.register('MyAPI', views.ApprovalsView)
urlpatterns = [
    # path('form/', views.myform, name='myform'), 
    # path('status/', views.approvereject), 
    # path('api/', include(router.urls)),
    path('', views.cxcontact, name='cxform'),
  
  
    
  
]
