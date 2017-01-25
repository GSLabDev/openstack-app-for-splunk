from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('openstack_app:home.html')
@login_required
def home(request):
    return {
        "message": "Hello World from openstack_app!",
        "app_name": "openstack_app"
    }