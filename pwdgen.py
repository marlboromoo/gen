#!/usr/bin/env python
# encoding: utf-8

import random
import string

def pwdgen(length=16):
    return ''.join(random.sample(
        "%s%s" % (string.ascii_letters, string.digits), length))

print pwdgen()
