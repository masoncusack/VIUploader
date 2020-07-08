import http.client, urllib.request, urllib.parse, urllib.error, base64
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Ocp-Apim-Subscription-Key': os.getenv('APIM_SUBSCRIPTION_KEY'),
}

# See API reference for below parameter and additional options:

params = urllib.parse.urlencode({
    # Request parameters
    'privacy': os.getenv('PRIVACY', default='Private'),
    'priority': os.getenv('PRIORITY', default='High'),
    'language': os.getenv('VIDEO_LANGUAGE', default='English'),
    'fileName': os.getenv('VIDEO_FILENAME'),
    'sendSuccessEmail': os.getenv('SEND_SUCCESS_EMAIL', default='True'),
    'accessToken': os.getenv('AUTH_TOKEN'),
})

location = os.getenv('LOCATION', default='westus2')
account_id = os.getenv('ACCOUNT_ID')
video_name = os.getenv('VIDEO_NAME', default='New%20Video')

# TODO: pull in file data from os as multipart form body

try:
    conn = http.client.HTTPSConnection('api.videoindexer.ai')
    conn.request("POST", "/" + location + "/Accounts/" + account_id + "/Videos?name=" + video_name + "&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
