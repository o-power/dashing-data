from django.contrib import admin
from .models import UserChart, BarChart

class BarChartAdminInline(admin.TabularInline):
    model = BarChart

class UserChartAdmin(admin.ModelAdmin):
    inlines = (BarChartAdminInline, )

admin.site.register(UserChart, UserChartAdmin)