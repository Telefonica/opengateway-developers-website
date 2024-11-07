---
title: Sample code for Device Status
excerpt: The following samples show how to use the [Open Gateway Device Status API](https://opengateway.telefonica.com/en/apis/device-status), to control your resource management during international roaming more securely
category: 66aa4f941e51e7000fa353ce
---

The following code shows, for didactic purposes, a hypothetical or sample SDK, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator. The final implementation will depend on the channel partner's development tools offering. Note that channel partners' Open Gateway SDKs are just code modules wrapping authorization and API calls providing an interface in your app's programming for convenience.

This sample code consumes the API without an SDK, using direct HTTP requests. However, you can use an SDK if your aggregator provides one.

Note that currently, our Sandbox SDK does not have Device Status implemented.

> 📘 It is recomended to use the [API Reference tool](https://developers.opengateway.telefonica.com/reference/) for faster calls of our APIs

### Table of contents
- [Backend flow](#backend-flow)
    - [Authorization](#authorization)
    - [API usage](#api-usage)

## Code samples
> 📘 These are code examples
> - Remember to replace 'my-app-id' and 'my-app-secret' with the credentials of your app. (If you are using our Sandbox, you can get them [here](https://sandbox.opengateway.telefonica.com/my-apps)).
> - Remember also to change the urls with your aggregator urls. If you are using the Sandbox, the url is https://sandbox.opengateway.telefonica.com/apigateway/

### Backend flow

Most likely, this API will be consumed in a backend flow, since it is the application owner not the end-user who wants to take advantage of its functionality. The authorization protocol used in Open Gateway for backend flows is the OIDC standard CIBA (Client-Initiated Backchannel Authentication). You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#ciba-flow-backend-flow).

#### Authorization

```python Sample HTTP using Python
import requests
import base64
import sys

## App data
athorize_url = "https://opengateway.aggregator.com/bc-authorize"
token_url = "https://opengateway.aggregator.com/token"
verify_url = "https://sandbox.opengateway.agregator.com/device-status/v0/roaming"

client_id = "my-app-id"
client_secret = "my-app-secret"

## Basic Auth
def basic_auth():
    credentials = f"{client_id}:{client_secret}"
    return base64.b64encode(credentials.encode()).decode()

## CIBA
def cibauth(headers, number):
    payload = {
            "login_hint": number,
            "purpose": "dpv:FraudPreventionAndDetection#device-status-roaming-read"
    }
    try:
        response = requests.post(ciba_url, data=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("auth_req_id")
    except:
        status_code = response.status_code
        error_msg = response.json().get("error_description")
        print(f"1 - Error {status_code}: {error_msg}")
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
        print(f"2 - Error {status_code}: {error_msg}")
        sys.exit(1)
```

#### API usage

```python Sample HTTP with Python
# DEVICE STATUS
def verify_number(token, number):
    payload = {
            "ueId": { "msisdn": number },
    }
    headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {token}"
    }
    try:
        response = requests.post(verify_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
        #return response.text
    except:
        status_code = response.status_code
        error_msg = response.json().get("error")
        print(f"3 - Error {status_code}: {error_msg}")
        sys.exit(1)

# MAIN
if __name__ == "__main__":
    number = "+34666555343"
    credentials = basic_auth()
    headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "authorization": f"Basic {credentials}"
    }
    ciba_response = cibauth(headers, number)
    token = get_token(headers, ciba_response)
    verify = verify_number(token, number)
    print(f"Roaming: {verify.get("roaming")}\nCountry: {verify.get("countryCode")}")
```