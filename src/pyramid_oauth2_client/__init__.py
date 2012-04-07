from pyramid import events

from pyramid_oauth2_client.facebook import FacebookClient
from pyramid_oauth2_client.github import GithubClient
from pyramid_oauth2_client.yasso import YassoClient


clients = {"facebook": FacebookClient,
           "github": GithubClient,
           "yasso": YassoClient,
          }


def oauth2_client(request, provider):
    """Return an OAuth2 client for the provider

    ``request``
        A Pyramid request object.
        Required.

    ``provider``
        The provider name to return the client for (str)
        Required.

        Supported providers:
            facebook
            github
            yasso
    """
    return clients[provider](request)


def includeme(config):
    """Set up standard configurator registrations. Use via:

    .. code-block:: python

    config = Configurator()
    config.include('pyramid_oauth2_client')
    """

    def new_request(event):
        request = event.request
        request.oauth2_client = lambda prov: oauth2_client(request, prov)

    def oauth2_default_provider(_request):
        return config.get_settings().get("oauth2.default_provider")

    config.add_subscriber(new_request, events.NewRequest)
    config.set_request_property(oauth2_default_provider, reify=True)
