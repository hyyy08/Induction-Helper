from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DatabaseUser, Category, Equipment, Induction, Catalog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib import colors
from django.http import HttpResponse
import csv
import xlsxwriter

from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Export dataUsers to csv from admin
def export_to_csv(modelsadmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    
    writer = csv.writer(response)
    
    headers = [field.verbose_name for field in modelsadmin.model._meta.fields]
    writer.writerow(headers)
    
    for obj in queryset:
        data_row = [getattr(obj, field.name) for field in modelsadmin.model._meta.fields]
        writer.writerow(data_row)
    
    return response

@admin.register(DatabaseUser)
class DatabaseUserAdmin(admin.ModelAdmin):
    list_display = ('userID', 'email', 'firstName', 'lastName', 'userDate')
    search_fields = ('email', 'firstName', 'lastName')
    list_filter = ('userID', 'userDate')
    actions = [export_to_csv] # export data

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'categoryDescription')
    search_fields = ('category', 'categoryDescription')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipmentName', 'equipmentDescription')
    search_fields = ('equipmentName', 'equipmentDescription')

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('category', 'equipmentName')

@admin.register(Induction)
class InductionAdmin(admin.ModelAdmin):
    list_display = ('userID', 'dateAdded', 'dateCompleted', 'completionStatus')
    
# Register the CustomUserAdmin with the admin site
