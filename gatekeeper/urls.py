
#from registration.backends.default.views import RegistrationView
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import object_tools

from django.contrib import admin
from adminplus.sites import AdminSitePlus

admin.site.index_template = 'admin/gatekeeper/change_form.html'
admin.site = AdminSitePlus()
admin.autodiscover()


urlpatterns = [
    # Examples:
#    url(r'^$', 'gatekeeperapp.views.home', name='home'),
    url(r'^', include('gatekeeperapp.urls')),
    #url(r'^nh5/', include('nh5.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    #url(r'^jet/', include('jet.urls', 'jet')),
    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_export/', include("admin_export.urls", namespace="admin_export")),
    url(r'^object-tools/', include(object_tools.tools.urls)) 
    #url(r'^accounts2/', include('users.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),
#    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
#   url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    #url(r'^accounts/register/$', 'accounts.views.registration_view', name='auth_register'),
    ##url(r'^accounts/password/reset/$', 'accounts.views.password_reset', name='password_reset'),
    #url(r'^accounts/address/add/$', 'accounts.views.add_user_address', name='add_user_address'),
    #url(r'^accounts/activate/(?P<activation_key>\w+)/$', 'accounts.views.activation_view', name='activation_view'),
    #url(r'^accounts/password/reset/$', include('registration.backends.default.urls')),
    

]



if settings.DEBUG:
        import debug_toolbar
        urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

admin.site.site_header = 'Gatekeeper'
