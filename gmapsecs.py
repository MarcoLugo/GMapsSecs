#########################################################################################
# Title: gmapsecs
# Author: Marco Lugo
# Description: uses the Google Maps API to extract the travelling time in seconds from 
#              point A to point B with a specified mode of transportation (i.e. walking,
#              driving, transit, bycicling).
#
#              To get your own API key go to: 
#              https://developers.google.com/places/web-service/get-api-key
#########################################################################################

import sys
import urllib.request
import json

API_KEY = ''

def getGoogleMapsDirections(origin, destination, mode, api_key):
    URL = 'https://maps.googleapis.com/maps/api/directions/json?origin='+origin+'&destination='+destination+'&mode='+mode+'&key='+api_key
    try:
        request = urllib.request.urlopen(URL)
    except:
        return(-1)
    googleResponse = request.read()
    googleResponse = googleResponse.decode('utf8')
    result = json.loads(googleResponse)
    return(result)
    
def getGoogleMapsDirectionsSeconds(origin, destination, mode, api_key):
    results = getGoogleMapsDirections(origin, destination, mode, api_key)
    if(results == -1):
        return(-2) #Error detected with the HTTP request or the Google API
    duration_seconds = -1 #default value
    for route in results['routes']:
        for leg in route['legs']:
            duration_seconds = leg['duration']['value']
    return(duration_seconds)

def showHelp():
    print('Example usage: python ' + sys.argv[0] + ' origin destination mode')
    print(' - Addresses cannot have spaces')
    print(' - Available modes: driving, walking, transit, bycicling\n')
    print(' - The program will return -1 if no result was found with the given addresses and -2 if the address triggered an error in the request.')
    print('')
    print(' Example: python ' + sys.argv[0] + ' old+port+montreal mont+royal+montreal walking\n')



if __name__ == "__main__":
    if(len(sys.argv) != 4):
        print('ERROR: please review arguments\n')
        showHelp()
        exit()

    s = getGoogleMapsDirectionsSeconds(sys.argv[1], sys.argv[2], sys.argv[3], API_KEY)
    print(s)