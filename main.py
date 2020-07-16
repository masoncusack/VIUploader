"""
Do auth, upload and index a video in one go.
"""

import os
import argparse

from dotenv import load_dotenv

from auth import get_access_token
from upload import upload_and_index


if __name__ == "__main__":

    # Optional filepath arg allows upload of n videos to the same workspace over a short period
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", required=False, help="File path to the video to upload from your local system")
    args = parser.parse_args()

    load_dotenv()

    # Load env variables
    location = os.getenv("LOCATION")
    account_id = os.getenv("ACCOUNT_ID")
    upload_name = os.getenv("UPLOADED_VIDEO_NAME")
    privacy = os.getenv("PRIVACY", default="private")
    priority = os.getenv("PRIORITY", default="High")
    language = os.getenv("VIDEO_LANGUAGE", default="English")
    success_email = os.getenv("SUCCESS_EMAIL", default="True")
    video_filename = os.getenv("VIDEO_FILENAME")
    video_filepath = args.path if args.path else os.getenv("VIDEO_FILEPATH")
    apim_key = os.getenv("APIM_SUBSCRIPTION_KEY")

    # Get access token
    access_token = get_access_token(location, account_id, apim_key)
    print("Retrieved access token: \n{}".format(access_token))

    res = upload_and_index(
        location,
        account_id,
        upload_name,
        privacy,
        priority,
        language,
        success_email,
        video_filename,
        access_token,
        video_filepath,
        apim_key,
    )
    print(res)

