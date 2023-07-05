import requests

# Fetch temperature data
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tel%20Aviv&appid=d59c4359779fe1b6e95b7f9cb73edf6e')
data = response.json()
temperature = data['main']['temp'] - 273.15

# Update README
with open('../../README.md', 'w') as f:
    f.write(f'Current temperature in Tel Aviv: {temperature}C')
