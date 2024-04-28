from django.urls import path
from . import views
#from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'siteapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'main'),
    path('search/', views.PostSearchList.as_view(), name='search'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('category/<int:pk>/', views.PostCategoryList.as_view(), name='category'),
    path('archive/<int:year>/', views.PostYearList.as_view(), name='year'),
    path('archive/<int:year>/<int:month>/', views.PostMonthList.as_view(), name='month'),
    path('google9689b400addd4ddc.html/', views.google_search_console, name='google_search_console'),
]
