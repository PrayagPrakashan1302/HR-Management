"""
URL configuration for onboarding_project project.

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
from django.contrib import admin
from django.urls import path, include
from onboarding_app import views as on_bording_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app', include('onboarding_app.urls')),  # Redirect default URL to onboarding_app
    path("", on_bording_views.login_page, name="log_in_page"),
    path("logout", on_bording_views.logout_view, name="logout")
]