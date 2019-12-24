#!/usr/bin/python3
import logging

logger = logging.getLogger("rainwalker")

class Walker:
    def __init__(self, speed=1, height=1.8, width=0.3):
        logger.info("New walker created")

        self.speed = speed
        self.height = height
        self.width = width

        self.rain_amount = 0
        self.position = 0

    def move(self):
        update_rain()
        update_position()

    def update_position(self):
        self.position = self.position + speed
