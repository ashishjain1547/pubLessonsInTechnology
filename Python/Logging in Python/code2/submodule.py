import logging

# define top level module logger
logger = logging.getLogger(__name__)

def do_something():
    
    logger.info('Something happended.')
    
    try:
        logger.info("In 'try'.")

    except Exception as e:
        logger.exception(e)
        logger.exception('Something broke.')
    
    