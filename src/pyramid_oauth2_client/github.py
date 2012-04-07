
from pyramid_oauth2_client.abstract import AbstractOAuth2Client
import json
import requests


class GithubClient(AbstractOAuth2Client):
    """OAuth2 client Github"""
    authorize_url = "https://github.com/login/oauth/authorize"
    token_url = "https://github.com/login/oauth/access_token"

    def get_user(self):
        access_token = self.get_access_token()
        user_url = "https://api.github.com/user"
        r = requests.post(user_url, data={'access_token': access_token})
        r.raise_for_status()
        return json.loads(r.content)

    def get_userid(self):
        return self.get_user['id']
