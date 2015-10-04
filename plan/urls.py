from django.conf.urls import url


urlpatterns = [
    url(r'^$','plan.views.total', name='total'),
    url(r'^myplan/$', 'plan.views.index', name='index'),
    url(r'^newplan/$', 'plan.views.create_plan', name='newplan'),
    url(r'^myplan/(?P<pk>\d+)/$', 'plan.views.detail', name='detail'),
    url(r'^myplan/(?P<pk>\d+)/edit/$', 'plan.views.edit_plan', name='edit_plan'),

    url(r'^myplan/(?P<pk>\d+)/transit/$', 'plan.views.index_transit', name='index_transit'),
    url(r'^myplan/(?P<pk>\d+)/transitadd/$', 'plan.views.add_transit', name='add_transit'),

    url(r'^myplan/(?P<pk>\d+)/comments/new$','plan.views.new_comment', name='new_comment'),
]
