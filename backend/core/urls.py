"""
URL configuration for induction_helper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import ( TokenObtainPairView,
                                            TokenRefreshView)
from core.views import (databaseUser_views,
                        equipment_views,
                        category_views,
                        induction_views,
                        userlogin_views,
                        catalog_views,
                        importstudentCSV_views,
                        exportFiles_views,
                        search_views,
                        instructor_view,
                        ocr_views,
                        get_serverIP,)                   

urlpatterns = [
    path('get_serverIP/', get_serverIP.get_serverIP, name='get_serverIP'),
    path('ocr/', ocr_views.OCRView.as_view(), name='ocr_image'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('databaseUser/', include([
        path('', databaseUser_views.UserListView.as_view(), name='user-list'),
        path('create/', databaseUser_views.UserCreateView.as_view(), name='create-user'),
        path('delete/<int:userID>/', databaseUser_views.UserDeleteView.as_view(), name='delete-user'),
        path('<int:userID>/', databaseUser_views.UserRetrieveUpdateDestroy.as_view(), name='update-user'),
    ])),
    
    path('Equipment/', include([
        path('', equipment_views.EquipmentListView.as_view(), name='equipment-list'),
        path('create', equipment_views.EquipmentCreateView.as_view(), name='create-equipment'),
        path('<str:equipmentName>', equipment_views.EquipmentRetrieveUpdateDestroy.as_view(), name='update-equipment'),
        path('delete/<str:equipmentName>', equipment_views.EquipmentDeleteView.as_view(), name='delete-equipment'),
    ])),
    path('Category/', include([
        path('', category_views.CategoryListView.as_view(), name='category-list'),
        path('create', category_views.CategoryCreateView.as_view(), name='create-category'),
        path('delete/<str:category>', category_views.CategoryDeleteView.as_view(), name='delete-category'),
        path('<str:category>', category_views.CategoryRetrieveUpdateDestroy.as_view(), name='update-category'),
    ])),
    path('Induction/', include([
        path('', induction_views.InductionListView.as_view(), name='induction-list'),
        path('create', induction_views.InductionCreateView.as_view(), name='create-induction'),
        path('<str:userID>/<str:category>/<str:equipmentName>', induction_views.InductionRetrieveUpdateDestroyView.as_view(), name='update-induction'),
        path('delete/<str:userID>/<str:category>/<str:equipmentName>', induction_views.InductionDeleteView.as_view(), name='delete-induction'),
    ])),
    path('Catalog/', include([
        path('', catalog_views.CatalogListView.as_view(), name='catalog-list'),
        path('create', catalog_views.CatalogCreateView.as_view(), name='create-catalog'),
        path('<str:category>/<str:equipmentName>/', catalog_views.CatalogRetrieveUpdateDestroy.as_view(), name='update-catalog'),
        path('delete/<str:category>/<str:equipmentName>', catalog_views.CatalogDeleteView.as_view(), name='delete-catalog'),
    ])),
    path('login/', include([
        path('', userlogin_views.CustomAuthToken.as_view(), name='login')
    ])),
    path('upload/', include([
        path('', importstudentCSV_views.CSVUploadViews.as_view(), name='upload'),
        path('users', importstudentCSV_views.CSVUploadViews.as_view(), name='user-upload')
    ])),
    path('search/', include([
        path('equipments', search_views.EquipmentSearchView.as_view(), name='equipment-search'),
        path('users/', search_views.UserSearchView.as_view(), name='user-search')
    ])),
    path('create-instructor/', instructor_view.CreateInstructorUserView.as_view(), name='create-instructor'),
    
    
    path('export_user_pdf/', exportFiles_views.export_user_pdf.as_view(), name ='export_user_pdf'),
    path('export_user_csv/', exportFiles_views.export_user_csv.as_view(), name ='export_user_csv'),
    path('export_induction_to_pdf/<int:user_id>/', exportFiles_views.export_induction_to_pdf_byID.as_view(), name='export_induction_to_pdf'),
    path('export_induction_to_pdf/', exportFiles_views.export_induction_to_pdf.as_view(), name='export_induction_to_pdf'),
    path('export_induction_to_csv/', exportFiles_views.export_induction_to_csv.as_view(), name='export_induction_to_csv'),
]
