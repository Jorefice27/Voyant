import requests
apiKey = 'af93fcaa320a01d0f242c67de449c02b'
print('Enter "weather" followed by the desired zip code (separated by a space) to receive the weather for an area in the USA. (weather {zip code})')
print('If you want the weather outside of the USA enter "weather" followed by the zip code, as well as the country code, separated by a space. (weather {zip code} { country code})')
print('Enter "Exit" to quit the program\n')
url = 'http://api.openweathermap.org/data/2.5/weather?'
while(True):
    userInput = input('$').strip()
    if userInput.lower() == 'exit':
        break

    arr = userInput.split(' ')
    if arr[0].lower() != 'weather':
        print('Request must begin with "weather"')
    else:
        if len(arr) == 3:
            r = requests.get(url=url, params={
                'zip': arr[1] + ',' + arr[2],
                'appId': apiKey,
            })
        elif len(arr) == 2:
            r = requests.get(url=url, params={
                'zip': arr[1],
                'appId': apiKey,
            })
        else:
            print('The form of the request was invalid')
            r = None
        if r is not None:
            resp = r.json()
            if resp['cod'] != 200:
                print('There was an error with your request: ' + resp['message'])
            else:
                print('{desc} {maxTemp} degrees Kelvin'.format(desc=resp['weather'][0]['main'], maxTemp=resp['main']['temp_max']))
