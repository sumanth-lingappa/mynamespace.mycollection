# -*- coding: utf-8 -*-

# Copyright (c) 2020 Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = """
---
name: test
short_description: Test lookup that does nothing
version_added: 0.1.0
author:
  - Felix Fontein (@felixfontein)
description:
  - A test lookup that really does nothing.
  - Ignore the argument spec, it's mainly there so this page looks nice.

options:
    _terms:
        description: URLs to query.
        required: true
        type: list
        elements: str
    method:
        description: HTTP method.
        type: str
        default: GET
    headers:
        description: HTTP headers.
        type: dict
    data:
        description: Data to send (Base64 encoded).
        type: str
    timeout:
        description:
            - Timeout in seconds
        type: float
        version_added: 0.7.0
    url_username:
        description:
            - The username for use with HTTP Basic Authentication.
        type: str
        version_added: 0.7.0
    url_password:
        description:
            - The password for use with HTTP Basic Authentication.
        type: str
        version_added: 0.7.0
    force_basic_auth:
        description:
            - Force passing C(Authorization) header on the first request when I(url_username) and I(url_password) are used.
        type: bool
        version_added: 0.7.0
"""

EXAMPLES = """
- name: Do a lookup
  ansible.builtin.debug:
    msg: "{{ lookup('mynamespace.mycollection.test', 'https://example.com', method='GET', headers={'foo': 'bar'}) }}"
"""

RETURN = """
_raw:
    description: Results of HTTP calls.
    type: list
    elements: dict
    returned: success
    contains:
        status:
            description: HTTP status of request.
            type: int
            sample: 200
        content:
            description: Content (Base64 encoded).
            type: str
            sample: 1.2.3.4
        headers:
            description: Headers.
            type: dict
            sample: {}
    sample:
        - status: 200
          content: 1.2.3.4
          headers: {}
"""

from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        self.set_options(direct=kwargs)

        return []
