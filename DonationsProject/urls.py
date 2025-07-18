"""
URL configuration for DonationsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from DonationsApp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
    
#     path('', include('DonationsApp.urls')),
#     path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='logout'),
# ]
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Add this
from django.conf import settings                      # ✅ required for MEDIA settings
from django.conf.urls.static import static            # ✅ required for MEDIA settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DonationsApp.urls')),  # Your app URLs
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # ✅ fixed
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # ✅ fixed
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

# Add this to serve media during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
