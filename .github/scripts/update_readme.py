import requests

# Fetch temperature data
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=d59c4359779fe1b6e95b7f9cb73edf6e')
data = response.json()
temperature = data['main']['temp']

# Update README
with open('../../README.md', 'w') as f:
    f.write(f'Current temperature in London: {temperature}K')
