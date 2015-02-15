# -*- coding: utf-8 -*-

import requests

__version__ = '0.1.0'
__author__ = 'Javier Palomo Almena'


class MMonit:

    def __init__(self, mmonit_url, username, password):
        self.mmonit_url = mmonit_url
        self.username = username
        self.password = password

        self.login()

    def login(self):
        self.session = requests.session()
        self.session.get(self.mmonit_url + '/index.csp')
        login_data = {
            "z_username": self.username,
            "z_password": self.password,
            "z_csrf_protection": "off"
        }
        self.session.post(self.mmonit_url + '/z_security_check', data=login_data)

    def _get(self, url):
        result = self.session.get(self.mmonit_url + url)
        return result.content

    def _post(self, url, data=None):
        result = self.session.post(self.mmonit_url + url, data)
        return result.content
