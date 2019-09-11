# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal_list(request):
    journal = (
        {'id': 1,
         'first_name': u'Віталій',
	 'last_name': u'Подоба'
         },
        {'id': 2,
         'first_name': u'Корост',
	 'last_name': u'Андрій'
         },
	{'id': 3,
         'first_name': u'Тарас',
         'last_name': u'Притула'
         },
    )
    return render(request, 'students/journal_list.html',
        {'journal': journal})

def journal_add(request):
    return HttpResponse('<h1>journal Add Form</h1>')

def journal_edit(request, sid):
    return HttpResponse('<h1>Edit journal %s</h1>' % sid)

def journal_delete(request, sid):
    return HttpResponse('<h1>Delete journal %s</h1>' % sid)
