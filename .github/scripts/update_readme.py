import requests

# Fetch temperature data
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tel%20Aviv&appid=d59c4359779fe1b6e95b7f9cb73edf6e')
data = response.json()
temperature = data['main']['temp'] - 273.15

# Round the temperature to the nearest integer
temperature = round(temperature)

# Update README
with open('README.md', 'w') as f:
    f.write([![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=435&lines=Hello+%F0%9F%91%8B+welcome+to+my+GitHub+%F0%9F%94%A5)](https://git.io/typing-svg)+f'Current temperature in Tel Aviv: {temperature}C')
