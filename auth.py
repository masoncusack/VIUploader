import os
import requests
from dotenv import load_dotenv


def get_auth_token(svc_location: str, acct_id: str, apim_key: str) -> str:

    url = """
        https://api.videoindexer.ai/auth/{location}/Accounts/{account_id}/AccessToken?allowEdit=true
        """.format(
        location=svc_location, account_id=acct_id
    )

    headers = {"Ocp-Apim-Subscription-Key": apim_key}

    response = requests.request("GET", url, headers=headers)

    return response.text.strip('"')


if __name__ == "__main__":
  # Run as a separate script if you want.
    load_dotenv()
    token = get_auth_token(
        svc_location=os.getenv("LOCATION"),
        acct_id=os.getenv("ACCOUNT_ID"),
        apim_key=os.getenv("APIM_SUBSCRIPTION_KEY"),
    )

    print(token)
