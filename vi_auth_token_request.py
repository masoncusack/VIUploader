import http.client
import mimetypes
import os

from dotenv import load_dotenv

load_dotenv()

location = os.getenv('LOCATION', default='westus2')
account_id = os.getenv('ACCOUNT_ID')

conn = http.client.HTTPSConnection("api.videoindexer.ai")
payload = ''
headers = {
  'Ocp-Apim-Subscription-Key': os.getenv('APIM_SUBSCRIPTION_KEY')
}
conn.request("GET", "/auth/" + location + "/Accounts/" + account_id + "/AccessToken?allowEdit=true", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))