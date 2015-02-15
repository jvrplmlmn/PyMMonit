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
        self._get('/index.csp')
        login_data = {
            "z_username": self.username,
            "z_password": self.password,
            "z_csrf_protection": "off"
        }
        self._post('/z_security_check', data=login_data)

    def _get(self, url):
        result = self.session.get(self.mmonit_url + url)
        return result.content

    def _post(self, url, data=None):
        result = self.session.post(self.mmonit_url + url, data)
        return result.content

    """
    http://mmonit.com/documentation/http-api/Methods/Status
    """
    def hosts_list(self):
        return self._get("/status/hosts/list")

    def hosts_get(self, host_id):
        return self._get("/status/hosts/get?id={}".format(host_id))

    def hosts_summary(self):
        return  self._get("/status/hosts/summary")

    """
    http://mmonit.com/documentation/http-api/Methods/Uptime
    """
    def uptime_hosts(self):
        return self._get("/reports/uptime/list")

    def uptime_services(self):
        return self._get("/reports/uptime/get")

    """
    http://mmonit.com/documentation/http-api/Methods/Events
    """
    def events_list(self):
        return self._get("/reports/events/list")

    def events_get(self, event_id):
        return self._get("/reports/events/get?id={}".format(event_id))

    def events_summary(self):
        return self._get("/reports/events/summary")

    def events_dismiss(self, event_id):
        return self._post("/reports/events/dismiss", event_id)
