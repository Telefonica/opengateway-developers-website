---
title: Sample code for Device Location Verification
excerpt: The following samples show how to use the [Open Gateway Device Location Verifiaction API](https://opengateway.telefonica.com/en/apis/device-status), 
category: 66aa4f941e51e7000fa353ce
---

The following code shows, for didactic purposes, a hypothetical or sample SDK, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator. The final implementation will depend on the channel partner's development tools offering. Note that channel partners' Open Gateway SDKs are just code modules wrapping authorization and API calls providing an interface in your app's programming for convenience.

> 📘 Want to give it a try before coding?
> Check the [API interactive reference](https://developers.opengateway.telefonica.com/reference/verifylocation-1)

### Table of contents
- [Backend flow](#backend-flow)
    - [Authorization](#authorization)
    - [API usage](#api-usage)

## Code samples

> 📘 Note
> These are code samples and not finalized ready-to-run code:
> - Remember to replace 'my-app-id' and 'my-app-secret' with the credentials of your app.
If you registered your test app on our Sandbox, you can retrieve its credentials [here](https://sandbox.opengateway.telefonica.com/my-apps). 
> - Remember also to replace "aggregator/opengateway-sdk" with the SDK from your aggregator.
If you are using our sandbox SDK, check info and installation of de Sandbox SDK [here](/docs/sdkreference)

### Backend flow

Most likely, this API will be consumed in a backend flow, since it is the application owner not the end-user who wants to take advantage of its functionality. The authorization protocol used in Open Gateway for backend flows is the OIDC standard CIBA (Client-Initiated Backchannel Authentication). You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#ciba-flow-backend-flow).

#### Authorization

```python Sample HTTP using Python
import requests
import base64
import sys

ciba_url = "https://sandbox.opengateway.telefonica.com/apigateway/bc-authorize"
token_url = "https://sandbox.opengateway.telefonica.com/apigateway/token"
verify_url = "https://sandbox.opengateway.telefonica.com/apigateway/location/v0/verify"

# AUTHENTICATION
## Basic Auth
def basic_auth():
    client_id='my-app-id',
    client_secret='my-app-secret'
    credentials = f"{client_id}:{client_secret}"
    return base64.b64encode(credentials.encode()).decode()

## CIBA
def cibauth(headers, number):
    payload = {
            "login_hint": number,
            "scope": "dpv:FraudPreventionAndDetection#device-location-read"
    }
    try:
        response = requests.post(ciba_url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("auth_req_id")
    except:
        status_code = response.status_code
        error_msg = response.json().get("error_description")
        print(f"Error {status_code}: {error_msg}")
        sys.exit(1)

## Token
def get_token(headers, ciba):
    payload = {
            "auth_req_id": ciba,
            "grant_type": "urn:openid:params:grant-type:ciba"
    }
    try:
        response = requests.post(token_url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("access_token")
    except:
        status_code = response.status_code
        error_msg = response.json().get("message")
        print(f"Error {status_code}: {error_msg}")
        sys.exit(1)

# Check if the number is in Distrito Telefónica
def verify_number(token, number):
    url = "https://sandbox.opengateway.telefonica.com/apigateway/location/v0/verify"
    payload = {
            "ueId": { "msisdn": "+34666666666" },
            "latitude": 40.5150,
            "longitude": -3.6640,
            "accuracy": 50
    }
    headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {token}"
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except:
        status_code = response.status_code
        error_msg = response.json().get("message")
        print(f"Error 3 {status_code}: {error_msg}")
        sys.exit(1)
```
```python Sample SDK for Python
import sys
from opengateway_sandbox_sdk import ClientCredentials, DeviceLocation

credentials = ClientCredentials(
    client_id='yout_client_id',
    client_secret='your_client_secret'
    )
phone_number = "+34666666666"
try:
    device_client = DeviceLocation(credentials, phone_number)
except:
    sys.exit(1)
```
#### API usage

```python Sample HTTP with Python
if __name__ == "__main__":
    number = "+34666666666"
    credentials = basic_auth()
    headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "authorization": f"Basic {credentials}"
    }
    ciba_response = cibauth(headers, number)
    token = get_token(headers, ciba_response)
    verify = verify_number(token, number)

    print(f"Is device {number} in Distrito Telefónica?: {verify.get("verificationResult")}")
```
```python Sample SDK for Python
    res = device_client.verify(phone_number, 40.5150, -3.6640, 50)

    print(res)
```