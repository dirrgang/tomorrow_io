import os
import sys
import unittest

from dotenv import load_dotenv

from src.tomorrow_io.tomorrow import Tomorrow

# Get the parent directory of the current script (test_tomorrow.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Now you can perform the relative import

load_dotenv()

api_key = os.getenv("API_KEY")

# Create an instance of YourWeatherClass
weather_instance = Tomorrow(api_key=api_key, units="metric")


class TestYourWeatherClass(unittest.TestCase):
    def test_realtime(self):
        # Call the new function and check its output
        result = weather_instance.get_realtime()

        # Add your assertions here
        print(result)
        assert result is not None

    def test_forecast(self):
        weather_instance = Tomorrow(api_key=api_key, units="metric")

        result = weather_instance.get_forecast(timestep="")

        print(result)
        assert result is not None
