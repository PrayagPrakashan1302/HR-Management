from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_page, name="login_page_app"),
    path('employee-list/', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('add-employee/', views.employee_add, name='employee_add'),
    path('onboard-employee/<int:pk>/', views.onboard_employee, name='onboard_employee'),
    path("onboard_check",views.onboard_check, name="onboard_check"),
]
