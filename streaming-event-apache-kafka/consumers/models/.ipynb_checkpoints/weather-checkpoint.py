"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        if 'weather' in message.topic():
            weather_info = message.value()
            self.temperature = weather_info['temperature']
            self.status = weather_info['status']
