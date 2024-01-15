from django.urls import path
from . import views
urlpatterns = [
    path('',views.show_data,name='home'),
    # path('update/',views.update_data,name='update'),
    path('save/',views.Save_form,name='save'), 
    path('delete/',views.delete_data,name='delete'),
    path('edit/',views.edit_data, name='edit'),   
  
]
