import requests
from datetime import datetime
import os
import pytz
from PIL import Image
from io import BytesIO

# Fetch temperature data
api_key = os.getenv('WEATHER_API_KEY')
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=Tel%20Aviv&appid={api_key}')
data = response.json()
temperature = data['main']['temp'] - 273.15

# Round the temperature to the nearest integer
temperature = round(temperature)

# Get the current time in Tel Aviv
tel_aviv = pytz.timezone('Asia/Jerusalem')
now = datetime.now(tel_aviv)
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M")

# Fetch a random image from Lorem Picsum
response = requests.get('https://picsum.photos/5000')
image_data = response.content
image = Image.open(BytesIO(image_data))

# Save the image
image.save('random_image.jpg')

# Read existing README content
with open('README.md', 'r') as f:
    content = f.read()

# Find the index of the temperature line if it exists
index = content.find('Current temperature in Tel Aviv')

# If the temperature line exists, remove it
if index != -1:
    end_index = content.find('\n', index)
    content = content[:index] + content[end_index+1:]

# Append the temperature data and the current time to the README content
content += f'\nCurrent temperature in Tel Aviv: {temperature}°C, recorded on {current_date} at {current_time}\n'
content += f'\n![Random Image](random_image.jpg)\n'  # Add image to README

# Write the updated content to the README
with open('README.md', 'w') as f:
    f.write(content)
