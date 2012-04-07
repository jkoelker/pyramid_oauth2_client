from pyramid_oauth2_client.facebook import FacebookClient
from pyramid_oauth2_client.github import GithubClient
from pyramid_oauth2_client.yasso import YassoClient


clients = {"facebook": FacebookClient,
           "github": GithubClient,
           "yasso": YassoClient,
          }


def get_oauth2_client(provider, request=None):
    """Return an OAuth2 client for the provider

    ``provider``
        The provider name to return the client for (str)
        Required.

        Supported providers:
            facebook
            github
            yasso

    ``request``
        A Pyramid request object. If provided the provider client class
        will be instantiated with the request.
    """
    client = clients[provider]
    if request:
        client = client(request)
    return client
