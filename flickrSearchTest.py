import requests
import json
import time

# Set for Search API
URL = 'https://api.flickr.com/services/rest/'
API_KEY = ''
USER_ID = ''
RESULT = 'Seartch_Result.txt'

payload = {
    'method': 'flickr.photos.search',               # API name
    'api_key': API_KEY,
    'user_id': USER_ID,                             # My flickr page
    'min_taken_date': '2017-03-04 00:00:00',        # Specify taken date range
    'max_taken_date': '2017-03-04 23:59:59',        # (MySQL datetime)
    'privacy_filter': '1',                          # Public
    'per_page': '10',                               # Request 10 pics
    'format': 'json',                               # JSON format
    'nojsoncallback': '1'                           # No callback
    }

# Search photos
print('Start Flickr search')

starttime = time.time()                             # Get start time
r = requests.get(URL, params=payload)               # Execute Search API
endtime = time.time() - starttime                   # Calc process time

# Output JSON data
sr_file = open(RESULT, 'w')
sr_file.write(json.dumps(r.json(), sort_keys=True, indent=2))
sr_file.close()

# ToDo - Format Flickr url list


print('Finish search\n' + '---> ' + 'search time: {0}'.format(endtime) + 'sec')