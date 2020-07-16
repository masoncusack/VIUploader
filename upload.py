import os
import requests

from dotenv import load_dotenv


def upload_and_index(
    svc_location: str,
    acct_id: str,
    upload_name: str,
    privacy: str,
    priority: str,
    language: str,
    success_email: str,
    video_filename: str,
    auth_token: str,
    video_filepath: str,
    apim_key: str,
) -> str:

    url = (
        "https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos?"
        "name={upload_name}"
        "&privacy={privacy}"
        "&priority={priority}"
        "&description"
        "&language={language}"
        "&fileName={video_filename}"
        "&sendSuccessEmail={success_email}"
        "&accessToken={auth_token}"
    ).format(
        location=svc_location,
        account_id=acct_id,
        upload_name=upload_name,
        privacy=privacy,
        priority=priority,
        language=language,
        success_email=success_email,
        video_filename=video_filename,
        auth_token=auth_token,
    )

    print("\nYour request url:\n{}".format(url))

    files = {"file": ("", open(video_filepath, "rb"), "multipart/form-data")}

    headers = {"Ocp-Apim-Subscription-Key": apim_key}

    print("\nUploading...")
    response = requests.post(url, headers=headers, files=files)

    if response.status_code == "200":
        print("Video uploaded successfully. Head to https://videoindexer.ai to check it out.")
    
    return response.text


if __name__ == "__main__":
    # Run as a separate script if you want
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
    auth_token = os.getenv("AUTH_TOKEN")
    video_filepath = os.getenv("VIDEO_FILEPATH")
    apim_key = os.getenv("APIM_SUBSCRIPTION_KEY")
    
    res = upload_and_index(
        location,
        account_id,
        upload_name,
        privacy,
        priority,
        language,
        success_email,
        video_filename,
        auth_token,
        video_filepath,
        apim_key,
    )
    print(res)
