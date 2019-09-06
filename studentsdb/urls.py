from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'studentsdb.views.students_list', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
