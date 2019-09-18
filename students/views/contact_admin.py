from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from studentsdb.settings import ADMIN_EMAIL
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control.label'
        self.helper.field_class = 'col-sm-10'

        self.helper.add_input(Submit('send_button', u'Send'))

    from_email = forms.EmailField(label=u"Your email address")
    subject = forms.CharField(label=u"List title", max_length=128)
    message = forms.CharField(label=u"Text message", max_length=2560, widget=forms.Textarea)


def contact_admin(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject,message,from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'An unexpected error occurred while submitting. Try to use form later.'
            else:
                message = u'Email was send successful!'
            return HttpResponseRedirect(u'%s?status_message=%s' % (reverse('contact_admin'), message))
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {'form': form})

