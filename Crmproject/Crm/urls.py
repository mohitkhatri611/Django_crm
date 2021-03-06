from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login, name="login"),
    path("reports_genrate/", views.reports_genrate, name="reports_genrate"),
    path("Admin_panel/", views.Admin_panel, name="Admin_panel"),
    path("Admin_panel/search_enq_month/",
         views.search_enq_month, name="search_enq_month"),
    path("enq_create/", views.enq_create, name="enq_create"),
    path("validate_Number", views.validate_Number, name="validate_Number"),
    path("Enquiry_Update/<str:pk_id>/",
         views.Enquiry_Update, name="Enquiry_Update"),
    path("Enquiry_search/", views.Enquiry_search, name="Enquiry_search"),
    path("Enquiry_Delete/<str:pk_id>/",
         views.Enquiry_Delete, name="Enquiry_Delete"),
    path("logout/", views.logout, name="logout"),
    path("history/<str:pk_id>/", views.history_view, name="history"),
    path("user_delete/<str:pk_id>/", views.user_delete, name="user_delete"),
    path("user_update/<str:pk_id>/", views.user_update, name="user_update"),
    path("enq_create/", views.enq_create, name="enq_create"),
    path("salesperson/salesenquiry_reports/",
         views.salesenquiry_reports, name="salesenquiry_reports"),
    path("salesperson/", views.saleperson_page, name="saleperson"),
    path("salesperson/salespersonsearch_enq_month/",
         views.salespersonsearch_enq_month, name="salespersonsearch_enq_month"),
    path('csv_Files_import/', views.csv_Files_import, name="csv_Files_import"),
    path("salesperson_enq_create/", views.salesperson_enq_create,
         name="salesperson_enq_create"),
    path("salesperson_Enquiry_Delete/<str:pk_id>/",
         views.salesperson_Enquiry_Delete, name="salesperson_Enquiry_Delete"),
    path("salesperson_Enquiry_Update/<str:pk_id>/",
         views.salesperson_Enquiry_Update, name="salesperson_Enquiry_Update"),
    path("csv_Files_export", views.csv_Files_export, name="csv_Files_export"),


]
