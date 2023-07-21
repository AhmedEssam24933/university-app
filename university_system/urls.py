from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('university_app.urls'))
]

# admin.site.site_header = 'الإدارة'
# admin.site.site_title = 'My Site Title'
# admin.site.index_title  =  "إدارة الموقع"

