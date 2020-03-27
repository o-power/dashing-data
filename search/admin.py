from django.contrib import admin
from .models import UserChart, BarChart, LineChart

class BarChartAdminInline(admin.TabularInline):
    model = BarChart

class LineChartAdminInline(admin.TabularInline):
    model = LineChart

class UserChartAdmin(admin.ModelAdmin):
    inlines = (BarChartAdminInline, LineChartAdminInline, )

admin.site.register(UserChart, UserChartAdmin)