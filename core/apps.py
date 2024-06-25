from django.apps import AppConfig
import logging


class CoreConfig(AppConfig):
    logger = logging.getLogger(__name__)
    name = 'core'
    logger.debug("Application started")
