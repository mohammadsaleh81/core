from django.contrib import admin
from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass