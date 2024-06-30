# app.py (runs when application starts)

import logging

import logging.config # This is required. Otherwise, you get error: AttributeError: module 'logging' has no attribute 'config'

import os.path

import submodule as sm

def main():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default_handler': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'standard',

                #'filename': os.path.join('logs', 'application.log'),
                'filename': 'application.log',

                'encoding': 'utf8'
            },
        },
        'loggers': {
            '': {
                'handlers': ['default_handler'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger(__name__)
    logger.info("Application started.") 
    sm.do_something()

if __name__ == '__main__':
    main()