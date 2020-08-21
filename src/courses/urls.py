from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    #my_fbv,
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    #path('', CourseView.as_view(template_name='contact.html'), name='course-list'),
    #path('', my_fbv, name='courses-list'),
    
    path('create/',CourseCreateView.as_view(), name='courses-create'),  
    path('<int:id>/', CourseView.as_view(), name='courses-detail'), #Generic detail view must be called with either an object pk or a slug.
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),

]