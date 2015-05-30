from django.core.urlresolvers import reverse_lazy

from grappelli_extensions.nodes import CLNode


class Navbar(object):
    nodes = (
        # ('Auth', {'nodes': (
        #     ('Users', {
        #         'url': reverse_lazy('admin:auth_user_changelist'),
        #         'perm': 'auth.change_user',
        #     }),
        #     ('Groups', {
        #         'url': reverse_lazy('admin:auth_group_changelist'),
        #         'perm': 'auth.change_group',
        #     }),
        # )}),

        # ('Nodes', {'nodes': (
        #     CLNode('auth', 'user'),
        #     #CLNode('sites', 'site'),
        # )}),
        # CLNode('auth', 'user', u"Site users"),
        # #CLNode('filebrowser', 'browse', u"Filebrowser"),

        ('Filebrowser',{'url': '/admin/filebrowser/browse/'}),
        ('Templates',{'url': '/admin/templates/'}),
        ('Web Pages',{'url': '/'}),
    )