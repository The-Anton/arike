"""arike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from dashboard.views import dashboard_view
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from facility.views import (GenericFacilityCreateView,
                            GenericFacilityDeleteView,
                            GenericFacilityDetailView,
                            GenericFacilityUpdateView)
from patients.views import (GenericDiseaseHistoryCreateView,
                            GenericDiseaseHistoryDeleteView,
                            GenericDiseaseHistoryDetailView,
                            GenericDiseaseHistoryUpdateView,
                            GenericFamilyCreateView, GenericFamilyDeleteView,
                            GenericFamilyDetailView, GenericFamilyUpdateView,
                            GenericPatientCreateView, GenericPatientDeleteView,
                            GenericPatientDetailView, GenericPatientUpdateView,
                            GenericTreatmentCreateView,
                            GenericTreatmentDeleteView,
                            GenericTreatmentDetailView,
                            GenericTreatmentUpdateView)
from users.views import GenericUserCreateView, GenericUserDeleteView, GenericUserDetailView, GenericUserListView, GenericUserUpdateView, login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", dashboard_view),
    path("login/", login_view),

    path("users/", GenericUserListView.as_view()),
    path("user-create/", GenericUserCreateView.as_view()),
    path("user-update/<pk>", GenericUserUpdateView.as_view()),
    path("user-detail/<pk>", GenericUserDetailView.as_view()),
    path("user-delete/<pk>", GenericUserDeleteView.as_view()),

    path("facility-create/", GenericFacilityCreateView.as_view()),
    path("facility-update/<pk>", GenericFacilityUpdateView.as_view()),
    path("facility-detail/<pk>", GenericFacilityDetailView.as_view()),
    path("facility-delete/<pk>", GenericFacilityDeleteView.as_view()),

    path("patient-create/", GenericPatientCreateView.as_view()),
    path("patient-update/<pk>", GenericPatientUpdateView.as_view()),
    path("patient-detail/<pk>", GenericPatientDetailView.as_view()),
    path("patient-delete/<pk>", GenericPatientDeleteView.as_view()),

    path("disease-history-create/", GenericDiseaseHistoryCreateView.as_view()),
    path("disease-history-update/<pk>", GenericDiseaseHistoryUpdateView.as_view()),
    path("disease-history-detail/<pk>", GenericDiseaseHistoryDetailView.as_view()),
    path("disease-history-delete/<pk>", GenericDiseaseHistoryDeleteView.as_view()),

    path("treatment-create/", GenericTreatmentCreateView.as_view()),
    path("treatment-update/<pk>", GenericTreatmentUpdateView.as_view()),
    path("treatment-detail/<pk>", GenericTreatmentDetailView.as_view()),
    path("treatment-delete/<pk>", GenericTreatmentDeleteView.as_view()),

    path("family-create/", GenericFamilyCreateView.as_view()),
    path("family-update/<pk>", GenericFamilyUpdateView.as_view()),
    path("family-detail/<pk>", GenericFamilyDetailView.as_view()),
    path("family-delete/<pk>", GenericFamilyDeleteView.as_view()),

]
