# -*- coding:utf-8 -*-
import logging
from utils.data.manager.log.manage import Manage

log_manage = Manage('mongo_manage')
log_manage.set_handler('mongo_manage.log', logging.ERROR)
logger = log_manage.logger
