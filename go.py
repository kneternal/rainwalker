#!/usr/bin/python3

import logging
import walker

logger = logging.getLogger("rainwalker")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)
logger.info("a")
w1 = walker.Walker()

