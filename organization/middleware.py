from django.contrib.sites.models import Site
from django.utils.deprecation import MiddlewareMixin
from organization.models import Organization
from django.http import HttpResponseForbidden



class SiteMiddleware(MiddlewareMixin):
    def process_request(self, request):
        domain = request.get_host().split(':')[0]
        print(domain)
        try:
            current_site = Site.objects.get(domain=domain)
            request.site = current_site
        except Site.DoesNotExist:
            request.site = None
