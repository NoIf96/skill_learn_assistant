# -*- coding:utf-8 -*-
import logging
from utils.data.manager.log.manage import Manage

log_manage = Manage('worm_manage')
log_manage.set_handler('worm_manage.log', logging.ERROR)
logger = log_manage.logger
