---
title: Sample code for Age Verification
excerpt: The following samples show how to use the [Open Gateway Age Verification API](https://opengateway.telefonica.com/en/apis/age-verification) to check if a subscriber meets a required age threshold, optionally including content lock or parental control information.
category: 681879c3afc1a0003709c745
---

The following code shows, for didactic purposes, a hypothetical or sample SDK, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator.

The final implementation will depend on the channel partner's development tools offering. Sample code on how to consume the API without an SDK, directly with HTTP requests, is also provided.

> 📘 Want to try it before coding?
> Check the [API interactive reference](https://developers.opengateway.telefonica.com/reference/verifyage)

### Table of contents
- [Backend flow](#backend-flow)
  - [Authorization](#authorization)
  - [API usage](#api-usage)
- [Frontend flow](#frontend-flow)
  - [Authorization code request](#authorization-code-request)
  - [Callback handling](#callback-handling)

## Backend flow

The authorization protocol used in Open Gateway for backend flows is the OIDC standard CIBA (Client-Initiated Backchannel Authentication). You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#ciba-flow-backend-flow).

### Authorization

```python Sample SDK for Python
from aggregator_opengateway_sdk import ClientCredentials, AgeVerifier

credentials = ClientCredentials(
    client_id='my-app-id',
    client_secret='my-app-secret'
)

age_client = AgeVerifier(credentials=credentials, phone_number='+34629255833')
```

```node Sample SDK for Node.js
import { ClientCredentials, AgeVerifier } from "aggregator/opengateway-sdk"

const credentials = new ClientCredentials({
    clientId: 'my-app-id',
    clientSecret: 'my-app-secret'
})

const customerPhoneNumber = '+34629255833'

const ageClient = new AgeVerifier(credentials, undefined, customerPhoneNumber)
```

```java Sample SDK for Java
import aggregator.opengatewaysdk.ClientCredentials;
import aggregator.opengatewaysdk.AgeVerifier;

ClientCredentials credentials = new ClientCredentials(
    "my-app-id",
    "my-app-secret"
);

final String customerPhoneNumber = "+34629255833";

AgeVerifier ageClient = new AgeVerifier(credentials, null, customerPhoneNumber);
```

```javascript HTTP using JavaScript (ES6)
let clientId = "my-app-id";
let clientSecret = "my-app-secret";
let appCredentials = btoa(`${clientId}:${clientSecret}`);
let scope = "dpv:FraudPreventionAndDetection kyc-age-verification:verify";

const tokenRequest = await fetch("https://opengateway.aggregator.com/token", {
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": `Basic ${appCredentials}`
  },
  body: new URLSearchParams({ scope })
});

const { access_token } = await tokenRequest.json();
```

### API usage

```python Sample SDK for Python
result = age_client.verify_age({
    "ageThreshold": 18,
    "idDocument": "12345678A",
    "givenName": "Federica",
    "familyName": "Sanchez",
    "birthdate": "1990-05-12",
    "email": "user@example.com",
    "includeContentLock": True,
    "includeParentalControl": True
})

print("Age check passed?", result.ageCheck)
print("Verified ID?", result.verifiedStatus)
print("Match score:", result.identityMatchScore)
print("Content lock:", result.contentLock)
print("Parental control:", result.parentalControl)
```

```node Sample SDK for Node.js
const result = await ageClient.verifyAge({
    ageThreshold: 18,
    idDocument: "12345678A",
    givenName: "Federica",
    familyName: "Sanchez",
    birthdate: "1990-05-12",
    email: "user@example.com",
    includeContentLock: true,
    includeParentalControl: true
})

console.log("Age check passed?", result.ageCheck)
console.log("Verified ID?", result.verifiedStatus)
console.log("Match score:", result.identityMatchScore)
console.log("Content lock:", result.contentLock)
console.log("Parental control:", result.parentalControl)
```

```java Sample SDK for Java
Map<String, Object> verificationData = new HashMap<>();
verificationData.put("ageThreshold", 18);
verificationData.put("idDocument", "12345678A");
verificationData.put("givenName", "Federica");
verificationData.put("familyName", "Sanchez");
verificationData.put("birthdate", "1990-05-12");
verificationData.put("email", "user@example.com");
verificationData.put("includeContentLock", true);
verificationData.put("includeParentalControl", true);

AgeVerificationResult result = ageClient.verifyAge(verificationData);

System.out.println("Age check passed? " + result.getAgeCheck());
System.out.println("Verified ID? " + result.getVerifiedStatus());
System.out.println("Match score: " + result.getIdentityMatchScore());
System.out.println("Content lock: " + result.getContentLock());
System.out.println("Parental control: " + result.getParentalControl());
```

```javascript HTTP using JavaScript (ES6)
const headers = new Headers();
headers.append("Authorization", `Bearer ${access_token}`);
headers.append("Content-Type", "application/json");

const payload = JSON.stringify({
  ageThreshold: 18,
  idDocument: "12345678A",
  givenName: "Federica",
  familyName: "Sanchez",
  birthdate: "1990-05-12",
  email: "user@example.com",
  includeContentLock: true,
  includeParentalControl: true
});

const response = await fetch("https://opengateway.aggregator.com/kyc-age-verification/v0.1/verify", {
  method: "POST",
  headers,
  body: payload
});

const result = await response.json();
console.log("Age check:", result.ageCheck);
console.log("Verified status:", result.verifiedStatus);
console.log("Match score:", result.identityMatchScore);
```

---

## Frontend flow

### Authorization code request

```javascript HTTP using JavaScript (ES6)
let clientId = "my-app-id";
let redirectUri = "https://myapp.com/age-callback";
let scope = "dpv:FraudPreventionAndDetection kyc-age-verification:verify";

const params = new URLSearchParams({
  client_id: clientId,
  response_type: "code",
  scope,
  redirect_uri: redirectUri
});

window.location.href = `https://opengateway.aggregator.com/authorize?${params.toString()}`;
```

### Callback handling

```python HTTP using Python + Flask
from flask import Flask, request
import requests, base64

client_id = "my-app-id"
client_secret = "my-app-secret"

app = Flask(__name__)

@app.route('/age-callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {credentials}"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "https://myapp.com/age-callback"
    }
    response = requests.post("https://opengateway.aggregator.com/token", headers=headers, data=data)
    access_token = response.json().get("access_token")
    return access_token

if __name__ == '__main__':
    app.run()