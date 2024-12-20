class OrganizationMixin:
    def get_organization(self):
        organization = getattr(self.request.site, 'organization', None)
        if not organization:
            self.permission_denied(self.request, message="Organization not found.")
        return organization
