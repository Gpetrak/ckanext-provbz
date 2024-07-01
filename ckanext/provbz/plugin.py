import logging

from ckan.common import CKANConfig
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.provbz.helpers as helpers

from ckan import model

# For CKAN 2.10
import ckanext.provbz.views as views

# import ckanext.dcatapit.interfaces as interfaces

from ckan.common import _, ungettext

try:
    from ckan.lib.plugins import DefaultTranslation
except ImportError:
    class DefaultTranslation():
        pass

log = logging.getLogger(__name__)

class PBZThemePlugin(plugins.SingletonPlugin, DefaultTranslation):

    '''
    The Provincia di Bolzano theme plugin.
    '''

    # IConfigurer
    plugins.implements(plugins.IConfigurer)

    # ITemplateHelpers
    plugins.implements(plugins.ITemplateHelpers)

    # IRoutes (not available in CKAN 2.10)
    plugins.implements(plugins.IBlueprint)

    # ICustomSchema
    # plugins.implements(interfaces.ICustomSchema)

    # ITranslation
    if toolkit.check_ckan_version(min_version='2.10.4'):
        plugins.implements(plugins.ITranslation, inherit=True)

    # Implementation of ICustomSchema
    # ------------------------------------------------------------

    def get_custom_schema(self):
        return [
            {
                'name': 'creation_date',
                'validator': ['ignore_missing'],
                'element': 'input',
                'type': 'date',
                'label': _('Creation Date'),
                'format': '%d-%m-%Y',
                'placeholder': _('creation date'),
                'is_required': False,
                'localized': False
            },  {
                'name': 'encoding',
                'validator': ['ignore_missing'],
                'element': 'input',
                'type': 'text',
                'label': _('Encoding'),
                'placeholder': _('encoding type'),
                'is_required': False,
                'localized': False
            }, {
                'name': 'site_url',
                'validator': ['ignore_missing'],
                'element': 'input',
                'type': 'url',
                'label': _('Site URL'),
                'placeholder': _('site url'),
                'is_required': False,
                'localized': False
            }, {
                'name': 'contact',
                'validator': ['ignore_missing'],
                'element': 'input',
                'type': 'email',
                'label': _('Contact'),
                'placeholder': _('contact'),
                'is_required': False,
                'localized': False,
                'ignore_from_info': True
            }
        ]

    # Implementation of IConfigurer
    # ------------------------------------------------------------

    def update_config(self, config: CKANConfig):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('assets', 'provbz') # path, webasset name
        toolkit.add_public_directory(config, 'assets') # needed workaround to have webasset find files

    # Implementation of ITemplateHelpers
    # ------------------------------------------------------------

    def get_helpers(self):
        return {
            # 'recent_updates': helpers.recent_updates,
            'get_default_locale': helpers.get_default_locale,
            'get_locale': helpers.get_locale,
            'getLocalizedPageLink': helpers.getLocalizedPageLink,
            'parseRefDate': helpers.parseRefDate,
            'get_news_preview': helpers.get_news_preview,
            'checkForShibboletURL': helpers.checkForShibboletURL,
            'hacked_current_url': helpers.hacked_current_url,
        }

    # Implementation of IRoute
    # ------------------------------------------------------------
    def get_blueprint(self):
        return views.get_blueprints()
