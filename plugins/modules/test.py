#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2020 Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: test
short_description: A module that does nothing
version_added: 0.1.0
author:
  - Felix Fontein (@felixfontein)
description:
  - This module does nothing. Really!
  - I want to extend this description because right now it's way too short.
    It does not contain anything really helpful to the user.
attributes:
  check_mode:
    description: Can run in C(check_mode) and return changed status prediction without modifying target.
    support: full
  diff_mode:
    description: Will return details on what has changed (or possibly needs changing in C(check_mode)), when in diff mode.
    support: partial
    details:
      - Only supports diff when nothing happens.
      - This is an excuse to write some details, nothing else.
  platform:
    description: Target OS/families that can be operated against.
    support: N/A
    platforms: POSIX

options:
  call_sequence:
    description: List of HTTP calls to make.
    type: list
    elements: dict
    required: true
    suboptions:
      url:
        description:
          - The URL.
          - It should be a plain URL that can be accessed via HTTP or HTTPS.
        type: str
        required: true
      method:
        description: HTTP method.
        type: str
        default: GET
      headers:
        description: HTTP headers.
        type: dict
      data:
        description:
          - Data to send (Base64 encoded).
          - Mutually exclusive with I(data_path).
        type: str
      data_path:
        description:
          - File to read data from.
          - Mutually exclusive with I(data).
        type: path
        version_added: 0.3.0
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
'''

EXAMPLES = r'''
- name: Does nothing
  mynamespace.mycollection.test:
    call_sequence: []
'''

RETURN = r'''
call_results:
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
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = dict(
        call_sequence=dict(type='list', elements='dict', required=True, options=dict(
            url=dict(type='str', required=True),
            method=dict(type='str', default='GET'),
            headers=dict(type='dict'),
            data=dict(type='str'),
            data_path=dict(type='path'),
            timeout=dict(type='float'),
            url_username=dict(type='str'),
            url_password=dict(type='str', no_log=True),
            force_basic_auth=dict(type='bool'),
        ), mutually_exclusive=[('data', 'data_path')]),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    module.exit_json(call_results=[], msg="I did nothing. Don't blame me!")


if __name__ == '__main__':
    main()
