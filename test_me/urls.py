from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', users_views.profile, name="profile"),
    path('classrooms/', include('classrooms.urls')),
    path('register/', users_views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html',
         redirect_authenticated_user=True), name='login'),
    path('logout/',
         LogoutView.as_view(), name='logout'),
    path('', users_views.dashboard, name="dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
