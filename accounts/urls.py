from django.conf.urls import patterns, url

urlpatterns = patterns('',


	 
    (r'^login/$',
     'django.contrib.auth.views.login',
     {'template_name': 'accounts/login.html'}),

    (r'^logout/$',
     'django.contrib.auth.views.logout',
     {'template_name': 'accounts/logged_out.html'}),

    (r'^password_change/$',
     'django.contrib.auth.views.password_change',
     {'template_name': 'accounts/password_change_form.html'}),

    (r'^password_change/done/$',
     'django.contrib.auth.views.password_change_done',
     {'template_name': 'accounts/password_change_done.html'}),

    (r'^password_reset/$',
     'django.contrib.auth.views.password_reset',
     {'template_name': 'accounts/password_reset_form.html',
      'email_template_name': 'accounts/password_reset_email.html'}),

    (r'^password_reset/done/$',
     'django.contrib.auth.views.password_reset_done',
     {'template_name': 'accounts/password_reset_done.html'}),

    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
     'django.contrib.auth.views.password_reset_confirm',
     {'template_name': 'accounts/password_reset_confirm.html'}),

    (r'^reset/done/$',
     'django.contrib.auth.views.password_reset_complete',
     {'template_name': 'accounts/password_reset_complete.html'}),

    (r'^signup/$',
     'accounts.views.signup',
     {'template_name': 'accounts/signup_form.html',
      'email_template_name': 'accounts/signup_email.html'}),

    (r'^signup/done/$',
     'accounts.views.signup_done',
     {'template_name': 'accounts/signup_done.html'}),

    (r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
     'accounts.views.signup_confirm'),

    (r'^signup/complete/$',
     'accounts.views.signup_complete',
     {'template_name': 'accounts/signup_complete.html'}),

)
