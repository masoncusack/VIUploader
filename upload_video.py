import os
import requests

from dotenv import load_dotenv

load_dotenv()

url = """
      https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos?name={video_name}&privacy={privacy}&priority={priority}&description&language={language}&fileName={video_filename}&sendSuccessEmail={success_email}&accessToken={auth_token}
      """.format(
        location = os.getenv('LOCATION'),
        account_id = os.getenv('ACCOUNT_ID'),
        video_name = os.getenv('UPLOADED_VIDEO_NAME'),
        privacy = os.getenv('PRIVACY', default='private'),
        priority = os.getenv('PRIORITY', default='High'),
        language = os.getenv('VIDEO_LANGUAGE', default='English'),
        success_email = os.getenv('SUCCESS_EMAIL', default='True'),
        video_filename = os.getenv('VIDEO_FILENAME'),
        auth_token = os.getenv('AUTH_TOKEN')
      )

print("\nRequest url: {}".format(url))

files = {
  'file': ('', open(os.getenv('VIDEO_FILEPATH'),'rb'), 'multipart/form-data')
}
headers = {
  #'Content-Type': 'multipart/form-data',
  'Ocp-Apim-Subscription-Key': os.getenv('APIM_SUBSCRIPTION_KEY')
}

response = requests.post(url, headers=headers, files=files)

print(response.text.encode('utf8'))
