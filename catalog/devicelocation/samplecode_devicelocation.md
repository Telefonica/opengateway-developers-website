---
title: Sample code for Device Location Verification
excerpt: The following samples show how to use the [Open Gateway Device Location Verification API](https://opengateway.telefonica.com/en/apis/device-location), 
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

# First step:
# Perform an authorization request

customer_phone_number = "+34555555555"

client_id = "my-app-id"
client_secret = "my-app-secret"
app_credentials = f"{client_id}:{client_secret}"
credentials = base64.b64encode(app_credentials.encode('utf-8')).decode('utf-8')
api_scope = "dpv:FraudPreventionAndDetection#device-location-read"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {credentials}"
}

data = {
    "login_hint": f"phone_number:{customer_phone_number}",
    "scope": api_scope
}

response = requests.post(
    "https://opengateway.aggregator.com/bc-authorize",
    headers=headers,
    data=data
)

auth_req_id = response.json().get("auth_req_id")

# Second step:
# Requesting an access token with the auth_req_id included in the result above

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {credentials}"
}

data = {
    "grant_type": "urn:openid:params:grant-type:ciba",
    "auth_req_id": auth_req_id
}

response = requests.post(
    "https://opengateway.aggregator.com/token",
    headers=headers,
    data=data
)

access_token = response.json().get("access_token")
```

```python Sample SDK for Python
from opengateway_sandbox_sdk import ClientCredentials, DeviceLocation

credentials = ClientCredentials(
    client_id='yout_client_id',
    client_secret='your_client_secret'
    )
customer_phone_number = "+34666666666"

device_client = DeviceLocation(credentials=credentials, phone_number=customer_phone_number)
```
#### API usage

```python Sample HTTP with Python
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

data = {
    "ueId": { "msisdn": customer_phone_number }, # as set in the authorization step
    "latitude": 40.5150,
    "longitude": -3.6640,
    "accuracy": 2
}
response = requests.post(
    "https://opengateway.aggregator.com/location/v0/verify",
    headers=headers,
    json=data
)

result = response.json()

print (f"Is the device in location? {result.get("verificationResult")}")
```
```python Sample SDK for Python
    result = device_client.verify(phone_number, 40.5150, -3.6640, 50)

    print (f"Is the device in location? {result}")
```