import requests

# Fetch temperature data
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tel%20Aviv&appid=d59c4359779fe1b6e95b7f9cb73edf6e')
data = response.json()
temperature = data['main']['temp'] - 273.15

# Round the temperature to the nearest integer
temperature = round(temperature)

# Read existing README content
with open('README.md', 'r') as f:
    content = f.read()

# Find the index of the temperature line if it exists
index = content.find('Current temperature in Tel Aviv')

# If the temperature line exists, remove it
if index != -1:
    end_index = content.find('\n', index)
    content = content[:index] + content[end_index+1:]

# Append the temperature data to the README content
content += f'\nCurrent temperature in Tel Aviv: {temperature}°C\n'

# Write the updated content to the README
with open('README.md', 'w') as f:
    f.write(content)
