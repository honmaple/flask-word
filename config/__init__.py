#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-18 07:20:38
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
import os

def load_config():
    mode = os.environ.get('MODE')
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'DEVELOPMENT':
            from .config import DevelopmentConfig
            return DevelopmentConfig
        else:
            from .config import DefaultConfig
            return DefaultConfig
    except:
        from .config import DefaultConfig
        return DefaultConfig
