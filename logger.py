#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging.config
from django.conf import settings

logger = logging.getLogger('django')
logging.config.dictConfig(settings.LOGGING)


if __name__ == '__main__':
    pass